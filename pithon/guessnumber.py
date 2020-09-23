#from gpiozero import LED

#red = LED(0)
#yellow = LED(1)
#lgreen = LED(2)

from random import randint

number = randint(0,99)
print(number)

guess = -1

while (guess != number):
	guess = int(input("Guess an integer from 0 to 99:"))
	if guess < number:
		
		print("Guess is too low, try again.")
	

	else:
		print("Guess is too high, try again.")



#green.on()
#time.sleep(0.5)
#green.off()

print(f"Congratulations! {number} is the correct guess!")



