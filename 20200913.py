from type import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        no_duplicate_list =[]

        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)

        return no_duplicate_list.pop()

    def singleNumber2(self, nums: List[int]) -> int:

        no_duplicate_set = set()

        for i in nums:
            if i not in no_duplicate_set:
                no_duplicate_set.add(i)

            else:
                no_duplicate_set.remove(i)

        return no_duplicate_set.pop()

S = Solution()

test_list = [1,2,2]
print(S.singleNumber2(test_list))

test_list2 = [4,2,2,1,1]

print(S.singleNumber2(test_list2))
