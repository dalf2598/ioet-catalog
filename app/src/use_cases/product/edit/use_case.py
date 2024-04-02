from typing import Any, Optional

from app.src.core import Product
from app.src.repositories import ProductRepository
from app.src.exceptions import (
    ProductNoneException,
    ProductRepositoryException,
    ProductBusinessException,
    ProductNotFoundException,
)

from .response import EditProductResponse
from .request import EditProductRequest


class EditProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __verify_product_exists(
        self, product: Optional[Product], request_entity_id: str
    ) -> None:
        if product is None:
            raise ProductNotFoundException(product_id=request_entity_id)

    def __call__(self, request: EditProductRequest) -> Optional[EditProductResponse]:
        product = Product(**request._asdict())
        try:
            existing_product = self.product_repository.get_by_id(request.product_id)
            self.__verify_product_exists(
                existing_product, request_entity_id=request.product_id
            )
            response: Optional[Product] = self.product_repository.edit(product)
            if not response:
                raise ProductNoneException()

            return EditProductResponse(**response._asdict())
        except ProductRepositoryException as e:
            raise ProductBusinessException(str(e))
