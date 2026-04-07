def sort(arr):
    i = 1
    while i<len(arr):
        j=0
        while j <= i:
            if arr[j]> arr[i]:
                arr[j] , arr[i] = arr[i], arr[j]
            j+=1
        i+=1
    return arr

print(sort([12,11,11,13,4,6,5,7]))