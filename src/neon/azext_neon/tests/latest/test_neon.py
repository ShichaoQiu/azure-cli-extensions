# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

from azure.cli.testsdk import (ScenarioTest, ResourceGroupPreparer)
from azure.cli.testsdk.scenario_tests import AllowLargeResponse

class NeonScenario(ScenarioTest):
    @AllowLargeResponse(size_kb=10240)
    @ResourceGroupPreparer(name_prefix='cli_test_neon', location="eastus2euap")
    def test_neon(self, resource_group):
        self.kwargs.update({
            'name': 'NeonCLITestOrg1',
            'location': 'eastus2euap',
            'subscription': '00000000-0000-0000-0000-000000000000',
            'marketplace_subscription_id': 'yxmkfivp',
            'publisher_id': 'neon1722366567200',
            'offer_id': 'neon_test',
            'plan_id': 'neon_test_1',
            'plan_name': 'Neon Serverless Postgres - Free (Test_Liftr)',
            'term_unit': 'P1M',
            'term_id': 'gmz7xq9ge3py',
            'user_first_name': 'Almas',
            'user_last_name': 'Khan',
            'user_email': 'khanalmas@example.com',
            'user_upn': 'khanalmas_microsoft.com#EXT#@qumulotesttenant2.onmicrosoft.com',
            'user_phone': '+1234567890',
            'company_name': 'SampleCompany',
            'country': 'USA',
            'business_phone': '+1234567890',
            'office_address': '5678 Azure Blvd',
            'domain': 'samplecompany.com',
            'number_of_employees': 500,
            'organization_id': 'org67890',
            'org-name': 'PartnerOrgForCLITest1',
            'enterprise_app_id': 'app67890',
            'sso_url': 'https://sso.partnerorgtest.com',
            'aad_domain': 'partnerorgtest.com',
            'resource_group': 'NeonDemoRG'
        })

        # Create Neon Organization
        self.cmd('az neon postgres create --resource-group {resource_group} --name {name} --location {location} --subscription {subscription} '
                 '--marketplace-details \'{{"subscription-id": "{marketplace_subscription_id}", "subscription-status": "PendingFulfillmentStart", '
                 '"offer-details": {{"publisher-id": "{publisher_id}", "offer-id": "{offer_id}", "plan-id": "{plan_id}", "plan-name": "{plan_name}", "term-unit": "{term_unit}", "term-id": "{term_id}"}}}}\' '
                 '--user-details \'{{"first-name": "{user_first_name}", "last-name": "{user_last_name}", "email-address": "{user_email}", "upn": "{user_upn}", "phone-number": "{user_phone}"}}\' '
                 '--company-details \'{{"company-name": "{company_name}", "country": "{country}", "business-phone": "{business_phone}", "office-address": "{office_address}", "domain": "{domain}", "number-of-employees": {number_of_employees}}}\' '
                 '--partner-organization-properties \'{{"organization-id": "{organization_id}", "org-name": "{org-name}", '
                 '"single-sign-on-properties": {{"single-sign-on-state": "Enable", "enterprise-app-id": "{enterprise_app_id}", "single-sign-on-url": "{sso_url}", "aad-domains": ["{aad_domain}"]}}}}\'',
                 checks=[
                     self.check('name', '{name}'),
                 ])

        # List Neon Organizations
        self.cmd('az neon postgres organization list --subscription {subscription} --resource-group {resource_group}',
                 checks=[])

        # Show Neon Organization
        self.cmd('az neon postgres organization show --subscription {subscription} --resource-group {resource_group} --name {name}',
                 checks=[
                     self.check('name', '{name}'),
                 ])