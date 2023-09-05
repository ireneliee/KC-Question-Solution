from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lrange = 2*[]
        
        def binarySearchStart(l: int, r: int) -> int:
            if r == l and target == nums[r]:
                return l
            
            elif l == r or l > r:
                return -1

            else:
                # print('l is ' + str(l))
                # print('r is ' + str(r))
                mid = (l + r)//2
                # print('mid is ' + str(mid))
                # print('when mid is ' + str(nums[mid]))

                if nums[mid] == target and (mid - 1 < 0 or nums[mid - 1] != target):
                    # print('target is found')
                    return mid
                
                if nums[mid] < target:
                    # print('target is bigger than mid, search to the rightt')
                    return binarySearchStart(mid + 1, r)
                else:
                    # print('target is smaller than mid, search to the left')
                    return binarySearchStart(l, mid -1)
        
        def binarySearchEnd(l: int, r: int) -> int:
            if r == l and target == nums[r]:
                return l
            
            elif l == r or r < l:
                return -1

            mid = (l + r) // 2
            
            if nums[mid] == target and (mid + 1 >= len(nums) or nums[mid + 1] != target):
                return mid
            if nums[mid] <= target:
                return binarySearchEnd(mid + 1, r)
            else:
                return binarySearchEnd(l, mid - 1)
            
        lrange.append(binarySearchStart(0, len(nums) - 1))
        lrange.append(binarySearchEnd(0, len(nums) - 1))

        return lrange

sol = Solution()
nums = [1,2,2,2,2,2,4,5,6,9,9]
# print('Length is ' + str(len(nums)))
target = 7
# print(sol.searchRange(nums,target))

# if number cant be found
# if number is at the last