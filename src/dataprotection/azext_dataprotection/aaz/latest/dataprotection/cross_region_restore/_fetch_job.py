# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


class FetchJob(AAZCommand):
    """Fetches a single Cross Region Restore Job
    """

    _aaz_info = {
        "version": "2024-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/locations/{}/fetchcrossregionrestorejob", "2024-04-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            required=True,
            id_part="name",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.job_id = AAZStrArg(
            options=["--job-id"],
            arg_group="Parameters",
            required=True,
        )
        _args_schema.source_backup_vault_id = AAZStrArg(
            options=["--source-backup-vault-id"],
            arg_group="Parameters",
            required=True,
        )
        _args_schema.source_region = AAZStrArg(
            options=["--source-region"],
            arg_group="Parameters",
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.FetchCrossRegionRestoreJobGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class FetchCrossRegionRestoreJobGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/locations/{location}/fetchCrossRegionRestoreJob",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "location", self.ctx.args.location,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-04-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("jobId", AAZStrType, ".job_id", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("sourceBackupVaultId", AAZStrType, ".source_backup_vault_id", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("sourceRegion", AAZStrType, ".source_region", typ_kwargs={"flags": {"required": True}})

            return self.serialize_content(_content_value)

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.activity_id = AAZStrType(
                serialized_name="activityID",
                flags={"required": True},
            )
            properties.backup_instance_friendly_name = AAZStrType(
                serialized_name="backupInstanceFriendlyName",
                flags={"required": True},
            )
            properties.backup_instance_id = AAZStrType(
                serialized_name="backupInstanceId",
                flags={"read_only": True},
            )
            properties.data_source_id = AAZStrType(
                serialized_name="dataSourceId",
                flags={"required": True},
            )
            properties.data_source_location = AAZStrType(
                serialized_name="dataSourceLocation",
                flags={"required": True},
            )
            properties.data_source_name = AAZStrType(
                serialized_name="dataSourceName",
                flags={"required": True},
            )
            properties.data_source_set_name = AAZStrType(
                serialized_name="dataSourceSetName",
            )
            properties.data_source_type = AAZStrType(
                serialized_name="dataSourceType",
                flags={"required": True},
            )
            properties.destination_data_store_name = AAZStrType(
                serialized_name="destinationDataStoreName",
            )
            properties.duration = AAZStrType()
            properties.end_time = AAZStrType(
                serialized_name="endTime",
                flags={"read_only": True},
            )
            properties.error_details = AAZListType(
                serialized_name="errorDetails",
                flags={"read_only": True},
            )
            properties.etag = AAZStrType()
            properties.extended_info = AAZObjectType(
                serialized_name="extendedInfo",
            )
            properties.is_user_triggered = AAZBoolType(
                serialized_name="isUserTriggered",
                flags={"required": True},
            )
            properties.operation = AAZStrType(
                flags={"required": True},
            )
            properties.operation_category = AAZStrType(
                serialized_name="operationCategory",
                flags={"required": True},
            )
            properties.policy_id = AAZStrType(
                serialized_name="policyId",
                flags={"read_only": True},
            )
            properties.policy_name = AAZStrType(
                serialized_name="policyName",
                flags={"read_only": True},
            )
            properties.progress_enabled = AAZBoolType(
                serialized_name="progressEnabled",
                flags={"required": True},
            )
            properties.progress_url = AAZStrType(
                serialized_name="progressUrl",
                flags={"read_only": True},
            )
            properties.rehydration_priority = AAZStrType(
                serialized_name="rehydrationPriority",
                flags={"read_only": True},
            )
            properties.restore_type = AAZStrType(
                serialized_name="restoreType",
                flags={"read_only": True},
            )
            properties.source_data_store_name = AAZStrType(
                serialized_name="sourceDataStoreName",
            )
            properties.source_resource_group = AAZStrType(
                serialized_name="sourceResourceGroup",
                flags={"required": True},
            )
            properties.source_subscription_id = AAZStrType(
                serialized_name="sourceSubscriptionID",
                flags={"required": True},
            )
            properties.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"required": True},
            )
            properties.status = AAZStrType(
                flags={"required": True},
            )
            properties.subscription_id = AAZStrType(
                serialized_name="subscriptionId",
                flags={"required": True},
            )
            properties.supported_actions = AAZListType(
                serialized_name="supportedActions",
                flags={"required": True},
            )
            properties.vault_name = AAZStrType(
                serialized_name="vaultName",
                flags={"required": True},
            )

            error_details = cls._schema_on_200.properties.error_details
            error_details.Element = AAZObjectType()
            _FetchJobHelper._build_schema_user_facing_error_read(error_details.Element)

            extended_info = cls._schema_on_200.properties.extended_info
            extended_info.additional_details = AAZDictType(
                serialized_name="additionalDetails",
            )
            extended_info.backup_instance_state = AAZStrType(
                serialized_name="backupInstanceState",
                flags={"read_only": True},
            )
            extended_info.data_transferred_in_bytes = AAZFloatType(
                serialized_name="dataTransferredInBytes",
                flags={"read_only": True},
            )
            extended_info.recovery_destination = AAZStrType(
                serialized_name="recoveryDestination",
                flags={"read_only": True},
            )
            extended_info.source_recover_point = AAZObjectType(
                serialized_name="sourceRecoverPoint",
            )
            _FetchJobHelper._build_schema_restore_job_recovery_point_details_read(extended_info.source_recover_point)
            extended_info.sub_tasks = AAZListType(
                serialized_name="subTasks",
                flags={"read_only": True},
            )
            extended_info.target_recover_point = AAZObjectType(
                serialized_name="targetRecoverPoint",
            )
            _FetchJobHelper._build_schema_restore_job_recovery_point_details_read(extended_info.target_recover_point)
            extended_info.warning_details = AAZListType(
                serialized_name="warningDetails",
                flags={"read_only": True},
            )

            additional_details = cls._schema_on_200.properties.extended_info.additional_details
            additional_details.Element = AAZStrType(
                flags={"read_only": True},
            )

            sub_tasks = cls._schema_on_200.properties.extended_info.sub_tasks
            sub_tasks.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.extended_info.sub_tasks.Element
            _element.additional_details = AAZDictType(
                serialized_name="additionalDetails",
            )
            _element.task_id = AAZIntType(
                serialized_name="taskId",
                flags={"required": True},
            )
            _element.task_name = AAZStrType(
                serialized_name="taskName",
                flags={"required": True},
            )
            _element.task_progress = AAZStrType(
                serialized_name="taskProgress",
                flags={"read_only": True},
            )
            _element.task_status = AAZStrType(
                serialized_name="taskStatus",
                flags={"required": True},
            )

            additional_details = cls._schema_on_200.properties.extended_info.sub_tasks.Element.additional_details
            additional_details.Element = AAZStrType(
                flags={"read_only": True},
            )

            warning_details = cls._schema_on_200.properties.extended_info.warning_details
            warning_details.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.extended_info.warning_details.Element
            _element.resource_name = AAZStrType(
                serialized_name="resourceName",
            )
            _element.warning = AAZObjectType(
                flags={"required": True},
            )
            _FetchJobHelper._build_schema_user_facing_error_read(_element.warning)

            supported_actions = cls._schema_on_200.properties.supported_actions
            supported_actions.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            return cls._schema_on_200


