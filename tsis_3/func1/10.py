def unique(nums: list):
    new_nums = list()
    for i in nums:
        if i not in new_nums:
            new_nums.append(i)
    print(new_nums)



unique([1, 1, 3, 4, 5, 6, 5])