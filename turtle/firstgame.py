import time
import random
import turtle

print("Press enter when you see the text.")

gameover = 0
total = 0
n = 0
best = 0
window = turtle.Screen()

while gameover == 0:
    david = turtle.Turtle()
    n = n + 1
    if gameover == 1:
        break
    
    time.sleep(random.randint(3,7))

    start_time = time.time()

    reaction = input("press enter now!")

    end_time = time.time()

    reaction_time = end_time - start_time

    print("Your reaction time was", round(reaction_time,3), "seconds.")
    
    total = total + reaction_time
    ave = round(total / n,3)
    
    print("Your average score is", ave, "seconds in", n,"times.")

    if best == 0:
        best = reaction_time

    else:
        if reaction_time >= best:
            pass

        elif reaction_time < best:
            best = reaction_time

    print("Your best score is",round(best,3) ,"seconds.")

    a = (input("do you want to play again?(y/n)"))

    if a == "n":
        gameover = 1

    elif a == "y":
        gameover = 0   
    
    else:
        print("Invalid input!")
        break
    turtle.clear()
print("Game over!")
