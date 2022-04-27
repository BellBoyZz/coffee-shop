from coffee_shop import CoffeeShop
from models.product import Product

coffee_shop_db = CoffeeShop.get_instance()


product_dao = coffee_shop_db.get_product_dao()
sales_receipt_dao = coffee_shop_db.get_sales_receipts_dao()
product = Product(product_id=999, product_group="h", product_category="g", product_type="d", product="s"
                  , product_description="a", unit_of_measure="n", current_wholesale=12.2, current_retail_price="r"
                  , tax_exempt_yn="v", promo_yn="b", new_product_yn="y")
# product_dao.add_product(product)

# product_dao.update_product_name(1, "Brazilian - Organic")
print(product_dao.get_product_by_id(1))
print(sales_receipt_dao.get_sales_receipt_by_id(11).product_id)

coffee_shop_db.close_db()

