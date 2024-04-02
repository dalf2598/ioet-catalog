from decimal import Decimal
from pydantic import BaseModel

from ..core.enums import ProductStatuses


class GetProductsRequest(BaseModel):
    status: ProductStatuses | None


class EditCaseProductRequest(BaseModel):
    product_id: str
    user_id: str
    name: str
    description: str | None
    price: Decimal
    location: str
    status: ProductStatuses
    is_available: bool


class DeleteCaseProductRequest(BaseModel):
    product_id: str
