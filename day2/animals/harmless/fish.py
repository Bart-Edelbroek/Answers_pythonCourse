class Fish:
	def __init__(self):
		self.members = ['Salmon','Shark','Guppy']

	def printMembers(self):
		print('Fish:')
		for member in self.members:
			print('\t '+ member)
