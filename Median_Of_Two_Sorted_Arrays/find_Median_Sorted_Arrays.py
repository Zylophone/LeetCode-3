class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = 0
        nums = []
        length = len(nums1) + len(nums2)
        len1 = len(nums1)
        len2 = len(nums2)
        while i < length :

            # i += 1
            if length % 2 == 1 and i  > length // 2 :
                return nums[i - 1]
            elif length % 2 == 0 and i > length // 2:
                return (float(nums[i - 2]) + float(nums[i - 1])) / 2
            elif len1 == 0:
                if len2 % 2 == 1:
                    return nums2[len2 // 2]
                else:
                    return (nums2[len2 // 2] + nums2 [len2 // 2 - 1]) / 2
            elif len2 == 0:
                if len1 % 2 == 1:
                    return nums1[len1 // 2]
                else:
                    return (nums1[len1 // 2] + nums1 [len1 - 1]) / 2
            if len1 == 1 and len2 == 1:
                return (nums1[0] + nums2[0]) / 2

            elif len(nums1) == 0:
                nums.append(nums2[0])
                nums2.pop(0)

            elif len(nums2) == 0:
                nums.append(nums1[0])
                nums1.pop(0)

            elif nums1[0] < nums2[0]:
                nums.append(nums1[0])
                nums1.pop(0)

            elif nums1[0] > nums2[0]:
                nums.append(nums2[0])
                nums2.pop(0)

            elif nums1[0] == nums2[0]:
                nums.append(nums1[0])
                # nums.append(nums2[0])
                nums1.pop(0)
                # nums2.pop(0)

            i += 1

demo = Solution()
nums1 = [10000]
nums2 = [10001]
print(demo.findMedianSortedArrays(nums1, nums2))