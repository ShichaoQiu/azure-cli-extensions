# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import yaml
from azext_confcom import config
from azext_confcom import oras_proxy
from azext_confcom.cose_proxy import CoseSignToolProxy
from azext_confcom.template_util import (
    case_insensitive_dict_get,
    extract_containers_from_text,
)


# input is the full rego file as a string
# output is all of the containers in the rego files as a list of dictionaries
def combine_fragments_with_policy(all_fragments):
    out_fragments = []
    for fragment in all_fragments:
        container_text = extract_containers_from_text(fragment, "containers := ")
        container_text = container_text.replace("\t", "    ")
        containers = yaml.load(container_text, Loader=yaml.FullLoader)
        out_fragments.extend(containers)
    return out_fragments


def get_all_fragment_contents(fragment_imports):
    fragment_feeds = [
        case_insensitive_dict_get(fragment, config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_FEED)
        for fragment in fragment_imports
    ]

    all_fragments_contents = []
    cose_proxy = CoseSignToolProxy()

    for fragment in fragment_imports:
        # pull locally if there is a path, otherwise pull from the remote registry
        if (
            config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_PATH in fragment and
            fragment[config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_PATH]
        ):
            contents = [
                cose_proxy.extract_payload_from_path(
                    fragment[config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_PATH]
                )
            ]
        else:
            feed_name = case_insensitive_dict_get(
                fragment, config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_FEED
            )
            contents = oras_proxy.pull_all_image_attached_fragments(feed_name)

        # add the new fragments to the list of all fragments if they're not already there
        # the side effect of adding this way is that if we have a local path to a nested fragment
        # we will pull then use the local version of the fragment instead of pulling from the registry
        for content in contents:
            fragment_text = extract_containers_from_text(
                content, config.REGO_FRAGMENT_START
            ).replace("\t", "    ")

            fragments = yaml.load(
                fragment_text,
                Loader=yaml.FullLoader,
            )

            # this adds new feeds to the list of feeds to pull dynamically
            # it will end when there are no longer nested fragments to pull
            for new_fragment in fragments:
                if new_fragment[config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_FEED] not in fragment_feeds:
                    fragment_imports.append(new_fragment[config.POLICY_FIELD_CONTAINERS_ELEMENTS_REGO_FRAGMENTS_FEED])

            all_fragments_contents.append(content)

    return combine_fragments_with_policy(all_fragments_contents)