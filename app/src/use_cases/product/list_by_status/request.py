from typing import NamedTuple
from ....core.enums._product_statuses import ProductStatuses


class ListProductsByStatusRequest(NamedTuple):
    status: ProductStatuses
