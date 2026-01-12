class Vehicle:
    def __init__(self,_vehicle_id,_base_rate):
        self._vehicle_id=_vehicle_id
        self._base_rate=_base_rate
        
    def display_details(self):
        return "Vehicle id is {} and base rate is {}".format(self._vehicle_id,self._base_rate)
 
    def rental_charge(self):
        return 0.0
        
class Car(Vehicle):
    def __init__(self,_vehicle_id,_base_rate,num_seats):
        self.num_seats=num_seats
        super().__init__(_vehicle_id,_base_rate)
        
    def rental_charge(self):
        return self._base_rate*self.num_seats
        
class Bike(Vehicle):
    def __init__(self,_vehicle_id,_base_rate,bike_type):
        self.bike_type=bike_type
        super().__init__(_vehicle_id,_base_rate)
        
    def rental_charge(self):
        return self._base_rate*0.5     
        
def calculate_rental(vehicle):
        return vehicle.rental_charge()
        
car=Car("CAR001",100.0,5)
bike=Bike("Bike001",78.2,"Scooter")
print(car.display_details())
print("Car Rental Charge:",calculate_rental(car))
print(bike.display_details())
print("Bike Rental Charge:",calculate_rental(bike))
    
    