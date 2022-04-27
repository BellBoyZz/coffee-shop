from sqlalchemy.orm import Session
from models.sales_reciept import SalesReceipt


class SalesReceiptDao:
    """DAO for sales receipts model."""

    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_sales_receipts(self):
        """Show all sales receipts."""
        return self.__session.query(SalesReceipt).all()

    def get_sales_receipt_by_id(self, transaction_id):
        """Select sales receipt by id."""
        try:
            return self.__session.query(SalesReceipt).filter_by(transaction_id=transaction_id).first()
        except:
            return "Can not find sales receipt with id " + transaction_id

    def add_sales_receipt(self, sales_receipt: SalesReceipt):
        """Add the sales receipt."""
        self.__session.add(sales_receipt)
        self.__session.commit()
        print("Successfully added.")

    def update_sales_receipt_quantity(self, transaction_id, new_quantity):
        """Update the sales receipt which will be searched by transaction id."""
        try:
            sales_receipt = self.__session.query(SalesReceipt).filter_by(transaction_id=transaction_id).first()
            sales_receipt.quantity = new_quantity
            self.__session.commit()
            print("Update Successfully.")
        except:
            print("Can not find sales receipt with id " + transaction_id)

    def delete_sales_receipt(self, transaction_id):
        """Delete the selected sales receipt."""
        try:
            sales_receipt = self.__session.query(SalesReceipt).filter_by(transaction_id=transaction_id).first()
            self.__session.delete(sales_receipt)
            self.__session.commit()
            print("Delete Successfully.")
        except:
            print("Failed to delete, can not find the sales receipt with id " + transaction_id)
