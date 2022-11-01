#Runtime O(log n + K)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #if x is less than first val of array, return up to k
        if x <= arr[0]: 
            return arr[:k]
        
        #if x is greater than last value array, return last k values of array
        if x >= arr[-1]:
            return arr[-k:]

        left = 0
        right = len(arr) - k # max start point
        
        while left < right:
            mid = left + (right - left) // 2

            # mid + k is closer to x, discard mid by assigning left = mid + 1
            if arr[mid + k] - x < x - arr[mid]:
                left = mid + 1

            # mid is equal or closer to x than mid + k, mid remains as candidate
            else:
                right = mid

        # left == right, which makes both left and left + k have same diff with x
        return arr[left : left + k]