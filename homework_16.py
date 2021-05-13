class Hotel:
	"""docstring for Hotel"""
	def __init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price):
		self.name = name
		self.place = place
		self.rooms_mid = rooms_mid
		self.mid_room_price = mid_room_price
		self.rooms_lux = rooms_lux
		self.lux_room_price = lux_room_price

	def presentation(self):
		hotel_presentation = F"Hotel{self.name} in {self.place} wiche mid rooms price is {self.mid_room_price} and lux rooms price {self.lux_room_price}  "
		return
	def booking(self):
		# if self.rooms_mid:
		# 	for i in self.rooms_mid:
		# 		if i == "free"
		# 			room_result = F""
			
		return
	def available_room_check(self):
		return
	def discount(self):
		return
class Taxi:
	"""docstring for Taxi"""
	def __init__(self, name, car_types, price_for_tour):
		self.name = name
		self.car_types = car_types
		self.price_for_tour = price_for_tour
	def presentation():
		p = F"This is {self.name} car typs is {self.car_types} and tour price is  {self.price_for_tour}"
		return p
	def discount(self): 
		return
class Tour(Hotel, Taxi):
	"""docstring for Tour"""
	def __init__(self, name, price_lux, price_mid, price_for_tour, car_types):
		
		self.name = name
		self.price_lux = price_lux
		self.price_mid = price_mid
		Taxi.__init__(self, name, car_types, price_for_tour )
		Hotel.__init__(self, name, place, rooms_mid, mid_room_price, rooms_lux, lux_room_price)
	def presentation(self):
		glogal_presetation = F"Hello we offer {self.name} tour we have two options {self.price_lux},{self.price_for_tour}"\
		F"which includes transport with ride_over company which provides bmw cars and price for it is {self.price_for_tour},"
		F"we will stay at Lerane which offers two types of rooms middle {self.mid_room_price} and lux {self.lux_room_price}"

		return glogal_presetation
touu = Tour(name="Ando", price_lux= 10000, place="Gexard", price_mid = 1000, price_for_tour=200000, car_types= "BMW")

print(Tour.presentation(touu))
print(Taxi.presentation(touu))

		
		