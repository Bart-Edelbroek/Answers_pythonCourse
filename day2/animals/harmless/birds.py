class Birds:
	def __init__(self):
		self.members = ['Robin','Blackbird','Parrot']

	def printMembers(self):
		print('Birds:')
		for member in self.members:
			print('\t '+ member)
