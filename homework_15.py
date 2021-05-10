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
		pass
		return
class Triangle(Shape):
	"""docstring for Triangle"""
	def __init__(self, side1, side2, base, height,name):
		self.height = height
		self.side1 = side1
		self.side2 = side2
		self.base = base
		super().__init__(name)

	def present(self):
		pass
		return
	def area(self):
		triangle_area_result= 1/2 * self.height * self.base 
		return F"Triangle area is {triangle_area_result}"
	def perimeter(self):
		triangle_perimeter_result = self.sides1 + self.sides2 + self.base
		return F"Triangle parimeter is {triangle_perimeter_result}"
class Square(Shape):
	"""docstring for ClassName"""
	def __init__(self, side1, side2, name):
		self.side1 = side1
		self.side2 = side2
		super().__init__(name)
	def present(self):
		pass
		return
	def area(self):
		square_area_result = self.side1 * self.side2
		return F"Square area is {square_area_result}"
	def perimeter(self):
		square_perimeter_result = 2 * self.side1 * self.side2 
		return F"Square area is {square_perimeter_result}"
	def get_bias(self):
		square_get_bias_result = sqrt(self.side1 ** 2 + self.side2 ** 2)
		return F"Square get_bias is {square_perimeter_result}"
		