# coffee-shop

This program will allow the user to easily manage their coffee shop.

#### Setup
Using SQlite and the `sqlite3` command line utility:

    # create "sample.db" using schema commands in a file sqlite3 sample.db < coffee-shop.schema

    # start the sqlite command line utility (or use a GUI tool)
    # import required data from a CSV file.

    sqlite> .mode csv
    sqlite> .import data/sales_reciepts.csv sales_receipts
    sqlite> .import data/product.csv products

#### UML Class Diagram
[UML](../../wiki/uml-class-diagram)

#### Package Diagram
[Package Diagram](../../wiki/package-diagram)

#### Web Service API
[Web Service API](../../wiki/web-service-API)
