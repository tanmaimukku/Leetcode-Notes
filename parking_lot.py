'''
Requirements:

1) Parking Lot, should be able to park vehicles and unpark vehicles
2) When new vehicle enters parking lot, it should be assigned a parking ticket with a unique parking spot id, and the parking spot id should be able to retrieve the exact location of the vehicle (Level etc.)
3) Three different sizes of vehicles, three different sizes of parking spots
4) e.g. if a small vehicle comes and there is an empty small and medium parking spot, we should fill the small parking spot first


Clarifications:

1) Parking can be sequential, so you can check for the first available parking spot starting from the bottommost level

Classes:

1) Vehicle
2) VehicleSize(Enum)
3) ParkingSpot
4) ParkingLevel
5) ParkingLot - Singleton Class

Attributes and Methods:

1) Vehicle:
Attributes: license -> str, size -> int, parking_spot_id -> str
Methods: get_size

2) ParkingSpot:
Attributes: parking_spot_id -> str, level_number -> int, is_occupied -> boolean, size -> int, vehicle -> Vehicle
Methods: park_vehicle, unpark_vehicle, get_is_occupied

3) ParkingLevel:
Attributes: level_number -> int, number_of_spots -> int, parking_spots -> List[ParkingSpot], available_spots -> int
Methods: get_available_spots, park_vehicle, unpark_vehicle

4) ParkingLot:
Attributes: parking_levels -> List[ParkingLevel], number_of_levels, spots_per_level
Methods: park_vehicle, unpark_vehicle, extract_level_from_parking_spot_id, get_available_spots 

'''

from enum import Enum
class VehicleSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Vehicle:
    def __init__(self, license, size, parking_spot_id):
        self.license = license
        self.size = size
        self.parking_spot_id = parking_spot_id

    def get_size(self):
        return self.size


class ParkingSpot:
    def __init__(self, size, level_number, parking_spot_id):
        self.size = size
        self.level_number = level_number
        self.parking_spot_id = parking_spot_id
        self.is_occupied = False
        self.vehicle = None

    def can_fit_vehicle(self, vehicle) -> bool:
        if vehicle.get_size()<=self.size:
            return True
        else:
            return False
    
    def park_vehicle(self, vehicle) -> bool:
        if self.can_fit_vehicle(vehicle) and not(self.is_occupied):
            self.vehicle = vehicle
            self.vehicle.parking_spot_id = self.parking_spot_id
            self.is_occupied = True
            return True
        else:
            return False
    
    def unpark_vehicle(self) -> bool:
        if self.is_occupied:
            self.vehicle = None
            self.vehicle.parking_spot_id = None
            self.is_occupied = False
            return True
        else:
            return False
    
    def get_is_occupied(self) -> bool:
        return self.is_occupied

    def get_parking_spot_id(self) -> str:
        return self.parking_spot_id

class ParkingLevel:
    def __init__(self, level_number, number_of_spots):
        self.level_number = level_number
        self.number_of_spots = number_of_spots
        self.parking_spots = []
        self.available_spots = number_of_spots

        for i in range(number_of_spots):
            if i < number_of_spots//3:
                size = VehicleSize.SMALL
            elif i <2*number_of_spots//3:
                size = VehicleSize.MEDIUM
            else:
                size = VehicleSize.LARGE
            
            parking_spot_id = f"L{level_number}-S{i}"
        
            self.parking_spots.append(ParkingSpot(size, level_number, parking_spot_id))
    
    def get_available_spots(self) -> int:
        return self.available_spots

    def get_level_number(self) -> int:
        return self.level_number

    
    def park_vehicle(self, vehicle) -> bool:
        if self.available_spots == 0:
            return False
        
        for parking_spot in self.parking_spots:
            if parking_spot.can_fit_vehicle(vehicle):
                parking_spot.park_vehicle(vehicle)
                self.available_spots = self.available_spots - 1
                return True
        
        return False

    def unpark_vehicle(self, parking_spot_id) -> bool:
        for parking_spot in self.parking_spots:
            if parking_spot.get_parking_spot_id() == parking_spot_id and parking_spot.get_is_occupied():
                parking_spot.unpark_vehicle()
                self.available_spots = self.available_spots + 1
                return True
            
        return False

    
class ParkingLot:

    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    
    def __init__(self, number_of_levels, spots_per_level):
        self.number_of_levels = number_of_levels
        self.spots_per_level = spots_per_level
        self.parking_levels = [ParkingLevel(i, spots_per_level) for i in range(number_of_levels)]

    def extract_level_from_parking_spot_id(self, parking_spot_id) -> int:
        return int(parking_spot_id.split("-")[0][1:])
    
    def park_vehicle(self, vehicle) -> bool:
        for parking_level in self.parking_levels:
            if parking_level.get_available_spots()>0:
                if parking_level.park_vehicle(vehicle):
                    return True
        return False

    def unpark_vehicle(self, parking_spot_id) -> bool:
        level_number = self.extract_level_from_parking_spot_id(parking_spot_id)
        for parking_level in self.parking_levels:
            if parking_level.get_level_number() == level_number:
                if parking_level.unpark_vehicle(parking_spot_id):
                    return True
        return False

    def get_available_spots(self) -> int:
        return sum(parking_level.get_available_spots() for parking_level in self.parking_levels)
    

    




    
    

    

