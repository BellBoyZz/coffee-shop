from sqlalchemy import Integer, Column, Text, Float, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class SalesReceipt(Base):
    __tablename__ = "sales_receipts"

    transaction_id = Column(Integer, primary_key=True)
    transaction_date = Column(Text)
    transaction_time = Column(Text)
    sales_outlet_id = Column(Integer)
    staff_id = Column(Integer)
    customer_id = Column(Integer)
    instore_yn = Column(Text)
    order_name = Column(Integer)
    line_item_id = Column(Integer)
    product_id = Column(Integer, ForeignKey("products.product_id"))
    quantity = Column(Integer)
    line_item_amount = Column(Float)
    unit_price = Column(Float)
    promo_item_yn = Column(Text)

    def __repr__(self):
        return f"Receipt(transaction_id={self.transaction_id}, transaction_date={self.transaction_date}," \
               f" transaction_time={self.transaction_time}, product_id={self.product_id}, quantity={self.quantity})"
