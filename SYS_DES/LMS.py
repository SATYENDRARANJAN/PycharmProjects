import datetime
from abc import ABC
from enum import Enum


class BookFormat(Enum):
    HARDCOVER,PAPERBACK,JOURNAL=1,2,3

class BookStatus(Enum):
    AVAILABLE,RESERVED,LOANED,LOST = 1, 2, 3, 4

class ReservationStatus(Enum):
    WAITING,PENDING,COMPLETED,CANCELLED,NONE=1,2,3,4,5

class AccountStatus(Enum):
    ACTIVE,CLOSED,CANCELLED,BLACKLISTED,NONE =1,2,3,4,5


class Person(ABC):
    def __init__(self,name,address,email,phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone

class Address:
    def __init__(self,street,city,state,zipcode,country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        self.__country = country

class Constants:
    MAX_BOOKS_ISSUED_TO_A_USER = 5
    MAX_LENDING_DAYS = 10

# USER (ACCOUNT) , MEMBER AND LIBRARIAN -- various people that interact with our system
from abc import ABC,abstractmethod

class User(ABC):
    def __init__(self,id , password, person, status=AccountStatus.ACTIVE):
        # id , password, status , person
        self.__id = id
        self.__password = password
        self.__status = status
        self.__person = person

    def resetPassword(self):
        pass


class Librarian(User):
    def __init__(self,id,password, person,status=AccountStatus.ACTIVE):
        super().__init__(id,password,person,status)

    def add_book_item(self):
        #if boooks already present -- add bookitem
        # if books not present -- add book and bookitem
        pass

    def block_member(self,member):
        pass

    def unblock_member(self,member):
        pass

    #added extra
    def issue_card_member(self,member):
        pass


class Member(User):
    def __init__(self,id ,password, person, status= AccountStatus.ACTIVE):
        super().__init__(self,id,password,person,status)
        self.__joining_date=datetime.date.today()
        self.__total_books_checkedout = 0

    def get_total_books_checkedout(self):
        return  self.__total_books_checkedout

    def reserve_book_item(self,book_item):
        pass

    def renew_book_item(self,book_item):
        # get reservation status of bookitem -
        # - if found : CANT RENEW - decrement member's book checkout count - and update book_item.state = BookStatus.RESERVED
        # and send book available notification
        self.check_for_fine(book_item.get_barcode())
        book_reservation = BookReservation.get_reservation_details(book_item.get_barcode())
        if book_reservation != None and book_reservation.get_member_id() != self.get_member_id():
            # Reservation already done by someone else
            print("self book is reserved by another member")
            self.decrement_total_book_checkout()
            book_item.update_book_item_state(BookStatus.RESERVED)
            book_reservation.send_book_available_notification()
            return False
        elif book_reservation != None:
            # pending reservation from self member
            book_reservation.update_status(ReservationStatus.COMPLETED)
        BookLending.lendbook(book_item.get_barcode(), self.get_member_id())
        book_item.update_due_date(datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
        return True

    def return_book_item(self,book_item_id ):
        pass

    def checkout_book_item(self,book_item):
        if self.get_total_books_checkedout()==Constants.MAX_BOOKS_ISSUED_TO_A_USER:
            print("ISSUE LIMIT CROSSED")
            return False

        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
        if book_reservation != None  and book_reservation.get_member_id() !=self.get_id():
            # BOOK ITEM has a pending reservation from another user
            print("Self book is reserved by another member")
            return False
        elif book_reservation != None:
            # Book item has a pending reservation from another member , update it
            book_reservation.update_status(ReservationStatus.COMPLETED)

        if not book_item.checkout(self.get_id()):
            #Book not issued
            return False
        #Book issued
        self.increment_total_books_checked_out()
        return True

    def get_fine(self):
        pass


## BOOK RESERVATION ,BOOK LENDING,FINE

class BookReservation:
    def __init__(self,creation_date ,status,book_item_barcode,member_id):
        self.__creation_date= creation_date
        self.__status=  status
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id


class BookLending:
    def __init__(self,created_date,due_date,return_date,book_item_barcode,member_id):
        self.__created_date = created_date
        self.__due_date = due_date
        self.__return_date = return_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def lend_book(self,barcode,member_id):
        pass

    def fetch_lending_details(self):
        pass


class Fine:
    def __init__(self,creation_date, book_item_barcode, member_id):
        self.__creation_date = creation_date
        self.__book_item_barcode = book_item_barcode
        self.__member_id = member_id

    def collect_fine(self,book_item_barcode):
        pass


## BOOK - Encapsulating a book item, this would be responsible for reservation, renewal and return of book item
from abc import ABC,abstractmethod
class Book(ABC):
    def __init__(self,ISBN,title,publisher,pages,format,authors):
        self.__ISBN = ISBN
        self.__title = title
        self.__publisher= publisher
        self.__authors = authors


# BookItem : Responsible for reservation, return and renewal of book item
class BookItem(Book):
    def __init__(self,barcode,is_reference_only , borrowed,due_date, price ,format,status,date_of_purchase,publication,placed_at):
        self.__barcode = barcode
        self.__is_reference_only = is_reference_only
        self.__borrowed = borrowed
        self.__due_date = due_date
        self.__price = price
        self.__format = format
        self.__status = status
        self.__date_of_purchase = date_of_purchase
        self.__publication = publication
        self.__placed_at = placed_at


    def checkout(self,member_id):
        # create reservation and BookLending
        if self.get_is_reference_only():
            return False
        if BookLending.lend_book(self.get_bar_code(),member_id):
            return False
        self.update_book_item_status(BookStatus.LOANED)
        return True


class Rack:
    def __init__(self,number,location_identifier):
        self.__number = number
        self.__location_identifier = location_identifier


## SEARCH INTERFACE AND CATALOG - THE CATALOG WILL IMPLEMENT SEARCH INTERFACE TO FACILITATE SEARCHING OF THE BOOKS
from abc import ABC , abstractmethod

class Search(ABC):
    def search_by_title(self,title):
        pass

    def search_by_author(self,author):
        pass

    def search_by_subject(self,subject):
        pass

    def search_by_pub_date(self,pub_date):
        pass



class Catalog(Search):
    def __init__(self):
        self.book_titles ={}
        self.book_authors ={}
        self.book_subjects ={}
        self.book_publication_dates ={}


    def search_by_title(self,query):
        return self.__book_titles.get(query)

    def search_by_author(self,query):
        return self.__book_authors.get(query)


