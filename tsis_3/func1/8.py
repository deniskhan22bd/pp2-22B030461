def spy_game(nums: list):
    cnt = 0
    for i in nums:
        if i == 0:
            cnt += 1
        elif i == 7 and cnt >= 2:
            return True
        elif i == 7:
            cnt = 0
    return False


print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
print(spy_game([0, 7, 0, 1, 0, 7]))