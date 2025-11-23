class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        array = []
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] > nums2[j]:
                array.append( nums2[j])
                j+=1

            elif nums1[i] <= nums2[j]:
                array.append( nums1[i])
                i+=1

            
        
        while i<len(nums1):
            array.append( nums1[i])
            i+=1

        while j<len(nums2):
            array.append( nums2[j])
            j+=1

        l = len(array)
        if l%2 == 0 :
            median = (array[l//2]+array[(l//2)-1])/2
        else:
            median = array[l//2]

        return median
