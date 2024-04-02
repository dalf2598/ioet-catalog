from decimal import Decimal
from app.src.core import ProductStatuses
from app.src.use_cases import (
    DeleteProductCase,
    DeleteCaseProductRequest,
    DeleteCaseProductResponse,
)


class TestEditProductsCase:

    def test_should_delete_product(self):

        request = DeleteCaseProductRequest(
            product_id="1",
        )

        use_case = DeleteProductCase()

        response = use_case(request=request)

        expected_response = DeleteCaseProductResponse(
            product_id="1",
            user_id="1",
            name="Headphones",
            description="Noise cancellation",
            price=Decimal(10.5),
            location="Quito",
            status=ProductStatuses.FOR_PARTS,
            is_available=True,
        )

        assert isinstance(response, DeleteCaseProductResponse)
        assert response == expected_response

    def test_return_none_because_product_with_non_existent_id(self):

        request = DeleteCaseProductRequest(
            product_id="666",
        )

        use_case = DeleteProductCase()

        response = use_case(request=request)

        assert response is None
