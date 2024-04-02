from decimal import Decimal
from app.src.use_cases import (
    EditProductCase,
    EditCaseProductRequest,
    EditCaseProductResponse,
)


class TestEditProductsCase:

    def test_should_edit_product(self):

        request = EditCaseProductRequest(
            product_id="1",
            user_id="1",
            name="Headphones",
            description="Noise cancellation",
            price=Decimal(8.5),
            location="Quito",
            status="Used",
            is_available=False,
        )

        use_case = EditProductCase()

        response = use_case(request=request)

        assert isinstance(response, EditCaseProductResponse)
        assert response == EditCaseProductResponse(**vars(request))

    def test_return_none_because_product_with_non_existent_id(self):

        request = EditCaseProductRequest(
            product_id="666",
            user_id="1",
            name="Headphones",
            description="Noise cancellation",
            price=Decimal(8.5),
            location="Quito",
            status="Used",
            is_available=False,
        )

        use_case = EditProductCase()

        response = use_case(request=request)

        assert response is None
