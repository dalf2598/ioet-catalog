from typing import List, Optional
from app.src import ProductRepository, ProductRepositoryException, Product


class MemoryProductRepository(ProductRepository):
    products: List[Product]

    def __init__(self) -> None:
        self.products = []

    def list_all(self) -> List[Product]:
        try:
            return self.products
        except ProductRepositoryException:
            raise ProductRepositoryException(method="list")

    def create(self, product: Product) -> Product:
        try:
            self.products.append(product)
            return product
        except Exception:
            raise ProductRepositoryException(method="create")

    def get_by_id(self, product_id: str) -> Optional[Product]:
        try:
            return next(
                (
                    product
                    for product in self.products
                    if product.product_id == product_id
                ),
                None,
            )
        except Exception:
            raise ProductRepositoryException(method="find")

    def edit(self, product_to_edit: Product) -> Product:
        try:
            for product in self.products:
                if product.product_id == product_to_edit.task_id:
                    self.tasks.remove(product)
                    self.tasks.append(product_to_edit)
                    return product_to_edit
            return None
        except Exception:
            raise ProductRepositoryException(method="edit")

    def delete(self, product_id: str) -> Product:
        try:
            for product in self.products:
                if product.product_id == product_id:
                    self.tasks.remove(product)
                    return product
            return None
        except Exception:
            raise ProductRepositoryException(method="delete")
