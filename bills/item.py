from enum import Enum
import datetime
from .entity import *

# Do not change the value of ISD_FACTOR var
ISD_FACTOR = 0.25


class TaxType(Enum):
    # Do not change this enum
    IVA = 1
    ISD = 2


class Tax:
    # Write the parameters in the next line
    def __init__(self, tax_id: str, tax_type: TaxType, percentage: float):
        # Write here your code
        self.tax_id = tax_id
        self.tax_type = tax_type
        self.percentage = percentage
        pass


class Product:
     # Write the parameters in the next line
    def __init__(self, product_id: str, name: str, expiration_date: datetime, bar_code: str, quantity: int, price: float, taxes: list['Tax']):
        # Write here your code
        self.product_id = product_id
        self.name = name
        self.expiration_date = expiration_date
        self.bar_code = bar_code
        self.quantity = quantity
        self.price = price
        self.taxes = taxes
        pass        

    def calculate_tax(self, tax: Tax) -> float:
        # Write here your code
        ISD_FACTOR = 0.25
        tax_found = None
        for t in self.taxes:
            if t.tax_type == tax.tax_type:
                tax_found = t
                break
        if not tax_found:
            return 0.0
        

    def calculate_total_taxes(self) -> float:
        # Write here your code
        total_acumulado = 0.0
        for tax in self.taxes:
            valor_impuesto = self.calculate_tax(tax)
            total_acumulado += valor_impuesto
        return float(total_acumulado)
    

    def calculate_total(self) -> float:
        # Write here your code
        subtotal = self.price * self.quantity
        total = subtotal + self.calculate_total_taxes(subtotal)
        return float(total)

    def __eq__(self, another):
        # Do not change this method
        return hasattr(another, 'product_id') and self.product_id == another.product_id

    def __hash__(self):
        # Do not change this method
        return hash(self.product_id)

    def print(self):
        # Do not change this method
        print(
            f"Product Id:{self.product_id} , name:{self.name}, quantity:{self.quantity}, price:{self.price}")
        for tax in self.taxes:
            print(f"Tax:{tax.tax_type} , percentage:{tax.percentage}")


class Bill:
    def __init__(self, bill_id: str, sale_date: datetime, seller: Seller, buyer: Buyer, products: list[Product]):
        # Write here your code
        self.bill_id: str = bill_id
        self.sale_date: datetime = sale_date
        self.seller: 'Seller' = seller
        self.buyer: 'Buyer' = buyer
        self.products: list['Product'] = products
        pass
        
       

    def calculate_total(self) -> float:
        # Write here your code
        total_factura = 0.0
        for producto in self.products:
            total_factura += producto.calculate_total()
        return float(total_factura)

    def print(self):
        # Do not change this method
        self.buyer.print()
        self.seller.print()
        for product in self.products:
            product.print()