"""
Beacon Framework Configuration Endpoints.
"""

# import logging

from beacon import conf

# LOG = logging.getLogger(__name__)
from beacon.db.schemas import DefaultSchemas

from beacon.utils.stream import json_stream


def get_entry_types():
    return {
        "dataset": {
            "id": "dataset",
            "name": "Dataset",
            "ontologyTermForThisType": {
                "id": "NCIT:C47824",
                "label": "Data set"
            },
            "partOfSpecification": "Beacon v2.0.0",
            "description": "A Dataset is a collection of records, like rows in a database or cards in a cardholder.",
            "defaultSchema": {
                "id": "EJP_catalogue_v3",
                "name": "EJP demo metadata model",
                "referenceToSchemaDefinition": "",
                "schemaVersion": "v3"
            },
            "additionalSupportedSchemas": []
        }

    }


async def configuration(request):
    meta = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/sections/beaconInformationalResponseMeta.json',
        'beaconId': conf.beacon_id,
        'apiVersion': conf.api_version,
        'returnedSchemas': []
    }

    response = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/configuration/beaconConfigurationSchema.json',
        'maturityAttributes': {
            'productionStatus': 'DEV'
        },
        'securityAttributes': {
            'defaultGranularity': 'record',
            'securityLevels': ['PUBLIC', 'REGISTERED', 'CONTROLLED']
        },
        'entryTypes': get_entry_types()
    }

    configuration_json = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/beaconConfigurationResponse.json',
        'meta': meta,
        'response': response
    }

    return await json_stream(request, configuration_json)


async def entry_types(request):
    meta = {
        'beaconId': conf.beacon_id,
        'apiVersion': conf.api_version,
        'returnedSchemas': []
    }

    response = {
        "entryTypes": get_entry_types()
    }

    entry_types_json = {
        'meta': meta,
        'response': response
    }

    return await json_stream(request, entry_types_json)


async def beacon_map(request):
    meta = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/sections/beaconInformationalResponseMeta.json',
        'beaconId': conf.beacon_id,
        'apiVersion': conf.api_version,
        'returnedSchemas': []
    }

    response = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/configuration/beaconMapSchema.json',
        "endpointSets": {
            "catalogue": {
                "entryType": "catalogue",
                "openAPIEndpointsDefinition": "https://github.com/ejp-rd-vp/query_builder_api/blob/feat/beacon_version/versions/v3/specification.yaml",
                "rootUrl": conf.uri + "/api/catalogue",
                "singleEntryUrl": conf.uri + "/api/catalogue/{id}",
                "filteringTermsUrl": conf.uri + "/api/catalogue/{id}/filtering_terms",
                "endpoints": {
                }
            }
        }
    }

    beacon_map_json = {
        'meta': meta,
        'response': response
    }

    return await json_stream(request, beacon_map_json)
