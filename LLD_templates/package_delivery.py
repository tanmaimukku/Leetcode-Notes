import math
import uuid
from typing import List, Optional

class Locker:
    def __init__(self, locker_id: int, size: str, x: float, y: float, store_open: int, store_close: int):
        self.locker_id = locker_id
        self.size = size  # "SMALL", "MEDIUM", "LARGE", "XL", "XXL"
        self.x = x  # x-coordinate
        self.y = y  # y-coordinate
        self.is_available = True  # Availability status
        self.package = None  # Assigned package (if any)
        self.qr_code = None  # QR Code tied to the locker for package retrieval
        self.store_open = store_open  # Store opening time in 24-hour format
        self.store_close = store_close  # Store closing time in 24-hour format
        self.expiry_time = None  # Expiry timestamp for package

    def assign_package(self, package):
        self.package = package
        self.is_available = False
        self.qr_code = str(uuid.uuid4())[:6]  # Generate a unique 6-digit QR code
        self.expiry_time = package.delivery_time + (3 * 24 * 60 * 60)  # 3 days in seconds

    def release_package(self):
        self.package = None
        self.is_available = True
        self.qr_code = None
        self.expiry_time = None

    def is_within_operating_hours(self, current_time: int) -> bool:
        return self.store_open <= current_time <= self.store_close

class Package:
    def __init__(self, package_id: int, size: str, x: float, y: float, delivery_time: int):
        self.package_id = package_id
        self.size = size  # "SMALL", "MEDIUM", "LARGE", "XL", "XXL"
        self.x = x  # Delivery location x-coordinate
        self.y = y  # Delivery location y-coordinate
        self.delivery_time = delivery_time  # Timestamp of delivery

class LockerSystem:
    def __init__(self):
        self.lockers: List[Locker] = []

    def add_locker(self, locker: Locker):
        self.lockers.append(locker)

    def find_nearest_available_locker(self, package: Package, current_time: int) -> Optional[Locker]:
        nearest_locker = None
        min_distance = float("inf")

        for locker in self.lockers:
            if (locker.is_available and locker.size == package.size and 
                locker.is_within_operating_hours(current_time)):
                # Calculate Euclidean distance
                distance = math.sqrt((locker.x - package.x) ** 2 + (locker.y - package.y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    nearest_locker = locker

        return nearest_locker

    def assign_locker_to_package(self, package: Package, current_time: int) -> bool:
        locker = self.find_nearest_available_locker(package, current_time)
        if locker:
            locker.assign_package(package)
            print(f"Package {package.package_id} assigned to Locker {locker.locker_id} with QR Code {locker.qr_code}.")
            return True
        else:
            print(f"No available locker for Package {package.package_id}.")
            return False

    def release_locker(self, locker_id: int):
        for locker in self.lockers:
            if locker.locker_id == locker_id:
                locker.release_package()
                print(f"Locker {locker_id} is now available.")
                return
        print(f"Locker {locker_id} not found.")

    def process_expired_packages(self, current_time: int):
        for locker in self.lockers:
            if not locker.is_available and locker.expiry_time <= current_time:
                print(f"Package in Locker {locker.locker_id} has expired. Initiating refund process.")
                locker.release_package()

# Example usage
if __name__ == "__main__":
    locker_system = LockerSystem()

    # Adding lockers
    locker_system.add_locker(Locker(1, "SMALL", 0, 0, 800, 2000))
    locker_system.add_locker(Locker(2, "MEDIUM", 5, 5, 800, 2000))
    locker_system.add_locker(Locker(3, "LARGE", 10, 10, 800, 2000))
    locker_system.add_locker(Locker(4, "SMALL", 2, 3, 800, 2000))

    # Creating a package
    package = Package(101, "SMALL", 1, 2, 1700000000)  # Assume delivery_time as a timestamp

    # Assigning a locker to the package
    current_time = 1700000000  # Assume current_time as a timestamp
    locker_system.assign_locker_to_package(package, current_time)

    # Simulating expired packages
    expired_time = 1700000000 + (4 * 24 * 60 * 60)  # 4 days later
    locker_system.process_expired_packages(expired_time)

    # Releasing a locker
    locker_system.release_locker(1)
