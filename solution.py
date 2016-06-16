import numpy as np

matrix = np.random.randint(0, 10, size=(10, 10, 10)) #actual task
# matrix = np.random.randint(0, 10, size=(3, 3, 3)) #useful for debugging

def max_sum(dimension, matrix):
    dim_sums = np.apply_along_axis(np.sum, dimension, matrix)
    dim_max_i, dim_max_j = np.unravel_index(dim_sums.argmax(), dim_sums.shape)
    # print(matrix) #not-so useful for debug, but good visualization
    # print(dim_sums) #useful for debug
    # print(dim_max_i,dim_max_j) #useful for debug

    if(dimension==0):
        print(matrix[:, dim_max_i, dim_max_j])

    elif (dimension==1):
        print(matrix[dim_max_i, :, dim_max_j])

    else:
        print(matrix[dim_max_i, dim_max_j, :])

print("Largest column sum along 1st dimension: ")
max_sum(0, matrix)

print("Largest column sum along 2nd dimension: ")
max_sum(1, matrix)

print("Largest column sum along 3rd dimension: ")
max_sum(2, matrix)

