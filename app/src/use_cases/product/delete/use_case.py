from typing import Optional

from app.src.exceptions import (
    ProductNoneException,
    ProductNotFoundException,
    ProductRepositoryException,
)

from app.src.core.models import Product
from app.src.repositories import ProductRepository

from .request import DeleteProductRequest
from .response import DeleteProductResponse


class DeleteProduct:
    def __init__(self, product_repository: ProductRepository) -> None:
        self.product_repository = product_repository

    def __verify_product_exists(
        self, product: Optional[Product], request_entity_id: str
    ) -> None:
        if product is None:
            raise ProductNotFoundException(product_id=request_entity_id)

    def __call__(self, request: DeleteProductRequest) -> DeleteProductResponse:
        try:
            existing_product = self.product_repository.get_by_id(request.product_id)
            self.__verify_product_exists(
                existing_product, request_entity_id=request.product_id
            )

            response: Optional[Product] = self.product_repository.delete(
                request.product_id
            )
            if not response:
                raise ProductNoneException()

            return DeleteProductResponse(**response._asdict())

        except ProductRepositoryException as e:
            raise e
