# Dynamic programming

+ [House Robber II](#house-robber-ii)

## House Robber II

https://leetcode.com/problems/house-robber-ii/

``` python
def rob_1(self, nums: List[int]) -> int:
    length = len(nums)
    if length == 0:
        return 0
    elif length == 1:
        return nums[0]
    elif length == 2:
        return max(nums)
    else:
        summ = [0]*length # assign dp array
        summ[0], summ[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, length):
            summ[i] = max(summ[i-1], summ[i-2]+nums[i])
        return max(summ)


def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:-1]))
```
