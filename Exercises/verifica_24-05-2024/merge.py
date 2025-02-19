def merge(nums1, m, nums2, n):

    
    if m > 1:
        for i in range(m, (len(nums1))-1):
        
            nums1.remove(nums1[i])

        nums1.remove(nums1[len(nums1)-1])

    if m > 0:
        new_nums1: list = nums1.copy()

    else: 
        new_nums1: list = []
        nums1.clear()


    new_nums2: list = []

    for j in range(n):

        new_nums2.append(nums2[j])

    for n1 in new_nums1:

        for n2 in new_nums2:

            if n2 < n1:

                ind: int = nums1.index(n1)

                nums1.insert(ind, n2)

                new_nums2.remove(n2)

    for i in new_nums2:

        nums1.append(i)



nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(merge(nums1, m, nums2, n))
print(nums1)  #Output [1, 2, 2, 3, 5, 6]