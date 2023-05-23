import math

array = [1,2,3,4,5,6,7,8,9,10]
def BinarySearch(target,start,end ):

    if start > end:
        return "Not Found"
    
    MIDDLE = math.floor((start+end)/2)

    if target == array[MIDDLE]:
        return f"Found at index {MIDDLE}"
    if array[MIDDLE] > target:
        return BinarySearch(target, start,MIDDLE-1)
    if array[MIDDLE] < target:
        return BinarySearch(target, MIDDLE+1,end)
    
print(BinarySearch(10,0,len(array)-1))
