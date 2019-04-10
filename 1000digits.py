# to simplify input procedure
def input_digits(fname):
    with open(fname) as fin:
        return [int(el) for el in fin.read() if el.isdigit()]


# let's define very helpful list multiplication function 
def multiply_list(l):
    m = 1
    for i in l: m *= i
    return m


def solve(l,adjacent_digits=13):

    k = adjacent_digits # number of adjacent digits to product
    p = 0 # here we store the greates product
    digits = [] # and another one for the digits

    for i in range(0,len(l)- k + 1): # cutting input in chunks of giving size to calculate product of each
        if 0 not in l[i:i+k]: # just not to do calculations if there is zero in a chunk
            pt = multiply_list(l[i:i+k])
            # adjust greatest product if needed:
            if pt > p:
                p = pt 
                digits = l[i:i+k] # and remember the digits
        else:
            continue
    
    return ''.join(map(str,digits)), p


if __name__ == '__main__':
    
    s = input_digits('input.txt')
    d, v = solve(s)
    
    # shows reasonable perfomance even for large input
    #s = s * 100000
    
    print('13 adjacent digits having greatest product are: ', d)
    print('and the value of this product is: ', v)
    