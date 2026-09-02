"""
Confectionery POS Pro
Dashboard Module
Part A
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from database import Database


class Dashboard:

    def __init__(self, root):

        self.root = root
        self.db = Database()

        # ---------------- Window ----------------

        self.root.title("Confectionery POS Pro")
        self.root.state("zoomed")
        self.root.minsize(1200, 700)

        # ---------------- Menu ----------------

        self.create_menu()

        # ---------------- Main Container ----------------

        self.container = ttk.Frame(self.root)
        self.container.pack(fill=BOTH, expand=True)

        # ==========================================
        # Sidebar
        # ==========================================

        self.sidebar = ttk.Frame(
            self.container,
            bootstyle="dark",
            width=220
        )

        self.sidebar.pack(
            side=LEFT,
            fill=Y
        )

        self.sidebar.pack_propagate(False)

        ttk.Label(
            self.sidebar,
            text="🍬 POS PRO",
            font=("Segoe UI", 18, "bold"),
            bootstyle="inverse-dark"
        ).pack(
            pady=(25, 35)
        )
                ttk.Button(
            self.sidebar,
            text="🏠 Dashboard",
            bootstyle="secondary",
            width=22
        ).pack(pady=5)

        ttk.Button(
            self.sidebar,
            text="📦 Products",
            bootstyle="secondary",
            width=22,
            command=self.open_products
        ).pack(pady=5)

        ttk.Button(
            self.sidebar,
            text="🧾 Billing",
            bootstyle="secondary",
            width=22,
            command=self.open_billing
        ).pack(pady=5)

        ttk.Button(
            self.sidebar,
            text="👥 Customers",
            bootstyle="secondary",
            width=22,
            command=self.open_customers
        ).pack(pady=5)

        ttk.Button(
            self.sidebar,
            text="🚚 Suppliers",
            bootstyle="secondary",
            width=22,
            command=self.open_suppliers
        ).pack(pady=5)

        ttk.Button(
            self.sidebar,
            text="📊 Reports",
            bootstyle="secondary",
            width=22,
            command=self.open_reports
        ).pack(pady=5)

        # ==========================================
        # Main Area
        # ==========================================

        self.main = ttk.Frame(self.container)

        self.main.pack(
            side=LEFT,
            fill=BOTH,
            expand=True
        )

        # ==========================================
        # Header
        # ==========================================

        self.header = ttk.Frame(
            self.main,
            bootstyle="primary"
        )

        self.header.pack(fill=X)

        ttk.Label(
            self.header,
            text="Confectionery POS Pro",
            font=("Segoe UI", 22, "bold"),
            foreground="white"
        ).pack(
            side=LEFT,
            padx=20,
            pady=15
        )

        self.page_title = ttk.Label(
            self.header,
            text="Dashboard",
            font=("Segoe UI", 14),
            foreground="white"
        )

        self.page_title.pack(
            side=RIGHT,
            padx=20
        )

        # ==========================================
        # Content Area
        # ==========================================

        self.content = ttk.Frame(
            self.main,
            padding=20
        )

        self.content.pack(
            fill=BOTH,
            expand=True
        )

        ttk.Label(
            self.content,
            text="Welcome Admin",
            font=("Segoe UI", 24, "bold")
        ).pack(
            anchor="w",
            pady=(10, 20)
        )
                # ==========================================
        # Dashboard Cards
        # ==========================================

        self.cards = ttk.Frame(self.content)
        self.cards.pack(fill=X, pady=10)

        def create_card(parent, title, value, style):

            card = ttk.Labelframe(
                parent,
                text=title,
                padding=20,
                bootstyle=style
            )

            card.pack(
                side=LEFT,
                fill=BOTH,
                expand=True,
                padx=8
            )

            value_lbl = ttk.Label(
                card,
                text=value,
                font=("Segoe UI", 28, "bold")
            )

            value_lbl.pack()

            return value_lbl

        self.lbl_products = create_card(
            self.cards,
            "Products",
            "0",
            "success"
        )

        self.lbl_customers = create_card(
            self.cards,
            "Customers",
            "0",
            "info"
        )

        self.lbl_users = create_card(
            self.cards,
            "Users",
            "1",
            "warning"
        )

        self.lbl_sales = create_card(
            self.cards,
            "Today's Sales",
            "₹0",
            "danger"
        )

        # ==========================================
        # Quick Actions Title
        # ==========================================

        ttk.Separator(self.content).pack(
            fill=X,
            pady=25
        )

        ttk.Label(
            self.content,
            text="Quick Actions",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w")
            # ==========================================
    # Menu Bar
    # ==========================================

    def create_menu(self):

        menubar = tk.Menu(self.root)

        file_menu = tk.Menu(
            menubar,
            tearoff=0
        )

        file_menu.add_command(label="Dashboard")
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            command=self.root.destroy
        )

        menubar.add_cascade(
            label="File",
            menu=file_menu
        )

        self.root.config(menu=menubar)
                # ==========================================
        # Quick Action Buttons
        # ==========================================

        self.quick = ttk.Frame(self.content)

        self.quick.pack(
            fill=X,
            pady=20
        )

        ttk.Button(
            self.quick,
            text="📦 Products",
            width=20,
            bootstyle="success",
            command=self.open_products
        ).grid(row=0, column=0, padx=10, pady=10)

        ttk.Button(
            self.quick,
            text="🧾 Billing",
            width=20,
            bootstyle="primary",
            command=self.open_billing
        ).grid(row=0, column=1, padx=10, pady=10)

        ttk.Button(
            self.quick,
            text="👥 Customers",
            width=20,
            bootstyle="info",
            command=self.open_customers
        ).grid(row=0, column=2, padx=10, pady=10)

        ttk.Button(
            self.quick,
            text="🚚 Suppliers",
            width=20,
            bootstyle="warning",
            command=self.open_suppliers
        ).grid(row=1, column=0, padx=10, pady=10)

        ttk.Button(
            self.quick,
            text="📊 Reports",
            width=20,
            bootstyle="secondary",
            command=self.open_reports
        ).grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(
            self.quick,
            text="⚙ Settings",
            width=20,
            bootstyle="dark",
            command=self.open_settings
        ).grid(row=1, column=2, padx=10, pady=10)

        ttk.Button(
            self.quick,
            text="🚪 Logout",
            width=20,
            bootstyle="danger",
            command=self.logout
        ).grid(
            row=2,
            column=1,
            pady=20
        )
            # ==========================================
    # Dashboard Refresh
    # ==========================================

    def refresh_dashboard(self):

        try:
            total_products = self.db.get_total_products()
            self.lbl_products.config(text=str(total_products))
        except:
            self.lbl_products.config(text="0")

    # ==========================================
    # Navigation Methods
    # ==========================================

    def open_products(self):
        messagebox.showinfo(
            "Products",
            "Products Module (Milestone 4)"
        )

    def open_billing(self):
        messagebox.showinfo(
            "Billing",
            "Billing Module (Coming Soon)"
        )

    def open_customers(self):
        messagebox.showinfo(
            "Customers",
            "Customers Module (Coming Soon)"
        )

    def open_suppliers(self):
        messagebox.showinfo(
            "Suppliers",
            "Suppliers Module (Coming Soon)"
        )

    def open_reports(self):
        messagebox.showinfo(
            "Reports",
            "Reports Module (Coming Soon)"
        )

    def open_settings(self):
        messagebox.showinfo(
            "Settings",
            "Settings Module (Coming Soon)"
        )

    # ==========================================
    # Logout
    # ==========================================

    def logout(self):

        if messagebox.askyesno(
            "Logout",
            "Do you want to logout?"
        ):
            self.root.destroy()

    # ==========================================
    # Clock
    # ==========================================

    def update_clock(self):

        current = datetime.now().strftime(
            "%d-%m-%Y   %I:%M:%S %p"
        )

        self.status_label.config(
            text=current
        )

        self.root.after(
            1000,
            self.update_clock
        )
                # ==========================================
        # Status Bar
        # ==========================================

        ttk.Separator(
            self.main,
            bootstyle="secondary"
        ).pack(fill=X)

        self.status = ttk.Frame(
            self.main
        )

        self.status.pack(
            fill=X,
            side=BOTTOM
        )

        self.status_label = ttk.Label(
            self.status,
            text=""
        )

        self.status_label.pack(
            side=LEFT,
            padx=15,
            pady=8
        )

        ttk.Label(
            self.status,
            text="User : Admin"
        ).pack(
            side=RIGHT,
            padx=15
        )

        self.refresh_dashboard()

        self.update_clock()