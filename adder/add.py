#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)

#GPIO.setup(26,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#print(GPIO.input(26))

#GPIO.setup(24,GPIO.OUT)
#GPIO.output(24,1)
#GPIO.output(24,0)

#GPIO.cleanup()

num1 = int(input("First number to be added:"))
num2 = int(input("Second number to be added:"))

binnum1 = bin(num1)
binnum2 = bin(num2)

def bitlength(binnum):
	binary = binnum[2:]
	return len(binary)

if bitlength(binnum1) >= bitlength(binnum2):
	wordlength = bitlength(binnum1)
else:
	wordlength = bitlength(binnum2)

binlist1 = [int(i) for i in list('{0:0b}'.format(num1))]
binlist2 = [int(i) for i in list('{0:0b}'.format(num2))]

def samelength(binlist):
	while len(binlist) < wordlength:
		binlist.insert(0,0)

samelength(binlist1)
samelength(binlist2)

print(binlist1)
print(binlist2)

carry = 0

result = []

#while wordlength > 0:
	bit1 = binlist1.pop()
	bit2 = binlist2.pop()
	
	if carry:
		GPIO.output(23,1)
	else:
		GPIO.output(23,0)

	if bit1:
		GPIO.output(24,1)
	else:
		GPIO.output(24,0)

	if bit2:
		GPIO.output(23,1)
	else:
		GPIO.output(23,0)

	time.sleep(0.01)

	result.append(GPIO.input(26))
	carry = GPIO.input(27)

result.insert(0,carry)

count = 0
summ = 0

while len(result) > 0:
	if result.pop():
		summ += 2**count
	count++

print(f"\nThe sum is: {summ}")
	



