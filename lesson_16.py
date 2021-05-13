# class A:
# 	"""docstring for A"""
# 	def __init__(self, a, b):
		
# 		self.a = a
# 		self.b = b

# 	def present_class(self):
# 		print(F"From class A {self.a} {self.b}")

# class B:
# 	"""docstring for B"""
# 	def __init__(self, a, b):
# 		self.c = a
# 		self.d = b

# 	def present_class(self):
# 		print(F"From class B {self.c} {self.d}")
# class New():
# 		"""docstring for New"""
# 		pass

# class C(A, B, New):
# 	"""docstring for c"""
# 	def __init__(self, name, q, w, a_e, a_t):
# 		self.name = name
# 		B.__init__(self, a=q, b=w)
# 		A.__init__(self, a=a_e, b=a_t)
# 	def present(self):
# 		print(F"Attrs of class C : from A {self.a}, {self.b}"\
# 			F"from B {self.c} {self.d} C :{self.name}")
		
# c_obj = C("c_object", "q", "w", "e", "t")

# c_obj.present()
# print("C obj")
# c_obj.present_class()

# print(C.__mro__)
# a_obj = A(1, 2)
# b_obj = B(3, 4)

# a_obj.present_class()
# b_obj.present_class()

class Resume:
	"""docstring for Resume"""
	def __init__(self, name, age, height):
		self.name = name
		self._age = age
		self.__height = height
	@property
	def age(self):
		return self._age
	@age.setter
	def age(self, num):
		print("setter worked")
		self._age = num

		# if self._age < 18:
		# 	return "not adult"
		# else:
		# 	return "adult"
	


resume_1 = Resume("john", 24, 175)
print(resume_1._age)
# print(resume_1._Resume__height)
print(resume_1.age)
resume_1.age = 15
print(resume_1.age)