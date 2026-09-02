import sqlite3

from app.database import DB_FILE


class ProductModel:

    def __init__(self):
        self.conn = sqlite3.connect(DB_FILE)
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    # ----------------------------------
    # Add Product
    # ----------------------------------

    def add_product(
        self,
        barcode,
        product_name,
        category,
        brand,
        unit,
        hsn,
        gst,
        purchase_price,
        selling_price,
        mrp,
        stock,
        minimum_stock,
    ):

        self.cursor.execute(
            """
            INSERT INTO products(

                barcode,
                product_name,
                category,
                brand,
                unit,
                hsn,
                gst,
                purchase_price,
                selling_price,
                mrp,
                stock,
                minimum_stock

            )

            VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                barcode,
                product_name,
                category,
                brand,
                unit,
                hsn,
                gst,
                purchase_price,
                selling_price,
                mrp,
                stock,
                minimum_stock,
            ),
        )

        self.conn.commit()

    # ----------------------------------
    # Get All Products
    # ----------------------------------

    def get_all_products(self):

        self.cursor.execute(
            """
            SELECT
                id,
                barcode,
                product_name,
                category,
                brand,
                stock,
                selling_price
            FROM products
            ORDER BY product_name
            """
        )

        return self.cursor.fetchall()

    # ----------------------------------
    # Search Products
    # ----------------------------------

    def search_products(self, keyword):

        self.cursor.execute(
            """
            SELECT
                id,
                barcode,
                product_name,
                category,
                brand,
                stock,
                selling_price
            FROM products

            WHERE

                barcode LIKE ?
                OR product_name LIKE ?
                OR category LIKE ?
                OR brand LIKE ?

            ORDER BY product_name
            """,
            (
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
                "%" + keyword + "%",
            ),
        )

        return self.cursor.fetchall()

    # ----------------------------------
    # Get Product By ID
    # ----------------------------------

    def get_product(self, product_id):

        self.cursor.execute(
            """
            SELECT *
            FROM products
            WHERE id=?
            """,
            (product_id,),
        )

        return self.cursor.fetchone()

    # ----------------------------------
    # Update Product
    # ----------------------------------

    def update_product(
        self,
        product_id,
        barcode,
        product_name,
        category,
        brand,
        unit,
        hsn,
        gst,
        purchase_price,
        selling_price,
        mrp,
        stock,
        minimum_stock,
    ):

        self.cursor.execute(
            """
            UPDATE products

            SET

                barcode=?,
                product_name=?,
                category=?,
                brand=?,
                unit=?,
                hsn=?,
                gst=?,
                purchase_price=?,
                selling_price=?,
                mrp=?,
                stock=?,
                minimum_stock=?,
                updated_at=CURRENT_TIMESTAMP

            WHERE id=?
            """,
            (
                barcode,
                product_name,
                category,
                brand,
                unit,
                hsn,
                gst,
                purchase_price,
                selling_price,
                mrp,
                stock,
                minimum_stock,
                product_id,
            ),
        )

        self.conn.commit()

    # ----------------------------------
    # Delete Product
    # ----------------------------------

    def delete_product(self, product_id):

        self.cursor.execute(
            """
            DELETE FROM products
            WHERE id=?
            """,
            (product_id,),
        )

        self.conn.commit()

    # ----------------------------------
    # Close
    # ----------------------------------

    def close(self):
        self.conn.close()