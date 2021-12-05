def findMedianSortedArrays(nums1, nums2):
    comb = nums1 + nums2
    comb.sort()

    if len(comb) % 2 == 0: # even
        idx = int(len(comb)/2)
        return (comb[idx]+comb[idx-1])/2.0
    else: # odd
        idx = int((len(comb)-1)/2)
        return float(comb[idx])

if __name__ == '__main__':
    print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
    print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
    print(findMedianSortedArrays(nums1 = [0,0], nums2 = [0,0]))
    print(findMedianSortedArrays(nums1 = [], nums2 = [1]))