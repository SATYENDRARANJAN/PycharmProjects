# Customer
# Parking Attendant
# Admin
# Vehicle - Car,Bike,Truck

# Parking Lot
# Entry/exit points
# Parking Floor
# Velhicle Slots  - Large ,Compact ,Small

# Payment Method
# Parking Rate
# Payment Class

# Vehicle - ParkingAttendent - slot id - intime- outime - parking rate  - ticket

# Notification Boards

# Admin
# Add /remove parking Floor
# Add remove parking slot
# Add parking attendant
# Add entrance /exit
# Add modify parkign rate

# Customer
# Take ticket
# scan ticket
# make payment using payment modes
# park vehicle at parking slot
# exit_vehicle

# Parking Attendant
# issue ticket to customer
# View Account
# Update account
# login/logout
# cash payment collection

# System
# Assign a parking slot to vehicle
# Remove a parkign slot
# Show parking full message
# Show available parking slot
from abc import ABC
from enum import Enum


class AccountStatus(Enum):
    ACTIVE ,BLOCKED, BANNED , COMPROMISED,ARCHIVED,UNKNOWN = 1,2,3,4,5


class ParkingSpotType(Enum):
    HANDICAPPED,COMPACT, BIKE,CAR, LARGE,ELECTRIC=1 ,2,3,4,5

class VehicleType(Enum):
    CAR,BIKE,TRUCK,VAN,ELECTRIC= 1,2,3,4,5

class Account:
    def __init__(self,username, password, person, status ):
        self.__username = username
        self.__password = password
        self.__person = person
        self.__status = status

    def reset_password(self):
        pass


class Admin(Account):
    def __init__(self,username, password, person,status= AccountStatus.ACTIVE):
        super().__init__(self,username, password, person,status= AccountStatus.ACTIVE)

    def add_parking_floor(self):
        None

    def add_parking_slot(self,floorname, spot):
        None

    def add_parking_display_board(self,floorname,spot):
        None

    def add_customer_info_panel(self,floorname, infopanel):
        None

    def add_entrance_panel(self,entrancepanel):
        None

    def add_exit_panel(self):
        None


class ParkingAttendant:
    def __init__(self,username,password,person,status):
        super().__init__(username,password,person,status)
    def process_ticket(self):
        None



# PARKING FLOOR - name , summary of floor spots , exit and entrance,display board
class ParkingFloor:
    def __init__(self,name ):
        self.__name = name
        self.__handicapped_spots={}
        self.__compact_spots ={}
        self.__bike_spots={}
        self.__large_spots={}
        self.__electric_spots={}
        self.__info_portals={}
        self.__display_board =ParkingDisplayBoard()

    def add_parking_slot(self,spot):
        switcher ={
            ParkingSpotType.ELECTRIC: self.__electric_spots.put(spot.get_number(),spot),
            ParkingSpotType.BIKE : self.__bike_spots.put(spot.get_number(),spot),
            ParkingSpotType.LARGE : self.__large_spots.put(spot.get_number(),spot),
            ParkingSpotType.COMPACT : self.__compact_spots.put(spot.get_number(),spot),
            ParkingSpotType.HANDICAPPED : self.__handicapped_spots.put(spot.get_number(),spot)
        }
        switcher.get(spot.get_type(),"Wrong spot type")

    def add_vehicle_to_spot(self,vehicle,spot):
        spot.assign_vehicle(vehicle)
        switcher={
            ParkingSpotType.COMPACT : self.update_display_board_for_compact(spot),
            ParkingSpotType.HANDICAPPED : self.update_display_board_for_handicapped(spot),
            ParkingSpotType.LARGE : self.update_display_board_for_large(spot),
            ParkingSpotType.BIKE : self.update_display_board_for_bike(spot),
            ParkingSpotType.ELECTRIC : self.update_display_board_for_electric(spot)
        }

    def update_display_board_for_compact(self,spot):
        if self.__display_board.get_compact_free_spot().get_number() == spot.get_number():
            for key in self.__compact_spots:
                if self.__compact_spots.get(key).is_free():
                    self.__display_board.set_compact_free_spot(spot)
        self.__display_board.show_empty_spot_number()




# Parking Display Board
class ParkingDisplayBoard:
    def __init__(self,name ):
        self.__name = name
        self.__handicapped_free_spot=None
        self.__large_free_spot =None
        self.__compact_free_spot=None
        self.__electric_free_spot=None
        self.__motorbike_free_spot=None

    def show_empty_spot_number(self):
        message =""
        if self.__handicapped_free_spot.is_free():
            message += "Free Handicapped : "  + self.__handicapped_free_spot.get_number()
        else:
            message += "Handicapped is full "

        if self.__electric_free_spot.is_free():
            message += "Free Electric Spot :" + self.__electric_free_spot.get_number()
        else:
            message += "Electric is Full"

        if self.__compact_free_spot.is_free():
            message += "Free Compact :" + self.__compact_free_spot.get_number()
        else:
            message += "ELectirc spot"

        print(message)


