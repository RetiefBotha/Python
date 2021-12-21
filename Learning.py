# #NumPy Arrays
# import numpy as np

# my_list = [1,2,3]
# np_arr = np.asarray(my_list)

# print(np_arr)
# print(np_arr.dtype)
# print(np_arr.shape)


# np_zeros = np.zeros((5,5))
# print(np_zeros) 

# np_zeros_int = np.zeros((5,5), dtype = int)
# print(np_zeros_int) 

# np_ones = np.ones((5,5), dtype = int)
# print(np_ones)

# np_range = np.arange(start = 2, step = 2, stop = 20)
# print(np_range)

# np_linspace = np.linspace(2, 30, 5)
# print(np_linspace)



# #Accessing, Reshaping and Modifying NumPy Arrays
# import numpy as np

# my_arr = np.arange(20)
# print(my_arr)

# my_arr_reshape = np.reshape(my_arr, (5,4))
# print(my_arr_reshape)

# my_arr_reshape2 = np.reshape(my_arr, (5,4), order = "F")
# print(my_arr_reshape2)

# #Modifying List and 2 Dimentional Array
# my_list = list(my_arr)
# my_list[1] = 5
# my_arr[1] = 555
# print(my_list[1])
# print(my_list)
# print(my_arr[1])
# print(my_arr)


# #Modifying 3 Dimentional Array
# my_list_reshaped = list(my_arr_reshape2)
# print(my_arr_reshape2[0,1])
# print(my_list_reshaped[0][1])




# #Slicing and Copying Arrays
# import numpy as np

# np.random.seed(0)
# np_random = np.random.random((3,3))
# np_sub_random = np.copy(np_random[0:2, 0])
# print(np_random)
# print(np_sub_random)




# #Array Logical Indexing
# import numpy as np

# np_arr = np.array([[1,2,3,],[4,5,6],[7,8,9]])
# np_con = np_arr[np_arr > 3]

# print(np_con)
# print(np_arr > 3)




#Broadcasting Array
import numpy as np

np_arr1 = np.array([[2,3],[4,10]])
np_broad = np_arr1 * 5
print(np_broad,"\n\nDiffrent way to do the same,but its faster")

np_five = np.array([[5,5],[5,5]])
np_broad_five = np_arr1 * np_five
print(np_broad_five)   




#Broadcasting Array




#Broadcasting Array