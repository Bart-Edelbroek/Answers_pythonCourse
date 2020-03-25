class Mammals:
	def __init__(self):
		self.members = ['Elephant','Moose','Platypus']

	def printMembers(self):
		print('Mammals:')
		for member in self.members:
			print('\t '+ member)
