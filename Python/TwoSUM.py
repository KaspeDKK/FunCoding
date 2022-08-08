# Import time in order to add delay to application window.
import time

def twoSum(arr, Sum):

    # search first element in the array
    for i in range(len(arr) - 1):

        print("index i(1st num) is", i) # Debug values

        # search other element in the array
        for x in range(i + 1, len(arr)):

            print("index x(2nd num) is", x) # Debug values

            print("CheckSum is", arr[i] + arr[x]) # Debug values

            # if these two elemets sum to Sum, print the pair
            if arr[i] + arr[x] == Sum:
                
                print("Pair with Sum",Sum ,"is: (", arr[i],",",arr[x],")")
                time.sleep(60)

# Define application variables
arr = [1,3,5,6,11,23]
Sum = 9
CheckSum = 0

# Call function with two defined parameters
twoSum(arr,Sum)