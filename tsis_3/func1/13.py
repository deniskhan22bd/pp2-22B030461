import random

num = random.randrange(1, 20)
print(num)
name = input("Hello! What is your name? ")
print("Well, {}, I am thinking of a number between 1 and 20".format(name))
cnt = 1
while True:
    print("Take a guess.")
    user_num = int(input())
    if(user_num == num):
        print("Good job, KBTU! You guessed my number in {} guesses!".format(cnt))
        break
    elif(user_num > num):
        cnt += 1
        print("Your guess is too high")
    else:
        cnt += 1
        print("Your guess is too low")
