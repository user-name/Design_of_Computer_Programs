import re
import timeit

my_list = ['abc-123', 'def-456', 'ghi-789', 'abc456', 'abd']
my_exp = re.compile('^abc$')

def gen_list():
    return [''.join(i.split()) for i in my_list]

def simple_check():
    new_list = gen_list()
    return [i for i in new_list if i=='abc']

t = timeit.Timer(simple_check)
print 'simple_check result >>', simple_check()
print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)

def re_check():
    new_list = gen_list()
    return [i for i in new_list if my_exp.match(i)]

t = timeit.Timer(re_check)
print 're_check result >>', re_check()
print "%.2f usec/pass" % (1000000 * t.timeit(number=100000)/100000)