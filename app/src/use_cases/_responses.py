from decimal import Decimal

from pydantic import BaseModel

from ..core.enums import ProductStatuses


class GetProductResponse(BaseModel):
    product_id: str
    name: str
    price: Decimal
    status: ProductStatuses
    is_available: bool


class GetProductsResponse(BaseModel):
    products: list[GetProductResponse]


class EditCaseProductResponse(BaseModel):
    product_id: str
    user_id: str
    name: str
    description: str | None
    price: Decimal
    location: str
    status: ProductStatuses
    is_available: bool
