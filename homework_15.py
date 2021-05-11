# 1 create class Shape which has
#  attrs: name
# methods: present_shape
# class Triangle which is child of class Shape
# attrs: side1, side2, base, height
# methods: present, area, perimeter
# class Square child of class Shape
# attrs: side1, side2
# methods: present, area, perimeter, get_bias (անկյունագիծ)
# and try
class Shape:
	"""docstring for ClassName"""
	def __init__(self, name):
		
		self.name = name
	def present_shape(self):
		
		return 
class Triangle(Shape):
	"""docstring for Triangle"""
	def __init__(self, side1, side2, base, height, name):
		self.height = height
		self.side1 = side1
		self.side2 = side2
		self.base = base
		self.name = "Triangle"
		super().__init__(name)
		
	def present(self):
		
		triangle_present = F"{self.name}'s height is {self.height} sides {self.side1}{self.side2} base{self.base}"
		return triangle_present
	def area(self):
		triangle_area_result= 1/2 * self.height * self.base 
		return F"Triangle area is {triangle_area_result}"
	def perimeter(self):
		triangle_perimeter_result = self.side1 + self.side2 + self.base
		return F"Triangle parimeter is {triangle_perimeter_result}"
class Square(Shape):
	"""docstring for ClassName"""
	def __init__(self, side1, side2, name):
		self.side1 = side1
		self.side2 = side2
		self.name = "Square"
		super().__init__(name)
		
	def present(self):
		Square_present = F"This is {self.name} " 
		return Square_present
	def area(self):
		self.square_area_result = self.side1 * self.side2
		return F"Square area is {self.square_area_result}"
	def perimeter(self):
		self.square_perimeter_result = 2 * self.side1 * self.side2 
		return F"Square area is {self.square_perimeter_result}"
	def get_bias(self):
		self.square_get_bias_result =  (self.side1 ** 2 + self.side2 ** 2) ** 0.5
		return F"Square get_bias is {self.square_get_bias_result}"

Shape1 = Triangle(height = 5, side1 = 3, side2 = 3, base = 6, name = "Triangle")
Shape2 = Square(side1 = 5, side2 = 5, name = "Square")
print(Triangle.present(Shape1))
print(Triangle.perimeter(Shape1))
print(Triangle.area(Shape1))
print(Square.present(Shape2))
print(Square.perimeter(Shape2))
print(Square.area(Shape2))
print(Square.get_bias(Shape2))

class Country:
	"""docstring for Country"""
	def __init__(self, name, continet):
		self.name = name
		self.continet = continet
	def country_continet(self):
		continet_text = F"Name is {name} continet is {self.continet}"

		return continet_text
class Brand:
	def __init__(self, brand_name, business_start_date):
		self.brand_name = brand_name
		self.business_start_date = business_start_date
	def brand_presentation(self):
		presentation_ = F"{self.brand_name} brand was founded {self.business_start_date}"
		return presentation_
class Season:
	def __init__(self, season_name, average_temperature)
		self.season_name = season_name
		self.average temperature = average temperature
	def season_presentation(self):
		presentation__ = F"{self.season_name} brand was founded {self.average temperature}"
		return presentation__
class Product(Country, Brand, Season):
	"""docstring for Product"""
	def __init__(self, product_name, product_type, product_price, product_quantity):
		self.product_name = product_name
		self.product_type = product_type
		self.product_price = product_price
		self.product_quantity = product_quantity
		self.given_percent = 50
	def product_present(self):
		present_product = F"This is {self.product_name} type is {self.product_type} price is {self.product_price} and quantity{self.product_quantity}"
		return present_product
	def product_price_percent(self):
		price_percen = self.product_price - (self.product_price * 50/100)
		return price_percen
	def increase_quantity(self):
		increase_quant = int(input("Pleas input to increase quantitys"))
		quantity_increase = self.product_quantity + increase_quant
		return quantity_increase
	def decrease_quantity(self):
		decrease_quant = int(input("Pleas input to increase quantitys"))
		quantity_decrease =  self.product_quantity - increase_quant
		return quantity_decrease
		