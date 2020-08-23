# HoT: Initial revision
import random
def toss_coin():
    print("Tossing a coin...")
    count = 0
    for i in range(1,4):
        print("Round",i ,":",end='')
        judge = random.randint(0,1)
        if judge == 1:
            print("Head")
            count += 1
        else:
            print("Tail")
    print("Heads:",count,"Tails:",3 - count)
    return count
