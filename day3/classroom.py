class Person:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname

	def printNameSubject(self):
		print('Fish:')
		for member in self.members:
			print('\t '+ member)
