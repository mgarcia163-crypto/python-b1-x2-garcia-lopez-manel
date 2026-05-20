# Write your imports here
from collections import Counter
from enum import Enum
from bills.bill import Bill 
from bills.item import Product
from bills.entity import Seller, Buyer



class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        # Write here your code
        product_counts = Counter()
        for bill in bills:
            for product in bill.products:
                product_counts[product] += 1
        if not product_counts:
            return (None, 0)
        top_product, frequency = product_counts.most_common(1)[0]
        return (top_product, frequency)

    def find_top_two_sellers(self) -> list:
        # Write here your code
        seller_sales = {}
        for bill in bills:
            seller = bill.seller
            bill_total = bill.calculate_total()
            if seller in seller_sales:
                seller_sales[seller] += bill_total
            else:
                seller_sales[seller] = bill_total
        sorted_sellers = sorted(seller_sales, key=seller_sales.get, reverse=True)
        return sorted_sellers[:2]
        

    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        # Write here your code
        if not bills:
            return (None, 0.0)
        buyer_purchases = {}
        for bill in bills:
            buyer = bill.buyer
            bill_total = bill.calculate_total()
            if buyer in buyer_purchases:
                buyer_purchases[buyer] += bill_total
            else:
                buyer_purchases[buyer] = bill_total
        lowest_buyer = min(buyer_purchases, key=buyer_purchases.get)
        lowest_total = buyer_purchases[lowest_buyer]
        return (lowest_buyer, float(lowest_total))
    

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        product_taxes = {}
        for bill in bills:
            for product in bill.products:
                tax_amount = product.calculate_total_taxes()
                if product in product_taxes:
                    product_taxes[product] += tax_amount
                else:
                    product_taxes[product] = tax_amount
        is_reverse = (order_type.name == "DESC")
        sorted_products = sorted(
        product_taxes.items(), 
        key=lambda item: item[1], 
        reverse=is_reverse)
        return sorted_products


    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
