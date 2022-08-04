import logging
from beacon.db.filtering_terms import get_filtering_terms

LOG = logging.getLogger(__name__)


def validate_filters(json_body=None):
    supported = [filter["id"] for filter in get_filtering_terms()]
    supplied = [filter["id"] for filter in json_body["query"]["filters"]]
    return set(supplied) - set(supported)