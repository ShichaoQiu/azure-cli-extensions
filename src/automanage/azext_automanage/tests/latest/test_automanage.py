# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import *
from time import sleep

class AutomanageScenario(ScenarioTest):
    @ResourceGroupPreparer(location='eastus2euap', name_prefix='clitest.rg.automanage.')
    def test_automanage_scenarios(self):
        # best-practice
        best_practice_name = self.cmd('az automanage best-practice list').get_output_in_json()
        if best_practice_name and len(best_practice_name) >= 2:
            best_practice_name = best_practice_name[1]["name"]
            self.cmd('az automanage best-practice show --best-practice-name {}'.format(best_practice_name))

            version_name = self.cmd('az automanage best-practice version list '
                                    '--best-practice-name {}'.format(best_practice_name)).get_output_in_json()
            if version_name and len(version_name) >= 1:
                version_name = version_name[0]["name"].split('/')[1]

                self.cmd('az automanage best-practice version show --best-practice-name {} --version-name '
                         '{}'.format(best_practice_name, version_name))

        # service-principal
        self.cmd('az automanage service-principal list')
        self.cmd('az automanage service-principal show-default')

    @ResourceGroupPreparer(location='eastus2euap', name_prefix='clitest.rg.automanage.configurationprofile.')
    def test_automanage_configuration_profile_scenarios(self):
        self.kwargs.update({
            'profile_name': self.create_random_name(prefix='profile', length=24),
            'version_name': self.create_random_name(prefix='version', length=24)
        })
        self.cmd('az automanage configuration-profile create -n {profile_name} -g {rg} --configuration '
                 '{{\\\"Antimalware/Enable\\\":false,\\\"Backup/Enable\\\":false,\\\"VMInsights/Enable\\\":true,'
                 '\\\"AzureSecurityCenter/Enable\\\":true,\\\"UpdateManagement/Enable\\\":true,'
                 '\\\"ChangeTrackingAndInventory/Enable\\\":true,\\\"GuestConfiguration/Enable\\\":true,'
                 '\\\"LogAnalytics/Enable\\\":true,\\\"BootDiagnostics/Enable\\\":true}}')
        self.cmd('az automanage configuration-profile show -n {profile_name} -g {rg}',
                 checks=[JMESPathCheck('name', self.kwargs.get('profile_name', '')),
                         JMESPathCheck('properties.configuration', {"Antimalware/Enable": False,
                                                                    "AzureSecurityCenter/Enable": True,
                                                                    "Backup/Enable": False,
                                                                    "BootDiagnostics/Enable": True,
                                                                    "ChangeTrackingAndInventory/Enable": True,
                                                                    "GuestConfiguration/Enable": True,
                                                                    "LogAnalytics/Enable": True,
                                                                    "UpdateManagement/Enable": True,
                                                                    "VMInsights/Enable": True})])
        self.cmd('az automanage configuration-profile list -g {rg}', checks=[JMESPathCheck('length(@)', 1)])
        self.cmd('az automanage configuration-profile update -n {profile_name} -g {rg} --configuration '
                 '{{\\\"Antimalware/Enable\\\":true,\\\"VMInsights/Enable\\\":false}}',
                 checks=[JMESPathCheck('properties.configuration', {"Antimalware/Enable": True,
                                                                    "VMInsights/Enable": False})])

        # # version
        self.cmd('az automanage configuration-profile version create --profile-name {profile_name} -g {rg} '
                 '-n {version_name} --configuration {{\\\"Antimalware/Enable\\\":false}}')
        self.cmd('az automanage configuration-profile version show --profile-name {profile_name} -g {rg} '
                 '-n {version_name}',
                 checks=[JMESPathCheck('name', self.kwargs.get('version_name', '')),
                         JMESPathCheck('properties.configuration', {"Antimalware/Enable": False})])
        self.cmd('az automanage configuration-profile version list --profile-name {profile_name} -g {rg}',
                 checks=[JMESPathCheck('length(@)', 1)])
        self.cmd('az automanage configuration-profile version update --profile-name {profile_name} -g {rg} '
                 '-n {version_name} --configuration {{\\\"Antimalware/Enable\\\":true}}',
                 checks=[JMESPathCheck('properties.configuration', {"Antimalware/Enable": True})])
        self.cmd('az automanage configuration-profile version delete --profile-name {profile_name} -g {rg} '
                 '-n {version_name} -y')
        self.cmd('az automanage configuration-profile version list --profile-name {profile_name} -g {rg}',
                 checks=[JMESPathCheck('length(@)', 0)])

        self.cmd('az automanage configuration-profile delete -n {profile_name} -g {rg} -y')
        self.cmd('az automanage configuration-profile list -g {rg}', checks=[JMESPathCheck('length(@)', 0)])

    @ResourceGroupPreparer(location='eastus2euap', name_prefix='clitest.rg.automanage.profileassignment.vm.')
    def test_automanage_configuration_profile_assignment_vm_scenarios(self):
        self.kwargs.update({
            'profile_name': self.create_random_name(prefix='profile', length=24),
            'vm_name': self.create_random_name(prefix='vm', length=24),
            'profile_name_2': self.create_random_name(prefix='profile', length=24),
        })
        profile_id = self.cmd('az automanage configuration-profile create -n {profile_name} -g {rg} '
                              '--configuration {{\\\"Antimalware/Enable\\\":true}}').get_output_in_json()["id"]
        self.kwargs.update({'profile_id': profile_id})
        vm_id = self.cmd('az vm create -n {vm_name} -g {rg} --image UbuntuLTS --generate-ssh-keys '
                         '--public-ip-sku Standard').get_output_in_json()["id"]
        self.cmd('az automanage configuration-profile-assignment vm create -n default -g {rg} '
                 '--vm-name {vm_name} --configuration-profile {profile_id}')
        self.cmd('az automanage configuration-profile-assignment vm show -n default -g {rg} --vm-name {vm_name}',
                 checks=[JMESPathCheck('name', 'default'),
                         JMESPathCheck('properties.configurationProfile', profile_id),
                         JMESPathCheck('properties.targetId', vm_id)])
        self.cmd('az automanage configuration-profile-assignment list -g {rg}', checks=[JMESPathCheck('length(@)', 1)])

        profile_id_2 = self.cmd('az automanage configuration-profile create -n {profile_name_2} -g {rg} '
                                '--configuration {{\\\"Antimalware/Enable\\\":false}}').get_output_in_json()["id"]
        self.kwargs.update({'profile_id_2': profile_id_2})
        self.cmd('az automanage configuration-profile-assignment vm update --n default -g {rg} '
                 '--vm-name {vm_name} --configuration-profile {profile_id_2}',
                 checks=[JMESPathCheck('properties.configurationProfile', profile_id_2),
                         JMESPathCheck('properties.targetId', vm_id)])

        sleep(10)
        report_name = self.cmd('az automanage configuration-profile-assignment vm report list --assignment-name default'
                               ' -g {rg} --vm-name {vm_name}').get_output_in_json()[0]["name"]
        self.kwargs.update({'report_name': report_name})
        self.cmd('az automanage configuration-profile-assignment vm report show -n {report_name} '
                 '--assignment-name default -g {rg} --vm-name {vm_name}')

        self.cmd('az automanage configuration-profile-assignment vm delete -n default -g {rg} --vm-name {vm_name} -y')
        self.cmd('az automanage configuration-profile-assignment list -g {rg}', checks=[JMESPathCheck('length(@)', 0)])

    @record_only()
    # need to first run：
    # az group create -l eastus2euap -g rgtestautomanage
    # (run as admin in Powershell) Connect-AzConnectedMachine -ResourceGroupName rgtestautomanage -Name arc1 -Location eastus2euap
    def test_automanage_configuration_profile_assignment_arc_scenarios(self):
        self.kwargs.update({
            'profile_name': self.create_random_name(prefix='profile', length=24),
            'rg': 'rgtestautomanage',
            'arc_name': 'arc1',
            'profile_name_2': self.create_random_name(prefix='profile', length=24),
        })
        profile_id = self.cmd('az automanage configuration-profile create -n {profile_name} -g {rg} '
                              '--configuration {{\\\"Antimalware/Enable\\\":true}}').get_output_in_json()["id"]
        self.kwargs.update({'profile_id': profile_id})

        self.cmd('az automanage configuration-profile-assignment arc create -n default -g {rg} '
                 '--machine-name {arc_name} --configuration-profile {profile_id}')
        self.cmd('az automanage configuration-profile-assignment arc show -n default -g {rg} --machine-name {arc_name}',
                 checks=[JMESPathCheck('name', 'default'),
                         JMESPathCheck('properties.configurationProfile', profile_id)])
        self.cmd('az automanage configuration-profile-assignment list -g {rg}', checks=[JMESPathCheck('length(@)', 1)])

        profile_id_2 = self.cmd('az automanage configuration-profile create -n {profile_name_2} -g {rg} '
                                '--configuration {{\\\"Antimalware/Enable\\\":false}}').get_output_in_json()["id"]
        self.kwargs.update({'profile_id_2': profile_id_2})
        self.cmd('az automanage configuration-profile-assignment arc update --n default -g {rg} '
                 '--machine-name {arc_name} --configuration-profile {profile_id_2}',
                 checks=[JMESPathCheck('properties.configurationProfile', profile_id_2)])

        sleep(20)
        report_name = self.cmd('az automanage configuration-profile-assignment arc report list --assignment-name '
                               'default -g {rg} --machine-name {arc_name}').get_output_in_json()[0]["name"]
        self.kwargs.update({'report_name': report_name})
        self.cmd('az automanage configuration-profile-assignment arc report show -n {report_name} '
                 '--assignment-name default -g {rg} --machine-name {arc_name}')

        self.cmd('az automanage configuration-profile-assignment arc delete -n default -g {rg} --machine-name '
                 '{arc_name} -y')
        self.cmd('az automanage configuration-profile-assignment list -g {rg}', checks=[JMESPathCheck('length(@)', 0)])

    @record_only()
    # self.cmd('az stack-hci cluster create --cluster-name {cluster_name} -g {rg}')
    @ResourceGroupPreparer(location='eastus2euap', name_prefix='clitest.rg.automanage.profileassignment.cluster.')
    def test_automanage_configuration_profile_assignment_cluster_scenarios(self):
        self.kwargs.update({
            'profile_name': self.create_random_name(prefix='profile', length=24),
            'cluster_name': 'cluster1',
            'profile_name_2': self.create_random_name(prefix='profile', length=24),
        })
        profile_id = self.cmd('az automanage configuration-profile create -n {profile_name} -g {rg} '
                              '--configuration {{\\\"Antimalware/Enable\\\":true}}').get_output_in_json()["id"]
        self.kwargs.update({'profile_id': profile_id})

        self.cmd('az automanage configuration-profile-assignment cluster create -n default -g {rg} '
                 '--cluster-name {cluster_name} --configuration-profile {profile_id}')
        self.cmd('az automanage configuration-profile-assignment cluster show -n default -g {rg} '
                 '--cluster-name {cluster_name}',
                 checks=[JMESPathCheck('name', 'default'),
                         JMESPathCheck('properties.configurationProfile', profile_id)])
        self.cmd('az automanage configuration-profile-assignment list -g {rg}', checks=[JMESPathCheck('length(@)', 1)])

        profile_id_2 = self.cmd('az automanage configuration-profile create -n {profile_name_2} -g {rg} '
                                '--configuration {{\\\"Antimalware/Enable\\\":false}}').get_output_in_json()["id"]
        self.kwargs.update({'profile_id_2': profile_id_2})
        self.cmd('az automanage configuration-profile-assignment cluster update --n default -g {rg} '
                 '--cluster-name {cluster_name} --configuration-profile {profile_id_2}',
                 checks=[JMESPathCheck('properties.configurationProfile', profile_id_2)])

        sleep(20)
        report_name = self.cmd('az automanage configuration-profile-assignment cluster report list --assignment-name '
                               'default -g {rg} --cluster-name {cluster_name}').get_output_in_json()[0]["name"]
        self.kwargs.update({'report_name': report_name})
        self.cmd('az automanage configuration-profile-assignment cluster report show -n {report_name} '
                 '--assignment-name default -g {rg} --cluster-name {cluster_name}')

        self.cmd('az automanage configuration-profile-assignment cluster delete -n default -g {rg} --cluster-name '
                 '{cluster_name} -y')
        self.cmd('az automanage configuration-profile-assignment list -g {rg}', checks=[JMESPathCheck('length(@)', 0)])