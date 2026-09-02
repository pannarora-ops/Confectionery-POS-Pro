import sqlite3

DB_NAME = "database.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def add_product(barcode, name, category, brand, unit,
                hsn, gst, purchase, sale, mrp,
                stock, min_stock):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO products(
            barcode,
            product_name,
            category,
            brand,
            unit,
            hsn_code,
            gst,
            purchase_price,
            sale_price,
            mrp,
            stock,
            min_stock
        )
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        barcode,
        name,
        category,
        brand,
        unit,
        hsn,
        gst,
        purchase,
        sale,
        mrp,
        stock,
        min_stock
    ))

    conn.commit()
    conn.close()