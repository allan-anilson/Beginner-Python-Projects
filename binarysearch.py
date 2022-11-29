def binsearch(arr,target):     #Binary Search without Recursion
    start = 0
    end = len(arr)-1
    mid = 0
    while(start<=end):
        mid = (start+end)//2
        if arr[mid]>target:
            end = mid-1
        elif arr[mid]<target :
            start = mid+1
        else:
            return mid
    return -1

def linearsearch(arr, target):
    for i in range(len(arr)):
        if(arr[i]==target):
            return i
    return -1

def recbinsearch(arr,start, end, target):     #Binary Search with Recursion
    if start<=end:     
        mid = (start+end)//2
        if arr[mid]>target:
            return recbinsearch(arr, start, mid-1, target)
        elif arr[mid]<target :
            return recbinsearch(arr, mid+1, end, target)        
        else:
            return mid
    else:
        return -1

arr = [3,4,6,8,11,13,15,22,25]
print(linearsearch(arr, 13))
print(recbinsearch(arr,0,len(arr)-1, 13))
