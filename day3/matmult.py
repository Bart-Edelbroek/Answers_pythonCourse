# Program to multiply two matrices using nested loops
import random
import numpy as np

# NxN matrix
@profile
def gen_x(N):
	X = np.random.rand(N, N)
	return X

# Nx(N+1) matrix
@profile
def gen_y(N):
	Y = np.random.rand(N, (N+1))
	return Y

"""

# result is Nx(N+1)
@profile
def res_gen(N):
	result = []
	for i in range(N):
		result.append([0] * (N+1))
	return result



# iterate through rows of X
@profile
def res_calc():
	for i in range(len(X)):
    # iterate through columns of Y
		for j in range(len(Y[0])):
    	# iterate through rows of Y
			for k in range(len(Y)):
				result[i][j] += X[i][k] * Y[k][j]
	return result

"""

@profile
def numpy_matmul():
	a = np.array(X)
	b = np.array(Y)
	return(np.matmul(a, b))




N = 250
X = gen_x(N)
Y = gen_y(N)
#result = res_gen(N)
#result = res_calc()
r2 = numpy_matmul()
#print("result")
#for r in result:
#    print(r)

print("numpy")
print(r2)
