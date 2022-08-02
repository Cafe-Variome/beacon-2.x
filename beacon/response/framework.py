"""
Beacon Framework Configuration Endpoints.
"""

# import logging

from beacon import conf, epnd_conf

# LOG = logging.getLogger(__name__)
from beacon.db.schemas import DefaultSchemas

from beacon.utils.stream import json_stream


def get_entry_types():
    return {
        "epnd-entry": {
            "id": "epnd-entry",
            "name": "EPND Draft Entry",
            "ontologyTermForThisType": {
                "id": "ABC:123",
                "label": "EPND Draft Term"
            },
            "partOfSpecification": "Beacon v2.0.0",
            "description": "A Dataset is a collection of records, like rows in a database or cards in a cardholder.",
            "defaultSchema": {
                "id": "epnd_schema",
                "name": "EPND Draft schema",
                "referenceToSchemaDefinition": "",
                "schemaVersion": "v0.1"
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


async def epnd_configuration(request):
    meta = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/sections/beaconInformationalResponseMeta.json',
        'beaconId': epnd_conf.beacon_id,
        'apiVersion': epnd_conf.api_version,
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


async def epnd_entry_types(request):
    meta = {
        'beaconId': epnd_conf.beacon_id,
        'apiVersion': epnd_conf.api_version,
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
            "analysis": {
                "entryType": "analysis",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/analyses/endpoints.json",
                "rootUrl": conf.uri + "/api/analyses",
                "singleEntryUrl": conf.uri + "/api/analyses/{id}",
                "endpoints": {
                    "genomicVariation": {
                        "returnedEntryType": "genomicVariation",
                        "url": conf.uri + "/api/analyses/{id}/g_variants"
                    },
                }
            },
            "biosample": {
                "entryType": "biosample",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/biosamples/endpoints.json",
                "rootUrl": conf.uri + "/api/biosamples",
                "singleEntryUrl": conf.uri + "/api/biosamples/{id}",
                "endpoints": {
                    "analysis": {
                        "returnedEntryType": "analysis",
                        "url": conf.uri + "/api/biosamples/{id}/analyses"
                    },
                    "genomicVariation": {
                        "returnedEntryType": "genomicVariation",
                        "url": conf.uri + "/api/biosamples/{id}/g_variants"
                    },
                    "run": {
                        "returnedEntryType": "run",
                        "url": conf.uri + "/api/biosamples/{id}/runs"
                    },
                }
            },
            "cohort": {
                "entryType": "cohort",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/cohorts/endpoints.json",
                "rootUrl": conf.uri + "/api/cohorts",
                "singleEntryUrl": conf.uri + "/api/cohorts/{id}",
                "filteringTermsUrl": conf.uri + "/api/cohorts/{id}/filtering_terms",
                "endpoints": {
                    "analysis": {
                        "returnedEntryType": "analysis",
                        "url": conf.uri + "/api/cohorts/{id}/analyses"
                    },
                    "individual": {
                        "returnedEntryType": "individual",
                        "url": conf.uri + "/api/cohorts/{id}/individuals"
                    },
                    "run": {
                        "returnedEntryType": "run",
                        "url": conf.uri + "/api/cohorts/{id}/runs"
                    }
                }
            },
            "dataset": {
                "entryType": "dataset",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/datasets/endpoints.json",
                "rootUrl": conf.uri + "/api/datasets",
                "singleEntryUrl": conf.uri + "/api/datasets/{id}",
                "filteringTermsUrl": conf.uri + "/api/datasets/{id}/filtering_terms",
                "endpoints": {
                    "analysis": {
                        "returnedEntryType": "analysis",
                        "url": conf.uri + "/api/datasets/{id}/analyses"
                    },
                    "biosample": {
                        "returnedEntryType": "biosample",
                        "url": conf.uri + "/api/datasets/{id}/biosamples"
                    },
                    "genomicVariation": {
                        "returnedEntryType": "genomicVariation",
                        "url": conf.uri + "/api/datasets/{id}/g_variants"
                    },
                    "individual": {
                        "returnedEntryType": "individual",
                        "url": conf.uri + "/api/datasets/{id}/individuals"
                    },
                    "run": {
                        "returnedEntryType": "run",
                        "url": conf.uri + "/api/datasets/{id}/runs"
                    }
                }
            },
            "genomicVariation": {
                "entryType": "genomicVariation",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/genomicVariations/endpoints.json",
                "rootUrl": conf.uri + "/api/g_variants",
                "singleEntryUrl": conf.uri + "/api/g_variants/{id}",
                "endpoints": {
                    "analysis": {
                        "returnedEntryType": "analysis",
                        "url": conf.uri + "/api/g_variants/{id}/analyses"
                    },
                    "biosample": {
                        "returnedEntryType": "biosample",
                        "url": conf.uri + "/api/g_variants/{id}/biosamples"
                    },
                    "individual": {
                        "returnedEntryType": "individual",
                        "url": conf.uri + "/api/g_variants/{id}/individuals"
                    },
                    "run": {
                        "returnedEntryType": "run",
                        "url": conf.uri + "/api/g_variants/{id}/runs"
                    }
                }
            },
            "individual": {
                "entryType": "individual",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/individuals/endpoints.json",
                "rootUrl": conf.uri + "/api/individuals",
                "singleEntryUrl": conf.uri + "/api/individuals/{id}",
                "filteringTermsUrl": conf.uri + "/api/individuals/{id}/filtering_terms",
                "endpoints": {
                    "analysis": {
                        "returnedEntryType": "analysis",
                        "url": conf.uri + "/api/individuals/{id}/analyses"
                    },
                    "biosample": {
                        "returnedEntryType": "biosample",
                        "url": conf.uri + "/api/individuals/{id}/biosamples"
                    },
                    "genomicVariation": {
                        "returnedEntryType": "genomicVariation",
                        "url": conf.uri + "/api/individuals/{id}/g_variants"
                    },
                    "run": {
                        "returnedEntryType": "run",
                        "url": conf.uri + "/api/individuals/{id}/runs"
                    }
                }
            },
            "run": {
                "entryType": "run",
                "openAPIEndpointsDefinition": "https://raw.githubusercontent.com/ga4gh-beacon/beacon-v2-Models/main/BEACON-V2-Model/runs/endpoints.json",
                "rootUrl": conf.uri + "/api/runs",
                "singleEntryUrl": conf.uri + "/api/runs/{id}",
                "endpoints": {
                    "analysis": {
                        "returnedEntryType": "analysis",
                        "url": conf.uri + "/api/runs/{id}/analyses"
                    },
                    "genomicVariation": {
                        "returnedEntryType": "genomicVariation",
                        "url": conf.uri + "/api/runs/{id}/g_variants"
                    },
                }
            },
        }
    }

    beacon_map_json = {
        'meta': meta,
        'response': response
    }

    return await json_stream(request, beacon_map_json)


async def epnd_beacon_map(request):
    meta = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/responses/sections/beaconInformationalResponseMeta.json',
        'beaconId': epnd_conf.beacon_id,
        'apiVersion': epnd_conf.api_version,
        'returnedSchemas': []
    }

    response = {
        '$schema': 'https://raw.githubusercontent.com/ga4gh-beacon/beacon-framework-v2/main/configuration/beaconMapSchema.json',
        "endpointSets": {

            "epnd-entry": {
                "entryType": "epnd-entry",
                "rootUrl": epnd_conf.uri + "/api/epnd",
            }
        }
    }

    beacon_map_json = {
        'meta': meta,
        'response': response
    }

    return await json_stream(request, beacon_map_json)
