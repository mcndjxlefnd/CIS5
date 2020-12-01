high = 1
low = 0
source = high

def transistor (collector,base):
	if base:
		return collector
	else:
		return low

def gate_and (A,B):
	return transistor(transistor(source,A),B)

def gate_or (A,B):
	if transistor(source,A):
		return high
	elif transistor(source,B):
		return high
	else:
		return low

def gate_nand (A,B):
	if transistor(transistor(source,A),B):
		return low
	else:
		return high

def gate_xor (A,B):
	return gate_and(gate_nand(A,B),gate_or(A,B))

def full_adder (A,B,c_in):
	global summ, c_out
	summ = gate_xor(gate_xor(A,B),c_in)
	c_out = gate_or(gate_and(gate_xor(A,B),c_in),gate_and(A,B))

############################################################################################

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

c_in = 0
result = []

while wordlength > 0:
	bit1 = binlist1.pop()
	bit2 = binlist2.pop()
	
	full_adder(bit1,bit2,c_in)

	result.insert(0,summ)
	c_in = c_out
	wordlength = wordlength-1

result.insert(0,c_out)

count = 0
summ = 0

while len(result) > 0:
	if result.pop():
		summ += 2**count
	count = count+1

print(f"\nThe sum is: {summ}")
	



