import logging
from beacon.db.filtering_terms import get_filtering_terms

LOG = logging.getLogger(__name__)


def validate_filters(json_body=None):
    supported = [filter["id"] for filter in get_filtering_terms()]
    supplied = [filter["id"] for filter in json_body["query"]["filters"]]
    LOG.debug(supplied)
    LOG.debug(supported)
    LOG.debug(set(supplied) - set(supported))
    if set(supplied) - set(supported) != set():
        LOG.debug("False")
    else:
        LOG.debug("True")
    return set(supplied) - set(supported)
