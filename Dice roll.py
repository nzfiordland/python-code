# this is a comment
import random
min = 1
max = 6
total_two = 0
total_three = 0
total_seven = 0

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    firstroll = random.randint(min, max)
    secondroll = random.randint(min, max)
    print(firstroll)
    print(secondroll)
    sum = firstroll + secondroll
    print(sum)
    if sum == 7:
        total_seven = total_seven + 1
    print(total_seven)

    roll_again = input("Roll the dices again?")
