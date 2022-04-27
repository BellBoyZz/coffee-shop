from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dao.sales_receipt_dao import SalesReceiptDao
from dao.product_dao import ProductDao


class CoffeeShop:

    sales_receipts_dao = None
    product_dao = None
    __instance = None

    @staticmethod
    def get_instance():
        """Static access method."""
        if CoffeeShop.__instance is None:
            CoffeeShop.__instance = CoffeeShop()
        return CoffeeShop.__instance

    def __init__(self, connection_url="sqlite:///sample.db"):
        engine = create_engine(connection_url)
        Session = sessionmaker(bind=engine)
        self.__db_session = Session()

    def get_sales_receipts_dao(self):
        """Get sales receipts dao."""
        if self.sales_receipts_dao is None:
            self.sales_receipts_dao = SalesReceiptDao(session=self.__db_session)
        return self.sales_receipts_dao

    def get_product_dao(self):
        """Get product dao."""
        if self.product_dao is None:
            self.product_dao = ProductDao(session=self.__db_session)
        return self.product_dao

    def close_db(self):
        """Close the database."""
        self.__db_session.close()
