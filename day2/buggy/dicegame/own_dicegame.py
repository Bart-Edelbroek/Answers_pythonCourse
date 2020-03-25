import random


print("Add the values of the dice")
print("It's really that easy")
print("What are you doing with your life.")

for i in range(5):
	roll = int(random.random() * 6 + 1)
	if roll == 1:
		print("---------\n|       |\n|   *   |\n|       |\n---------")
	elif roll == 2:
		print("---------\n|*      |\n|       |\n|      *|\n---------")
	elif roll == 3:
		print("---------\n|*      |\n|   *   |\n|      *|\n---------")
	elif roll == 4:
		print("---------\n|*     *|\n|       |\n|*     *|\n---------")
	elif roll == 5:
		print("---------\n|*     *|\n|   *   |\n|*     *|\n---------")
	else:
		print("---------\n|*     *|\n|*     *|\n|*     *|\n---------")

guess = input("Sigh. What is your guess?: ")
guess = int(guess)

