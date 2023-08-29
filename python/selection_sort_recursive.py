


"""
similar to the previous algo
base limit should be something related to the length of the array? 

where if len(array) == 1, return array[0] ?

This is similar to find_shortest_string. except instead of returning the element, return the array?
I tried using recursion to iterate through each element, but I am having issues
    when i < i + 1, you swap the elements. then, you add i + call the function again with the first element chopped off

got super close to using a recursive selection sort in place but can't figure out how to start back at the begining of the list

going to try using the iterative solution where MIN was used

so the min of 5, -3, 1, 4 is -3
pop that out and now you have 5, 1 , 4

before you attach it to the begining of the list, you call the function again
5, -3, 1, 4
min is -3

5, 1, 4
min is 1

5, 4
min is 4,

5,
min is 5

[]
list is 0, return list? this is the base case

min + return of function call





gonna solve this with python first since I'm more familar with that and then try JS
"""


def selection_sort_recursive(arr):
    if len(arr) == 0:
        return arr

    min_value = min(arr)
    arr.remove(min_value)
    return [min_value] + selection_sort_recursive(arr)

    # current = arr.pop()
    # last = arr.pop()

    # if current < last:
    #     arr.append(current)
    #     return selection_sort_recursive(arr).append(last)
    # else:
    #     arr.append(last)
    #     arr = selection_sort_recursive(arr)
    #     print(arr)
    #     return arr

    # if arr[0] <= arr[1]:
    #     arr = [arr[0]] + selection_sort_recursive(arr[1:])
    # else:
    #     arr_1 = arr[1]
    #     arr_0 = arr[0]
    #     arr[1] = arr_0
    #     arr[0] = arr_1

    # if arr[0] > arr[1]:
    #     arr_1 = arr[1] #-1
    #     arr_0 = arr[0] #3
    #     arr[1] = arr_0
    #     arr[0] = arr_1
    #     arr_0 = arr[0]

    #     arr = selection_sort_recursive(arr[1:])
    #     if arr[0] > arr[1]:
            
    #     arr = [arr[0]] + 
    # else:
    #     return arr
    
    # else:
    #     arr_0 = [arr[0]]
    #     arr = arr[1:]
    #     if arr[0] > arr[1]:
    #         arr_1 = arr[1] #-1
    #         arr_0 = arr[0] #3
    #         arr[1] = arr_0
    #         arr[0] = arr_1
    #         return [arr[0]] + selection_sort_recursive(arr[1:])
        # return arr_0 + arr
    # selection_sort_recursive(test_2)

if __name__ == "__main__":
    test_values = [
        [3, -1, 5, 2],
        [5, 4, 10, 0]
    ]

    test_answers = [
        [-1, 2, 3, 5],
        [0, 4, 5, 10]
    ]

    for value, answer in zip(test_values, test_answers):
        result = selection_sort_recursive(value)

        try:
            assert result == answer
        except:
            print(f"Test failed for {value}. Expected {answer}, got {result}")
        else:
            print(f"Test Successful")