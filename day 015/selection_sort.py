def sort(arr):
    i = 0
    while i<len(arr):
        j = i+1
        k = i
        while j<len(arr):
            if arr[j] < arr[k]:
                k = j
            j+=1
        arr[k],arr[i] = arr[i],arr[k]
        i+=1
    return arr

print(sort([12,11,11,13,5,6]))
