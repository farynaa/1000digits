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
	# first, we need to get the products of chunks
	mps = [multiply_list(l[i:i+13]) for i in range(len(l)-12)]
	# sorting and getting largest product
	value = sorted(mps)[-1]
	# find for largest product the index of first digit in input
	ndx = mps.index(value)
	# extracting digits
	digits = l[ndx:ndx+13]
	return digits, value

if __name__ == '__main__':
	s = input_digits('input.txt')
	# the solution is rather slow on large input
	#s = s * 10000
	
	d, v = solve(s)
	print('13 adjacent digits having greatest product are: ', ''.join(map(str,d)))
	print('and the value of this product is: ', v)
	