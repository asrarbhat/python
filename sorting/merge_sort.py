"""

this module contains a single mathematically pure function that 
does merge sort of a given list/tuple/set and returns a list.

FUNCTIONS
---------

1.  merge_sort(array)

     eg

     merge_sort([1,5,4,2])  

     RETURNS  
           [1,2,4,5]

"""


def merge_sort(array):
    """
    returns a sorted list for a given list/tuple/set

    PARAMETERS
    -----------
    array : a list of homogenous primitive items eg a list of floats/ints/strings etc

    RETURNS
    ----------
        a sorted list for that input
    """

    # validating input
    if not isinstance(array, (list, tuple, set)):
        return False

    # this function merges two sorted arrays
    def merge(array1, array2):
        merged_array = []
        length1 = len(array1)
        length2 = len(array2)

        i = 0
        j = 0
        while(i < length1):
            if array1[i] <= array2[j]:
                merged_array.append(array1[i])
                i += 1
                continue
            merged_array.append(array2[j])
            j += 1
            if j == length2:
                return merged_array+array1[i:]

        return merged_array+array2[j:]

    def sort(array):

        # base condition of recursion
        length = len(array)
        if length == 1:
            return array

        half_length = length//2
        first_half_sorted = sort(array[:half_length])
        second_half_sorted = sort(array[half_length:])

        return merge(first_half_sorted, second_half_sorted)

    return sort(array)


# tests
if (__name__ == "__main__"):
    print(merge_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
