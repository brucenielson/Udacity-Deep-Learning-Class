import numpy as np
element = [[1,2],
           [3,4]]

test_elements = [
                 [[1,2],
                  [3,4]],
                 [[2,3],
                  [4,5]]
                ]

output = np.isin(element, test_elements)
#print(output)


def multidim_intersect(arr1, arr2):
    print([('',arr1.dtype)]*arr1.shape[1])
    arr1_view = arr1.view([('',arr1.dtype)]*arr1.shape[1])
    print(arr1_view)

    arr2_view = arr2.view([('',arr2.dtype)]*arr2.shape[1])
    intersected = np.intersect1d(arr1_view, arr2_view)
    return intersected.view(arr1.dtype).reshape(-1, arr1.shape[1])


test_arr1 = np.array([[0, 2],
                         [1, 3],
                         [4, 5],
                         [0, 2]])

test_arr2 = np.array([[1, 2],
                         [0, 2],
                         [3, 1],
                         [1, 3]])

output = multidim_intersect(test_arr1, test_arr2)
print(output)