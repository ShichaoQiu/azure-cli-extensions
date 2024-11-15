# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command_group(
    "deidservice",
    is_preview=True,
)
class __CMDGroup(AAZCommandGroup):
    """Health Data service for providing de-identification of health PHI data (Features: Surrogation, multi-modality)
    """
    pass


__all__ = ["__CMDGroup"]
