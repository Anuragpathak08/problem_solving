def merge_sort(arr,left,right):
    if len(arr)>1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr,left,mid)
        merge_sort(right_arr,mid+1,right)
        i = 0
        j = 0
        k = 0
        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]:
                arr[k]=left_arr[i]
                i+=1 
                
            elif left_arr[i] > right_arr[j]:
                arr[k] = right_arr[j]
                j+=1
            k+=1
            
        while i < len(left_arr):
            arr[k]=left_arr[i]
            i+=1
            k+=1
        while j < len(right_arr):
            arr[k]=right_arr[j]
            j+=1
            k+=1

    return arr


arr=[31,3,24,112,5]
print(merge_sort(arr,0, len(arr)))