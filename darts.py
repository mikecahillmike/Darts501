# Darts training 

# Delaring 501 variables
remaining = 501
avg = 0.0
avg100 = 0.0
thrown = 0
totalScored = 0
scored = 0
lastScored = 0

print("Game Started!")
while True:
    print("Last Scored: " + str(lastScored))
    print("Average: {:.2f}".format(avg))
    scored = int(input("Enter total score from your 3 darts"))
    if 0 <= scored < 180:
        if scored <= remaining:
            remaining -= scored
            lastScored = scored
            # Average
            thrown += 3
            totalScored += scored
            avg = totalScored / thrown
            if remaining == 0:
                break
            print("Remaining: " + str(remaining))
        else:
            print("Invailed Score! Exceeded Checkout")
    else:
        print("Invailed Score!")

print("Game Over! Congrats")
print("Average score per dart: {:.2f}".format(avg))
            





