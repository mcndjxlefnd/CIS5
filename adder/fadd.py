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

sum_reg_A = []
sum_reg_B = []
