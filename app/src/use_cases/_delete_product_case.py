from decimal import Decimal
from ..core.enums import ProductStatuses
from ..core.models import Product
from ._requests import DeleteCaseProductRequest
from ._responses import DeleteCaseProductResponse


class DeleteProductCase:
    def __call__(
        self, request: DeleteCaseProductRequest
    ) -> DeleteCaseProductResponse | None:
        all_products = [
            Product(
                product_id="1",
                user_id="1",
                name="Headphones",
                description="Noise cancellation",
                price=Decimal(10.5),
                location="Quito",
                status=ProductStatuses.FOR_PARTS,
                is_available=True,
            ),
            Product(
                product_id="2",
                user_id="2",
                name="Jacket",
                description="Official ioet jacket",
                price=Decimal(20),
                location="Loja",
                status=ProductStatuses.USED,
                is_available=True,
            ),
            Product(
                product_id="3",
                user_id="3",
                name="Mac mini",
                description="With the M1 chip",
                price=Decimal(20),
                location="Guayaquil",
                status=ProductStatuses.NEW,
                is_available=False,
            ),
        ]

        for product in all_products:
            if product.product_id == request.product_id:
                all_products.remove(product)
                return DeleteCaseProductResponse(**product._asdict())

            return None
