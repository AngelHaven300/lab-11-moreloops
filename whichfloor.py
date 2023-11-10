maximumstories = 60 
usernum = int(input("On what floor of the building is your office?"))

while usernum > maximumstories:
    print("you entered:" + str(usernum) + " but there are only" + " " + str(maximumstories) + " floors in this building. Try again...")
    usernum = int(input("On what floor of the building is your office?"))

print("Congrats! You work on floor number: " + str(usernum))