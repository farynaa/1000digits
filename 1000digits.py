# to simplify input procedure
def input_digits(fname):
	with open(fname) as fin:
		return [int(el) for el in fin.read() if el.isdigit()]

# let's define very helpful list multiplication function 
def multiply_list(l):
	m = 1
	for i in l: m *= i
	return m

def solve(l):
	mps = [multiply_list(l[i:i+13]) for i in range(len(l)-12)]
	value = sorted(mps)[-1]
	ndx = mps.index(value)
	digits = l[ndx:ndx+13]
	return digits, value

if __name__ == '__main__':
	s = input_digits('input.txt')
	d, v = solve(s)
	print('13 adjacent digits having greatest product are: ', ''.join(map(str,d)))
	print('and the value of this product is: ', v)
	