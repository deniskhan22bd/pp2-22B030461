def histogram(nums: list):
    for i in nums:
        for j in range(i):
            print("*",end="")
        print()
    
histogram([4, 9, 7])