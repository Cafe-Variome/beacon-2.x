from typing import Optional
from beacon.db.filters import apply_filters
from beacon.db.schemas import DefaultSchemas
from beacon.db.utils import query_id, get_count, get_documents
from beacon.request.model import RequestParams
from beacon.db import client

import logging

LOG = logging.getLogger(__name__)


def get_datasets(entry_id: Optional[str], qparams: RequestParams):
    query = apply_filters({}, qparams.query.filters)
    schema = DefaultSchemas.DATASETS
    count = get_count(client.beacon.ejp, query)
    docs = get_documents(
        client.beacon.ejp,
        query,
        qparams.query.pagination.skip,
        qparams.query.pagination.limit
    )
    return schema, count, docs


def get_dataset_with_id(entry_id: Optional[str], qparams: RequestParams):
    query = apply_filters({}, qparams.query.filters)
    query = query_id(query, entry_id)
    schema = DefaultSchemas.DATASETS
    count = get_count(client.beacon.datasets, query)
    docs = get_documents(
        client.beacon.datasets,
        query,
        qparams.query.pagination.skip,
        qparams.query.pagination.limit
    )
    return schema, count, docs


def filter_public_datasets(requested_datasets_ids):
    query = {"dataUseConditions.duoDataUse.modifiers.id": "DUO:0000004"}
    return client.beacon.datasets \
        .find(query)
