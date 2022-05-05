class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def getMedian(nums):
            if len(nums) % 2 == 1:
                mid = nums[len(nums)//2]
            else:
                mid = (nums[len(nums)//2] + nums[len(nums)//2-1])/2

            return mid

        if nums1 != [] and nums2 != []:
            nums1.extend(nums2)
            nums1.sort()
            return getMedian(nums1)

        elif nums1 == [] and nums2 != []:
            return getMedian(nums2)

        elif nums1 != [] and nums2 == []:
            return getMedian(nums1)

        else:
            return 0


            
