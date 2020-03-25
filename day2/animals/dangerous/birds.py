class Birds:
	def __init__(self):
		self.members = ['Cassowary','Ostridge','Vulture']

	def printMembers(self):
		print('Birds:')
		for member in self.members:
			print('\t '+ member)
