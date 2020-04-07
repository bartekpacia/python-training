class Solution:

    def pick_largest_smaller_than(self, largest_num: int, s: str):
        largest = "/"
        for char in s:
            if ord(char) > ord(largest) and ord(char) < largest_num:
                largest = char

        return largest if largest != "/" else None

    def pick_smallest_greater_than(self, lower_num: int, s: str):
        smallest = "ź"
        for char in s:
            if ord(char) < ord(smallest) and ord(char) > lower_num:
                smallest = char

        return smallest if smallest != "ź" else None

    def sortString(self, s: str) -> str:
        result = ""

        smallest = "ź"
        for char in s:
            if ord(char) < ord(smallest):
                smallest = char

        result += smallest

        for char in s:
            smallest = self.pick_smallest_greater_than(ord(smallest), s)
            if not smallest:
                break
            result += smallest

        largest = "/"
        for char in s:
            if ord(char) > ord(largest):
                largest = char

        result += largest

        for char in s:
            largest = self.pick_largest_smaller_than(ord(largest), s)
            if not largest:
                break
            result += largest

        return result


solution = Solution()
print(solution.sortString("aaaabbbbcccc"))