# Parking Spot
class ParkingSpot:
    def __init__(self,no,parking_spot_type):
        self.__no= no
        self.__type = parking_spot_type
        self.__free = True
        self.__vehicle = None

    def assign_vehicle(self):
        pass

    def remove_vehicle(self):
        pass

    def update_display_board(self):
        pass


class HandicappedSpot(ParkingSpot):
    def  __init__(self,number):
        super().__init__(number,ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):
    def __init__(self,number):
        super().__init__(number,ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self,number):
        super().__init__(number, ParkingSpotType.LARGE)

class MotorbikeSpot(ParkingSpot):
    def __init__(self,number):
        super().__init__(number, ParkingSpotType.BIKE)

class ElectricSpot(ParkingSpot):
    def __init__(self,number):
        super().__init__(number, ParkingSpotType.ELECTRIC)



# VEHICLE AND ALL ITS CLASSES
class Vehicle(ABC):
    def __init__(self,license_number, vehicle_type,ticket=None):
        self.__license_number = license_number
        self.__vehicle_type = vehicle_type
        self.__ticket = ticket

    def assign_ticket(self,ticket):
        self.__ticket= ticket


class Car(Vehicle):
    def __init__(self,license_number, ticket):
        super().__init__(self,license_number,ticket)

class Bike(Vehicle):
    def __init__(self,license_number,ticket):
        super().__init__(self,license_number,ticket)


class ParkingRate:
    def __init__(self,type , nth_hour , price):
        self.__type=type
        self.__nth_hour = nth_hour
        self.__price = price


import threading
class ParkingLot:
    instance = None
    class __OnlyOne:
        def __init__(self,name, address):
            self.__name = name
            self.__address = address
            self.parkingRate =ParkingRate()

            self.__compact_spot_count = 0
            self.__large_spot_count = 0
            self.__motorbike_spot_count = 0
            self.__electric_spot_count = 0
            self.__handicapped_spot_count =0

            self.__max_compact_count = 0
            self.__max_large_count = 0
            self.__max_motorbike_count =0
            self.__max_electric_count =0
            self.__max_handicapped_spot_count =0

            self.__entrance_panels ={}
            self.__exit_panels ={}
            self.__parking_floors ={}

            self.__active_tickets ={}
            self.__lock = threading.lock()

        def __init__(self,name,address):
            if not ParkingLot.instance:
                ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
            else:
                ParkingLot.instance.__name = name
                ParkingLot.instance.__address = address

        def __getattr__(self,name):
            return getattr(self.instance,name)

        def get_new_parking_ticket(self,vehicle):
            if self.is_full(vehicle.get_type()):
                raise Exception('Parking Full')

            self.__lock_acquire()
            ticket = ParkingTicket()
            vehicle.assign_ticket(ticket)
            ticket.save_in_db()

            #When ticket issued and saved in db
            self.increment_spot_count(vehicle.get_type())
            self.__active_tickets.put(ticket.get_ticket_number(),ticket)
            self.__lock.release()
            return ticket

            def is_full(self,type):
                if type == VehicleType.TRUCK or type ==VehicleType.Van:
                    return self.__large_spot_count >= self.__max_large_count
                if type == VehicleType.MotorBike :
                    return self.__motorbike_spot_count >= self.__max_motorbike_count
                if type == VehicleType.CAR:
                    return (self.__car_spot_count +self.__compact_spot_count) >= (self.__max_large_count +self.__max_compact_count)
                return (self.__electric_spot_count + self.__large_spot_count +self.__compact_spot_count) >= (self.__max_electric_count + self.__max_large_count +self.__max_compact_count)

            def is_full(self):
                for key in self.__parking_floors :
                    if not self.__parking_floors.get(key).is_full():
                        return False
                    return True

            def add_parking_floor(self):
                # store in db
                pass

            def add_entrance_panel(self):
                # store in db
                pass

            def add_exit_panel(self):
                # store in db
                pass


        def increment_spot_count(self,type):
            if type ==VehicleType.TRUCK or type == VehicleType.VAN:
                self.__large_spot_count +=1
            elif type  == VehicleType.BIKE :
                self.__motorbike_spot_count+=1
            elif type ==VehicleType.CAR:
                if self.__compact_spot_count >= self.__max_compact_count:
                    self.__compact_spot_count+=1
                else:
                    self.__large_spot_count +=1
            elif type == VehicleType.ELECTRIC:

                if self.__electric_spot_count < self.__max_electric_count:
                    self.__electric_spot_count +=1
                elif self.__compact_spot_count < self.__max_compact_count:
                    self.__compact_spot_count +=1
                else :
                    self.__large_spot_count +=1

        def is_full(self):
            for key in self.__parking_floors :
                if not self.__parking_floors.get(key).is_full():
                    return False
                return True



class ParkingTicket:
    def __init__(self,vid,tid , in_time, out_time ):
        self.__vehicle_id  =vid
        self.__in_time = in_time
        self.__out_time = out_time
        self.__curr_fee = 0
        self.__transaction_id = tid


