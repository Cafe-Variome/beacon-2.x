import logging
import json
from typing import Optional
from beacon.db import client
from beacon.db.filters import apply_filters
from beacon.db.utils import query_id, get_documents, get_count
from beacon.request.model import RequestParams

LOG = logging.getLogger(__name__)


def get_filtering_terms(entry_id: Optional[str], qparams: RequestParams):
    filtering_terms = [
        {
            "type": "alphanumeric",
            "id": "id",
            "label": "The id of the resource"
        },
        {
            "type": "alphanumeric",
            "id": "name",
            "label": "The resource name"
        },
        {
            "type": "alphanumeric",
            "id": "description",
            "label": "A description of the resource"
        },
        {
            "type": "alphanumeric",
            "id": "resourceTypes",
            "label": "Unique identifier of the resource"
        }
    ]
    return "", "", filtering_terms
