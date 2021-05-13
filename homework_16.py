class Hotel:
    """docstring for Hotel"""
    def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):
        self.name = name
        self.place = place
        self.rooms_mid = rooms_mid
        self.mid_room_price = mid_room_price
        self.rooms_lux = {room1:1, room2:1, room3: 1}
        self.lux_room_price = lux_room_price

    def presentation(self):
        hotel_presentation = F"Hotel{self.name} in {self.place} wiche mid rooms price is {self.mid_room_price} and lux rooms price {self.lux_room_price}  "
        return hotel_presentation
    def booking(self):
        return
    def available_room_check(self):
        self.free_rooms = {}
        if 
        for key, value in self.rooms_mid.items():
            if value==1:
                self.free_rooms[key] = value
        for key, value in self.rooms_lux.items():
            if value==1:
                self.free_rooms[key] = value
        return self.free_rooms
    def discount(self):
        return
# class Taxi:
#     """docstring for Taxi"""
#     def __init__(self, name, car_types, price_for_tour):
#         self.name = name
#         self.car_types = car_types
#         self.price_for_tour = price_for_tour
#     def presentation():
#         p = F"This is {self.name} car typs is {self.car_types} and tour price is  {self.price_for_tour}"
#         return p
#     def discount(self): 
#         return
# class Tour(Hotel, Taxi):
#     """docstring for Tour"""
#     def __init__(self, name, price_lux, price_mid, price_for_tour, car_types, place,lux_room_price, rooms_lux, mid_room_price, rooms_mid):
        
#         self.name = name
#         self.price_lux = price_lux
#         self.price_mid = price_mid
#         Taxi.__init__(self, name, car_types, price_for_tour )
#         Hotel.__init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
#     def presentation(self):
#         glogal_presetation = F"Hello we offer {self.name} tour we have two options {self.price_lux},{self.price_for_tour}"\
#         F"which includes transport with ride_over company which provides bmw cars and price for it is {self.price_for_tour},"
#         F"we will stay at Lerane which offers two types of rooms middle {self.mid_room_price} and lux {self.lux_room_price}"

#         return glogal_presetation
#touu = Tour(name="Ando", price_lux= 10000, place = "Gexard", price_mid = 1000, price_for_tour=200000, car_types= "BMW")
hot = Hotel(name="Mariot", place="Yerevan", rooms_mid={'room1':1, 'room2':0, 'room3':1}, mid_room_price=1000, rooms_lux={'room1':1, 'room2':1, 'room3':1}, lux_room_price=20000)
# print(Tour.presentation(touu))
# print(Taxi.presentation(touu))
print(Hotel.booking(hot))
        
        