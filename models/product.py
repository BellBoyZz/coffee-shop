from sqlalchemy import Integer, Column, Text, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key=True)
    product_group = Column(Text)
    product_category = Column(Text)
    product_type = Column(Text)
    product = Column(Text)
    product_description = Column(Text)
    unit_of_measure = Column(Text)
    current_wholesale = Column(Float)
    current_retail_price = Column(Text)
    tax_exempt_yn = Column(Text)
    promo_yn = Column(Text)
    new_product_yn = Column(Text)

    def __repr__(self):
        return f"Product(product_id={self.product_id}, product_group={self.product_group}," \
               f" product_category={self.product_category}, product={self.product}, " \
               f" product_description={self.product_description}, unit_of_measure={self.unit_of_measure}," \
               f" current_retail_price={self.current_retail_price})"
