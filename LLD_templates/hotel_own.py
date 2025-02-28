'''
Requirements: 

1) Users should be able to reserve multiple rooms in 1 reservation, and should be able to make multiple reservations
2) There are different room sizes available - like single, double, apex, suite etc.
3) Users should be able to search for available rooms between a range of dates. 
4) Users must be able to modify/cancel their resrvations
5) Hotel Admin should be able to see all the reservations for a specific user. 
6) Hotel Admin should be able to see all checked in guests, and their expected checkout dates. 
7) Users should be able to check in and check out
8) Each reservation should have a price calculation, which depends on the no. of rooms, room types/sizes, price per night etc. 


Classes, Methods and Attributes:

1) Room 
Attributes: room_id, price_per_night, is_booked, room_type
Methods: 
2) User:
Attributes: user_id, user_name, reservations: List[Reservation]
Methods: add_reservation
3) Reservation
Attributes: reservation_id, from_date, to_date, user_id, rooms, is_checked_in, is_cancelled (status)
Methods: calculate_price, check_in, check_out, cancel_reservation, modify_reservation
4) Hotel
Attributes: rooms: List[Room], name, reservations: List[Reservation]
Methods: add_room, check_availability, create_reservation, modify_reservation, cancel_reservation, get_user_reservations, get_checked_in_users
5) HotelAdmin
Attributes: hotel, admin_id
Methods: get_user_reservations, get_checked_in_users
'''
from enum import Enum

class RoomType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"

class Room:
    def __init__(self, room_id, room_type, price_per_night):
        self.room_id = room_id
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_booked = False
    
class User: 
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.reservations = []
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)
    
class Reservation:
    def __init__(self, reservation_id, from_date, to_date, user, rooms):
        #Assume they exist
        self.is_checked_in = False
        self.is_cancelled = False

    def check_in(self):
        if self.is_cancelled == True:
            raise Error
        else:
            is_checked_in = True

    def check_out(self):
        if self.is_checked_in == False:
            raise Error
        else:
            is_checked_in = False
    
    def calculate_price():
        total_price = 0
        num_of_days = (to_date - from_date).date
        for room in rooms:
            total_price+=(num_of_days*room.price_per_night())
        return total_price

    def modify_reservation(self, new_from_date, new_end_date):
        if self.checked_in == False and self.is_cancelled == False:
            self.from_date = new_from_date
            self.to_date = new_to_date
        else:
            raise Error("Can't modify a cancelled/checked in reservation")
    
    def cancel_reservation(self):
        if self.is_checked_in == False:
            self.is_cancelled = True
        else:
            raise Error("Can't cancel a checked in reservation")

# Methods: add_room, check_availability, create_reservation, modify_reservation, cancel_reservation, get_user_reservations, get_checked_in_users
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.reservations = []
    
    def add_room(self, room):
        self.rooms.append(room)
    
    def check_availability(self, from_date, to_date, room_type):
        pass

    




    

    





