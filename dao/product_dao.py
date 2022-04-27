from sqlalchemy.orm import Session
from models.product import Product


class ProductDao:
    """DAO for product model."""

    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all_products(self):
        """Show all products."""
        return self.__session.query(Product).all()

    def get_product_by_id(self, product_id):
        """Select product by id."""
        try:
            return self.__session.query(Product).filter_by(product_id=product_id).first()
        except:
            return "Can not find the product with id " + product_id

    def add_product(self, product: Product):
        """Add the product."""
        self.__session.add(product)
        self.__session.commit()
        print("Successfully added.")

    def update_product_name(self, product_id, new_product_name: str):
        """Update the product which will be searched by transaction id."""
        try:
            product = self.__session.query(Product).filter_by(product_id=product_id).first()
            product.product = new_product_name
            self.__session.commit()
            print("Update Successfully.")
        except:
            print("Can not find sales receipt with id " + product_id)

    def delete_product(self, product_id):
        """Delete the selected product."""
        try:
            product = self.__session.query(Product).filter_by(product_id=product_id).first()
            self.__session.delete(product)
            self.__session.commit()
            print("Delete Successfully.")
        except:
            print("Failed to delete, can not find the sales receipt with id " + product_id)
