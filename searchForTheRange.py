from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lrange = 2*[]
        
        def binarySearchStart(l: int, r: int) -> int:
            if r < l:
                return -1

            elif l == r:
                return l

            else:
                mid = (l + r)//2
                print('mid is ' + str(mid))
                print('when mid is ' + str(nums[mid]))

                if nums[mid] == target and (mid - 1 < 0 or nums[mid - 1] != target):
                    print('target is found')
                    return mid
                
                if nums[mid] < target:
                    print('mid is smaller than target, search to the left')
                    return binarySearchStart(mid, r)
                else:
                    print('mid is smaller than target, search to the right')
                    return binarySearchStart(l, mid)
        
        def binarySearchEnd(l: int, r: int) -> int:
            if r < l:
                return -1
            
            elif l == r:
                return l

            mid = (l + r) // 2
            
            if nums[mid] == target and (mid + 1 >= len(nums) or nums[mid + 1] != target):
                return mid
            if nums[mid] <= target:
                return binarySearchEnd(mid, r)
            else:
                return binarySearchEnd(l, mid)
            
        lrange.append(binarySearchStart(0, len(nums) - 1))
        lrange.append(binarySearchEnd(0, len(nums) - 1))

        return lrange

sol = Solution()
nums = [1,2,2,2,2,2,4,5,6,8]
print('Length is ' + str(len(nums)))
target = 13
print(sol.searchRange(nums,target))