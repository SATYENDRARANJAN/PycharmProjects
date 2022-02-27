# Amazon online shopping system .
#

# guest  - register
#       - search prods
#       - add to cart
# customer - search
#          - add to cart
#          - make payment
#          - add shipping address
#          - login / logout
#          - cancel membership
#          - update account
#          - checkout shopping cart
#          - add product review
# admin - add/remove category
#       - add products
#       - blacklist /block customer
# System - send notifiations
#        - shipping updates
import datetime
from enum import Enum
from abc import ABC

class Address:
    def __init__(self,street , city , state , zipcode , country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__country = country

class OrderStatus (Enum):
    UNSHIPPED,PENDING , SHIPPED , COMPLETED , CANCELLED , REFUND_APPLIED = 1,2,3,4,5

class AccountStatus(Enum):
    ACTIVE , BLOCKED , BANNED , COMPROMISE, ARCHIVED, UNKNOWN = 1,2,3,4,5,6

class ShipmentStatus(Enum) :
    PENDING,SHIPPED,DELIVERED,ONHOLD =1,2,3,4

class PaymentStatus(Enum):
    UNPAID,PENDING,PAID,CANCELLED_BY_CUSTOMER,ABANDONED,DECLINED_BY_BANK,SETTLING,SETTLED,REFUNDED=1,2,3,4,5,6,7,8,9


class Account :
    def __init__(self,username, password, email , phone , shipping_address,status =AccountStatus):
        self.__username = username
        self.__password = password
        self.__email = email
        self.__phone = phone
        self.__shipping_address = shipping_address
        self.__status= status

    def add_product(self,product):
        None

    def add_product_review(self,product):
        None

    def reset_password(self):
        None


class Customer(ABC):
    def __init__(self,cart ,order):
        self.__cart = cart
        self.__order = order

    def get_shopping_cart(self):
        return self.__cart

    def search_shopping_cart(self):
        None

    def add_item_to_shopping_cart(self,item):
        None

    def remove_item_from_shopping_cart(self,item):
        None


def Guest(Customer):
    def register_account(self):
        None


def Member(Customer):
    def __init__(self,account):
        self.__account = account

    def place_order(self,order):
        None


class ProductCategory :
    def __init__(self,name,description):
        self.__name = name
        self.__description = description


class ProductReview:
    def __init__(self, rating , review,reviewer):
        self.__rating = rating
        self.__review = review
        self.__reviewer = reviewer


class Product :
    def __init__(self, id , name , description , price , category  , seller_account  ):
        self.__product_id  =id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__category = category
        self.__seller_account = seller_account
        self.__count = 0

    def get_available_count(self):
        return self.__count

    def get_price(self):
        return self.__price


class Item:
    def __init__(self,product_id , sku , model , brand ,count , color, size):
        self.product_id = product_id
        self.__sku = sku
        self.__model = model
        self.__brand  = brand
        self.__color = color
        self.__size = size
        self.__count = count

    def get_count(self):
        return  self.__count


class ShoppingCart:
    def __init__(self):
        self.__items =[]

    def add_item(self):
        None

    def remove_item(self):
        None

    def update_item_quantity(self):
        None

    def get_items(self):
        None

    def checkout(self):
        None


class OrderLog :
    def __init__(self,order_number, status = OrderStatus.PENDING):
        self.__order = order_number
        self.__creation_date = datetime.date.today()
        self.__status = status


class Order :
    def __init__(self,order_number , status = OrderStatus.PENDING ):
        self.__order_number = 0
        self.__status = status
        self.__order_date =datetime.date.today()
        self.__order_log = []

    def send_for_shipment(self):
        None

    def make_payment(self,payment):
        None

    def add_order_log(self,order_log):
        None


class ShipmentLog(ABC):
    def __init__(self,order_id,status,shipment_number,shipment_method , estimated_arrival_date):
        self.__order_id = order_id
        self.__shipment_number = shipment_number
        self.__shipment_date = datetime.date.today()
        self.__shipment_method = shipment_method
        self.__estimated_arrival = estimated_arrival_date
        self.__status = status #missing in doc
        self.__creation_date = datetime.datetime.today()
        self.__shipment_logs  = []

    def add_shipment_log(self,shipment_log):
        None


class Notification(ABC):
    def __init__(self,id , content):
        self.__notification_id = id
        self.__content = content
        self.__created_on = datetime.datetime.today()

    def send_notification(self):
        None


# Search Interface and Catalog
class Search(ABC) :
    def search__by_name(self,name):
        None

    def search_by_color(self,color):
        None

    def search_by_category(self,category):
        None


class Catalog(Search):
    def __init__(self):
        self.__product_names=[]
        self.__product_categories =[]

    def search_products_by_names(self,name):
        return self.__product_names.get(name)

    def search_products_by_categories(self,category):
        return self.__product_categories.get(category)



