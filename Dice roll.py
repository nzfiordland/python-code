import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    firstroll = random.randint(min, max)
    secondroll = random.randint(min, max)
    print(firstroll)
    print(secondroll)
    print('Total = ', firstroll + secondroll)

    roll_again = input("Roll the dices again?")