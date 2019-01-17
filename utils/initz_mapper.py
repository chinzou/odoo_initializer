

def get_product_header(header=""):
    return header.replace(
        "Fully specified name:en", "name"
    ).replace(
        "odoo_price", "lst_price"
    ).split(",") if header is not "" else ["name", "lst_price"]
