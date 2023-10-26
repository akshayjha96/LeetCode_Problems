'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.'''


## SOLUTION 1 ##
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        element_occurances = defaultdict(int)
        for i,n in enumerate(nums):

            element_occurances[n] += 1

        reverse_sorted = sorted(list(element_occurances.values()),reverse=True)[:k]
        print(reverse_sorted)
        #keys_with_target_values = [key for key, value in my_dict.items() if value in target_values]
        keys_with_highest_occurances = [key for key,value in element_occurances.items() if value in reverse_sorted]
        return     keys_with_highest_occurances
## SOLUTION 2 ##
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #value: counts
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            count[n] = 1+ count.get(n,0)
        
        for n,c in count.items():
            freq[c].append(n)
        res = []
        
        for i in range(len(freq) -1, 0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
##O(n)
