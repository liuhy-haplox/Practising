#Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
#Type "copyright", "credits" or "license()" for more information.
nums = [1,8,2,23,7,-4,18,23,2,1,37]
import heapq
print heapq.heapify(nums)
#nums
#[-4, 1, 1, 2, 7, 2, 18, 23, 23, 8, 37]
print heapq.heappop(nums)
#-4
print heapq.heappop(nums)
#
print heapq.heappop(nums)
