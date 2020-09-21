# defaultdict is like a normal dictionary. The only difference is when
#  you  try to access a key that doesn't exist - defaultdict will create
# that key for you, instead of raising an error
import collections

nums = [1, 2, 3]
names = ["one", "two", "three"]

normal_dict = dict()
default_dict = collections.defaultdict(int)

for num in nums:
    # normal_dict[num] # uncomment and see how it throws a KeyError
    default_dict[num]

print(f"{normal_dict=}")
print(f"{default_dict=}")
