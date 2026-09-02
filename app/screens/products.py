from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from app.models.product_model import ProductModel


class ProductsScreen(MDScreen):

    # ---------------------------------
    # Screen Open
    # ---------------------------------

    def on_pre_enter(self, *args):
        self.update_layout()
        self.build_table()
        self.load_products()
        
    # ---------------------------------
    # Window Resize
    # ---------------------------------

    def on_resize(self, *args):
        self.update_layout()

    # ---------------------------------
    # Responsive Layout
    # ---------------------------------

    def update_layout(self):

        if Window.width < 900:
            self.ids.form_grid.cols = 1
        else:
            self.ids.form_grid.cols = 2
    def build_table(self):

        self.data_tables = MDDataTable(

            size_hint=(1, 1),

            use_pagination=True,

            rows_num=10,

            check=False,

            column_data=[

                ("ID", dp(20)),
                ("Barcode", dp(35)),
                ("Product", dp(45)),
                ("Category", dp(35)),
                ("Stock", dp(25)),
                ("Price", dp(25)),

            ],

            row_data=[],
        )

        self.ids.table_box.clear_widgets()

        self.ids.table_box.add_widget(self.data_tables)
    # ---------------------------------
    # Save Product
    # ---------------------------------

    def save_product(self):

        print("SAVE BUTTON CLICKED")

        db = ProductModel()

        db.add_product(
            self.ids.barcode.text.strip(),
            self.ids.pname.text.strip(),
            self.ids.category.text.strip(),
            self.ids.brand.text.strip(),
            self.ids.unit.text.strip(),
            self.ids.hsn.text.strip(),
            float(self.ids.gst.text or 0),
            float(self.ids.purchase.text or 0),
            float(self.ids.sale.text or 0),
            float(self.ids.mrp.text or 0),
            float(self.ids.stock.text or 0),
            float(self.ids.minstock.text or 0),
        )

        db.close()

        print("PRODUCT SAVED SUCCESSFULLY")

        self.clear_fields()
        self.load_products()

    # ---------------------------------
    # Load Products
    # ---------------------------------

    def load_products(self):

        db = ProductModel()

        products = db.get_all_products()

        db.close()

        rows = []

        for p in products:

            rows.append(

                (

                    str(p["id"]),

                    p["barcode"],

                    p["product_name"],

                    p["category"],

                    str(p["stock"]),

                    str(p["selling_price"]),

                )

            )

        self.data_tables.row_data = rows
    # ---------------------------------
    # Search Product
    # ---------------------------------

    def search_product(self, keyword):

        self.ids.product_list.clear_widgets()

        db = ProductModel()

        products = db.search_products(keyword)

        db.close()

        for product in products:

            text = (
                f"{product['barcode']}   |   "
                f"{product['product_name']}   |   "
                f"Stock : {product['stock']}   |   "
                f"₹ {product['selling_price']}"
            )

            self.ids.product_list.add_widget(
                OneLineListItem(text=text)
            )

    # ---------------------------------
    # Clear Form
    # ---------------------------------

    def clear_fields(self):

        self.ids.barcode.text = ""
        self.ids.pname.text = ""
        self.ids.category.text = ""
        self.ids.brand.text = ""
        self.ids.unit.text = ""
        self.ids.hsn.text = ""
        self.ids.gst.text = ""
        self.ids.purchase.text = ""
        self.ids.sale.text = ""
        self.ids.mrp.text = ""
        self.ids.stock.text = ""
        self.ids.minstock.text = ""