class _FetchJobHelper:
    """Helper class for FetchJob"""

    _schema_inner_error_read = None

    @classmethod
    def _build_schema_inner_error_read(cls, _schema):
        if cls._schema_inner_error_read is not None:
            _schema.additional_info = cls._schema_inner_error_read.additional_info
            _schema.code = cls._schema_inner_error_read.code
            _schema.embedded_inner_error = cls._schema_inner_error_read.embedded_inner_error
            return

        cls._schema_inner_error_read = _schema_inner_error_read = AAZObjectType()

        inner_error_read = _schema_inner_error_read
        inner_error_read.additional_info = AAZDictType(
            serialized_name="additionalInfo",
        )
        inner_error_read.code = AAZStrType()
        inner_error_read.embedded_inner_error = AAZObjectType(
            serialized_name="embeddedInnerError",
        )
        cls._build_schema_inner_error_read(inner_error_read.embedded_inner_error)

        additional_info = _schema_inner_error_read.additional_info
        additional_info.Element = AAZStrType()

        _schema.additional_info = cls._schema_inner_error_read.additional_info
        _schema.code = cls._schema_inner_error_read.code
        _schema.embedded_inner_error = cls._schema_inner_error_read.embedded_inner_error

    _schema_restore_job_recovery_point_details_read = None

    @classmethod
    def _build_schema_restore_job_recovery_point_details_read(cls, _schema):
        if cls._schema_restore_job_recovery_point_details_read is not None:
            _schema.recovery_point_id = cls._schema_restore_job_recovery_point_details_read.recovery_point_id
            _schema.recovery_point_time = cls._schema_restore_job_recovery_point_details_read.recovery_point_time
            return

        cls._schema_restore_job_recovery_point_details_read = _schema_restore_job_recovery_point_details_read = AAZObjectType()

        restore_job_recovery_point_details_read = _schema_restore_job_recovery_point_details_read
        restore_job_recovery_point_details_read.recovery_point_id = AAZStrType(
            serialized_name="recoveryPointID",
        )
        restore_job_recovery_point_details_read.recovery_point_time = AAZStrType(
            serialized_name="recoveryPointTime",
        )

        _schema.recovery_point_id = cls._schema_restore_job_recovery_point_details_read.recovery_point_id
        _schema.recovery_point_time = cls._schema_restore_job_recovery_point_details_read.recovery_point_time

    _schema_user_facing_error_read = None

    @classmethod
    def _build_schema_user_facing_error_read(cls, _schema):
        if cls._schema_user_facing_error_read is not None:
            _schema.code = cls._schema_user_facing_error_read.code
            _schema.details = cls._schema_user_facing_error_read.details
            _schema.inner_error = cls._schema_user_facing_error_read.inner_error
            _schema.is_retryable = cls._schema_user_facing_error_read.is_retryable
            _schema.is_user_error = cls._schema_user_facing_error_read.is_user_error
            _schema.message = cls._schema_user_facing_error_read.message
            _schema.properties = cls._schema_user_facing_error_read.properties
            _schema.recommended_action = cls._schema_user_facing_error_read.recommended_action
            _schema.target = cls._schema_user_facing_error_read.target
            return

        cls._schema_user_facing_error_read = _schema_user_facing_error_read = AAZObjectType()

        user_facing_error_read = _schema_user_facing_error_read
        user_facing_error_read.code = AAZStrType()
        user_facing_error_read.details = AAZListType()
        user_facing_error_read.inner_error = AAZObjectType(
            serialized_name="innerError",
        )
        cls._build_schema_inner_error_read(user_facing_error_read.inner_error)
        user_facing_error_read.is_retryable = AAZBoolType(
            serialized_name="isRetryable",
        )
        user_facing_error_read.is_user_error = AAZBoolType(
            serialized_name="isUserError",
        )
        user_facing_error_read.message = AAZStrType()
        user_facing_error_read.properties = AAZDictType()
        user_facing_error_read.recommended_action = AAZListType(
            serialized_name="recommendedAction",
        )
        user_facing_error_read.target = AAZStrType()

        details = _schema_user_facing_error_read.details
        details.Element = AAZObjectType()
        cls._build_schema_user_facing_error_read(details.Element)

        properties = _schema_user_facing_error_read.properties
        properties.Element = AAZStrType()

        recommended_action = _schema_user_facing_error_read.recommended_action
        recommended_action.Element = AAZStrType()

        _schema.code = cls._schema_user_facing_error_read.code
        _schema.details = cls._schema_user_facing_error_read.details
        _schema.inner_error = cls._schema_user_facing_error_read.inner_error
        _schema.is_retryable = cls._schema_user_facing_error_read.is_retryable
        _schema.is_user_error = cls._schema_user_facing_error_read.is_user_error
        _schema.message = cls._schema_user_facing_error_read.message
        _schema.properties = cls._schema_user_facing_error_read.properties
        _schema.recommended_action = cls._schema_user_facing_error_read.recommended_action
        _schema.target = cls._schema_user_facing_error_read.target


__all__ = ["FetchJob"]