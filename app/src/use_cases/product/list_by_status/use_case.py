from typing import Any
from app.src.exceptions.repository.product import ProductRepositoryException
from app.src.repositories import ProductRepository
from app.src.use_cases.product.list_by_status.request import ListProductsByStatusRequest
from .response import ListProductsByStatusResponse


class ListProductsByStatus:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(
        self, request: ListProductsByStatusRequest
    ) -> ListProductsByStatusResponse:
        try:
            products = self.product_repository.list_all()
            products_by_status = filter(
                lambda product: product.status == request.status, products
            )
            return ListProductsByStatusResponse(products=products_by_status)
        except ProductRepositoryException as error:
            raise ProductRepositoryException(str(error))
