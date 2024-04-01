from http import HTTPStatus
import pytest
from pytest_mock import MockFixture
from fastapi.testclient import TestClient
from app.src import ProductStatuses
from app.src.use_cases.product import ListProductResponse


def test_should_return_a_list_of_products(mocker: MockFixture, api_client: TestClient):
    mock_list_products_response = [
        {
            "product_id": "1",
            "user_id": "1",
            "name": "Product 1",
            "description": "Product 1 description",
            "price": "10.0",
            "location": "Location 1",
            "status": "New",
            "is_available": True,
        }
    ]
    mocker.patch(
        "app.src.use_cases.product.list_all.use_case.ListProducts.__call__",
        return_value=ListProductResponse(products=mock_list_products_response),
    )

    response = api_client.get("/products/")
    products = response.json().get("products")
    assert response.status_code == HTTPStatus.OK
    assert products == mock_list_products_response


@pytest.mark.parametrize("status", ProductStatuses)
def test_should_return_a_list_of_products_by_status(
    mocker: MockFixture, api_client: TestClient, status: str
):
    mock_list_products_response = [
        {
            "product_id": "1",
            "user_id": "1",
            "name": "Product 1",
            "description": "Product 1 description",
            "price": "10.0",
            "location": "Location 1",
            "status": "New",
            "is_available": True,
        }
    ]
    mocker.patch(
        "app.src.use_cases.product.list_by_status.use_case.ListProductsByStatus.__call__",
        return_value=ListProductResponse(products=mock_list_products_response),
    )

    response = api_client.get(f"/products/status/{status}")
    products = response.json().get("products")
    assert response.status_code == HTTPStatus.OK
    assert products == mock_list_products_response
