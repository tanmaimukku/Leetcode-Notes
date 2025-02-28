'''
Requirements:
1) Users should be able to search availability (Range of dates)
2) Users should be able to reserve rooms (multiple if needed), cancel, modify their booking if needed
3) A reservation should be linked to a user and specific room(s)
4) System should support multiple room types (suite, single, double)
5) Should be able to calculate price for a reservation (each room will have a price per day)
6) Guests should be able to check in and check out
7) System should be able to retrieve a reservation for a user
8) View checked-in guests and expected check-out dates

Classes:
1) User
2) Room
3) Reservation
4) Hotel

Attributes and Methods:

1) User  
   - **Attributes**: `user_id`, `name`, `reservations: List[Reservation]`  
   - **Methods**:  
     - `add_reservation(reservation)`: Adds a reservation to the user  

2) Room  
   - **Attributes**: `room_id`, `room_type`, `price_per_night`, `max_occupancy`, `is_booked`  
   - **Methods**:  
     - `__repr__()`: Returns a string representation of the room  

3) Reservation  
   - **Attributes**: `reservation_id`, `user`, `rooms: List[Room]`, `start_date`, `end_date`, `is_checked_in`, `is_cancelled`  
   - **Methods**:  
     - `calculate_price()`: Computes the total price for the reservation  
     - `check_in()`: Marks the reservation as checked-in  
     - `check_out()`: Marks the reservation as checked-out  
     - `cancel()`: Cancels the reservation  

4) Hotel  
   - **Attributes**: `name`, `rooms: List[Room]`, `reservations: Dict[int, Reservation]`, `reservation_counter`  
   - **Methods**:  
     - `add_room(room)`: Adds a new room to the hotel  
     - `check_availability(start_date, end_date, room_type, num_rooms)`: Checks available rooms  
     - `create_reservation(user, start_date, end_date, room_type, num_rooms)`: Creates a new reservation  
     - `get_user_reservations(user)`: Retrieves all reservations for a user  
     - `get_checked_in_guests()`: Retrieves a list of checked-in guests  
'''

from datetime import date
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
from enum import Enum

class RoomType(Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"

class IReservable(ABC):
    @abstractmethod
    def check_availability(self, start_date: date, end_date: date, room_type: RoomType, num_rooms: int) -> List['Room']:
        pass

    @abstractmethod
    def create_reservation(self, user: 'User', start_date: date, end_date: date, room_type: RoomType, num_rooms: int):
        pass

class Room:
    def __init__(self, room_id: int, room_type: RoomType, price_per_night: float, max_occupancy: int):
        self.room_id = room_id
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_occupancy = max_occupancy
        self.is_booked = False  # Simplified for now
    
    def __repr__(self):
        return f"Room({self.room_id}, {self.room_type.value}, ${self.price_per_night}/night)"

class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name
        self.reservations: List['Reservation'] = []

    def add_reservation(self, reservation: 'Reservation'):
        self.reservations.append(reservation)
    
    def __repr__(self):
        return f"User({self.user_id}, {self.name})"

class Reservation:
    def __init__(self, reservation_id: int, user: User, rooms: List[Room], start_date: date, end_date: date):
        self.reservation_id = reservation_id
        self.user = user
        self.rooms = rooms
        self.start_date = start_date
        self.end_date = end_date
        self.is_checked_in = False
        self.is_cancelled = False

    def calculate_price(self):
        days = (self.end_date - self.start_date).days
        return sum(room.price_per_night * days for room in self.rooms)
    
    def modify_reservation(self, new_start_date: date, new_end_date: date):
        if not self.is_checked_in and not self.is_cancelled:
            self.start_date = new_start_date
            self.end_date = new_end_date
        else:
            raise ValueError("Cannot modify a checked-in or cancelled reservation")
    
    def check_in(self):
        if not self.is_cancelled:
            self.is_checked_in = True
    
    def check_out(self):
        if self.is_checked_in:
            self.is_checked_in = False
    
    def cancel(self):
        if not self.is_checked_in:
            self.is_cancelled = True
    
    def __repr__(self):
        return f"Reservation({self.reservation_id}, User: {self.user.name}, Rooms: {[room.room_id for room in self.rooms]}, Dates: {self.start_date} - {self.end_date})"

class Hotel(IReservable):
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.reservations: Dict[int, Reservation] = {}
        self.reservation_counter = 1
    
    def add_room(self, room: Room):
        self.rooms.append(room)
    
    def check_availability(self, start_date: date, end_date: date, room_type: RoomType, num_rooms: int) -> List[Room]:
        available_rooms = [room for room in self.rooms if room.room_type == room_type and not room.is_booked]
        return available_rooms[:num_rooms]
    
    def create_reservation(self, user: User, start_date: date, end_date: date, room_type: RoomType, num_rooms: int):
        available_rooms = self.check_availability(start_date, end_date, room_type, num_rooms)
        if len(available_rooms) < num_rooms:
            raise ValueError("Not enough rooms available")
        
        reservation = Reservation(self.reservation_counter, user, available_rooms, start_date, end_date)
        self.reservations[self.reservation_counter] = reservation
        self.reservation_counter += 1
        
        for room in available_rooms:
            room.is_booked = True
        
        user.add_reservation(reservation)
        return reservation
    
    def get_user_reservations(self, user: User):
        return [res for res in self.reservations.values() if res.user == user]
    
    def get_checked_in_guests(self):
        return [res for res in self.reservations.values() if res.is_checked_in]
    
    def __repr__(self):
        return f"Hotel({self.name}, Rooms: {len(self.rooms)})"

# Example Usage
if __name__ == "__main__":
    hotel = Hotel("Grand Hotel")
    hotel.add_room(Room(101, RoomType.SINGLE, 100.0, 1))
    hotel.add_room(Room(102, RoomType.DOUBLE, 150.0, 2))
    
    user1 = User(1, "Alice")
    reservation1 = hotel.create_reservation(user1, date(2025, 3, 1), date(2025, 3, 5), RoomType.SINGLE, 1)
    
    print(reservation1)
    print("Total Price:", reservation1.calculate_price())
    
    reservation1.check_in()
    print("Checked-in guests:", hotel.get_checked_in_guests())
    
    # Example of modifying a reservation
    try:
        reservation1.modify_reservation(date(2025, 3, 2), date(2025, 3, 6))
        print("Modified Reservation:", reservation1)
    except ValueError as e:
        print("Error:", e)
