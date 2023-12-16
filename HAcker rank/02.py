import numpy

arr = [1, 2, 3, 4, -8, -10]
b = numpy.array(arr, float)
c = b[:: -1]
print(c)
