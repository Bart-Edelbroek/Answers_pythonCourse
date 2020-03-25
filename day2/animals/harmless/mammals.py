class Mammals:
	def __init__(self):
		self.members = ['Pygmy shrew','Cat','Mouse']

	def printMembers(self):
		print('Mammals:')
		for member in self.members:
			print('\t '+ member)
