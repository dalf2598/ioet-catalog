from ..use_cases import GetProductsCase, EditProductCase


def get_products_case() -> GetProductsCase:
    return GetProductsCase()


def edit_product_case() -> EditProductCase:
    return EditProductCase()
