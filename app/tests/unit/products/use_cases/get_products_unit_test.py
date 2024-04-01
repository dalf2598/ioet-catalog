import pytest
from app.src.use_cases import GetProductsCase, GetProductsRequest, GetProductsResponse
from app.src.core.enums import ProductStatuses


class TestGetProductsCase:
    def test__returns_a_list_of_products(self):
        expected_products = 3
        request = GetProductsRequest(status=None)
        use_case = GetProductsCase()

        response = use_case(request=request)

        assert isinstance(response, GetProductsResponse)
        assert len(response.products) == expected_products

    @pytest.mark.parametrize("status", ProductStatuses)
    def test__returns_a_list_of_products_by_status(self, status):
        request = GetProductsRequest(status=status.value)
        use_case = GetProductsCase()

        response = use_case(request=request)

        assert isinstance(response, GetProductsResponse)
        for product in response.products:
            assert product.status == status
