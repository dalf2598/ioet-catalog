from typing import List

from fastapi import APIRouter, Depends

from app.src.use_cases import (
    ListProducts,
    ListProductResponse,
    ListProductsByStatus,
    ListProductsByStatusRequest,
    ListProductsByStatusResponse,
    FindProductById,
    FindProductByIdResponse,
    FindProductByIdRequest,
    CreateProduct,
    CreateProductResponse,
    CreateProductRequest,
    EditProduct,
    EditProductResponse,
    EditProductRequest,
    DeleteProduct,
    DeleteProductResponse,
    DeleteProductRequest,
)
from ..dtos import (
    ProductBase,
    ListProductResponseDto,
    ListProductsByStatusResponseDto,
    CreateProductRequestDto,
    CreateProductResponseDto,
    FindProductByIdResponseDto,
    EditProductRequestDto,
    EditProductResponseDto,
    DeleteProductResponseDto,
)
from factories.use_cases import (
    list_product_use_case,
    list_product_by_status_use_case,
    find_product_by_id_use_case,
    create_product_use_case,
    edit_product_use_case,
    delete_product_use_case,
)
from app.src.core.models import Product

product_router = APIRouter(prefix="/products")


@product_router.get("/", response_model=ListProductResponseDto)
async def get_products(
    use_case: ListProducts = Depends(list_product_use_case),
) -> ListProductResponse:
    response = use_case()
    response_dto: ListProductResponseDto = ListProductResponseDto(
        products=[ProductBase(**product._asdict()) for product in response.products]
    )
    return response_dto


@product_router.get("/status/{status}", response_model=ListProductsByStatusResponseDto)
async def get_products_by_status(
    status: str,
    use_case: ListProductsByStatus = Depends(list_product_by_status_use_case),
) -> ListProductsByStatusResponse:
    response = use_case(ListProductsByStatusRequest(status=status))
    response_dto: ListProductsByStatusResponseDto = ListProductsByStatusResponseDto(
        products=[ProductBase(**product._asdict()) for product in response.products]
    )
    return response_dto


@product_router.get("/{product_id}", response_model=FindProductByIdResponseDto)
async def get_product_by_id(
    product_id: str, use_case: FindProductById = Depends(find_product_by_id_use_case)
) -> FindProductByIdResponse:
    response = use_case(FindProductByIdRequest(product_id=product_id))
    response_dto: FindProductByIdResponseDto = FindProductByIdResponseDto(
        **response._asdict()
    )
    return response_dto


@product_router.post("/", response_model=CreateProductResponseDto)
async def edit_product(
    request: CreateProductRequestDto,
    use_case: CreateProduct = Depends(create_product_use_case),
) -> CreateProductResponse:
    response = use_case(
        CreateProductRequest(
            product_id=request.product_id,
            user_id=request.user_id,
            name=request.name,
            description=request.description,
            price=request.price,
            location=request.location,
            status=request.status.value,
            is_available=request.is_available,
        )
    )
    response_dto: CreateProductResponseDto = CreateProductResponseDto(
        **response._asdict()
    )
    return response_dto


@product_router.put("/", response_model=EditProductResponseDto)
async def edit_product(
    request: EditProductRequestDto,
    use_case: EditProduct = Depends(edit_product_use_case),
) -> EditProductResponse:
    response = use_case(
        EditProductRequest(
            product_id=request.product_id,
            user_id=request.user_id,
            name=request.name,
            description=request.description,
            price=request.price,
            location=request.location,
            status=request.status.value,
            is_available=request.is_available,
        )
    )
    response_dto: EditProductResponseDto = EditProductResponseDto(**response._asdict())
    return response_dto


@product_router.delete("/{product_id}", response_model=DeleteProductResponseDto)
async def delete_product_by_id(
    product_id: str, use_case: DeleteProduct = Depends(delete_product_use_case)
) -> DeleteProductResponse:
    response = use_case(DeleteProductRequest(product_id=product_id))
    response_dto: DeleteProductResponseDto = DeleteProductResponseDto(
        **response._asdict()
    )
    return response_dto
