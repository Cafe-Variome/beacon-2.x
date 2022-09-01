import logging
import json
from typing import Optional
from beacon.db import client
from beacon.db.filters import apply_filters
from beacon.db.utils import query_id, get_documents, get_count
from beacon.request.model import RequestParams

LOG = logging.getLogger(__name__)


def get_filtering_terms():
    filtering_terms = [
        {
            "type": "National Cancer Institute Thesaurus",
            "id": "obo:NCIT_C28421",
            "label": "Sex"
        },
        {
            "type": "Orphanet rare disease ontology",
            "id": "sio:SIO_001003",
            "label": "Diagnosis of the rare disease"
        },
        {
            "type": "Human Phenotype Ontology",
            "id": "	sio:SIO_010056",
            "label": "Phenotype"
        },
        {
            "type": "alphanumeric",
            "id": "obo:NCIT_C16612",
            "label": "Causative genes"
        },
        {
            "type": "alphanumeric",
            "id": "obo:NCIT_C25150",
            "label": "age this year"
        },
        {
            "type": "alphanumeric",
            "id": "efo:EFO_0004847",
            "label": "Age at disease manifestation"
        },
        {
            "type": "alphanumeric",
            "id": "obo:NCIT_C156420",
            "label": "Age at diagnosis"
        },
        {
            "type": "alphanumeric",
            "id": "availableMaterials",
            "label": "available materials"
        }
    ]
    return filtering_terms

def get_resources():
    resources = [
        {
            "id": "ncit",
            "name": "National Cancer Institute Thesaurus",
            "url": "http://purl.obolibrary.org/obo/ncit.owl",
            "version": "22.03d",
            "nameSpacePrefix": "NCIT",
            "iriPrefix": "http://purl.obolibrary.org/obo/NCIT_"
        },
        {
            "id": "ordo",
            "name": "Orphanet rare disease ontology",
            "url": "http://www.orpha.net/version4.1",
            "version": "4.1",
            "nameSpacePrefix": "orphanet",
            "iriPrefix": "http://www.orpha.net/ORDO/Orphanet_"
        },
        {
            "id": "hp",
            "name": "Human Phenotype Ontology",
            "url": "http://purl.obolibrary.org/obo/hp.owl",
            "version": "2022-06-11",
            "nameSpacePrefix": "HP",
            "iriPrefix": "http://purl.obolibrary.org/obo/HP_"
        }
    ]

    return resources
