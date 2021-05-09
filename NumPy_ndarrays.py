# 1-D array
x = np.array([1, 2, 3])
x.ndim

# 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
Y.ndim

# Here the`zeros()` is an inbuilt function that you'll study on the next page. 
# The tuple (2, 3, 4( passed as an argument represents the shape of the ndarray
y = np.zeros((2, 3, 4))
y.ndim

# We save x into the current directory as 
np.save('my_array', x)

# We load the saved array from our current directory into variable z
z = np.load('my_array.npy')
