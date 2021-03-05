try:
    # first we read the age as characheters
    age = input("how old are you?")
    # we try to convert the age to the number
    age = int(age)

except ValueError:
    print ("Sorry, but that was not a number")
except:
    print("you were born around", 2021 - age)
finally:
    print("Thanks for playing my game")














