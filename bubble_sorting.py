unsorted = [43, 5, 1, 7, 80, 4, 9,-9, -5, 2, 6, -12]
# random array
def bubble_sorting_algorithm(array):
    for i in range(len(array)):
        #each list item needs to be looped

        for item in range(len(array)-i-1):
            #each list item need to get compared and sorted in it's correct index

            if array[item]>array[item+1]:
                array[item], array[item+1] = array[item+1], array[item]
    return array
print(bubble_sorting_algorithm(unsorted))
# output: [-12, -9, -5, 1, 2, 4, 5, 6, 7, 9, 43, 80]
