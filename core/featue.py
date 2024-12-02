# Write a function that takes in an array of integers and returns the sum of all even numbers in the array.


def sum_of_evens(arr):
        return sum(num for num in arr if num % 2 == 0)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(sum_of_evens(arr))  # 30


# Write a function to sort an array of integers in ascending order.
def sort_array(arr):
    return sorted(arr)



## Sort function 
# logic for sort function 
# get the array a[5,3,4,2]
# for (i=0; i < count(a) -1; i++)
# if(a[i] > a[i+1])
# return 0 
# else 1

# Write a function that turns an array of objects into a single object where the keys are the ids of the objects, and the values are the objects themselves.
# input: [{'id': 'abc', 'name': 'John'}, {'id': 'efg', 'name': 'Jane'}] output: {'abc': {'id': 'abc', 'name': 'John'}, 'efg': {'id': 'efg', 'name': 'Jane'}]

# input = [{'id': 'abc', 'name': 'John'}, {'id': 'efg', 'name': 'Jane'}] output: {'abc': {'id': 'abc', 'name': 'John'}, 'efg': {'id': 'efg', 'name': 'Jane'}]
# optimizedarray = [];
# for(i = 0 ;i < count(input) i++)
   # optimizedarray = [input[i]['id'] => input[i]];

# return optimizedArray


