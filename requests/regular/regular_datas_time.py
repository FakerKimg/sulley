from sulley import *

import string
import random

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

def hour():
    r = random.randint(1,3)
    if r == 1:
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='01')
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')
    else:
        s_static('2')
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='01234')

def hour2():
    r = random.randint(1,3)
    if r == 1:
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='01')
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='0123456789')
    else:
        s_static('2')
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='01234')

def minute():
    r = random.randint(1,3)
    if r == 1:
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='012345')
        s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='0123456789')
    else:
        s_static('60')

# Time
s_initialize("Time_001")
hour()
s_static(':')
minute()

s_initialize("Time_002")
hour()
s_limit_random(value="", min_length = 2, max_length = 100, num_mutations = 1, limit_values=':')
minute()

s_initialize("Time_003")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0')
hour()
s_static(':')
minute()

s_initialize("Time_004")
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')
s_static(':')
minute()

s_initialize("Time_005")
s_limit_random(value="", min_length = 3, max_length = 100, num_mutations = 1, limit_values='123456789')
s_static(':')
minute()

s_initialize("Time_006")
hour2()
s_static(':')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0')
if random.randint(1,3)==1:
    s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='12345')
    s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')
else:
    s_static('60')

s_initialize("Time_007")
hour2()
s_static(':')
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')

s_initialize("Time_008")
hour2()
s_static(':')
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='6789')
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')

s_initialize("Time_009")
hour2()
s_static(':')
s_limit_random(value="", min_length = 3, max_length = 100, num_mutations = 1, limit_values='123456789')

s_initialize("Time_010")
hour()
s_static(':60')

s_initialize("Time_011")
hour()
s_static(':60')
for i in range(random.randint(0,11)):
    s_static(':')
    s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='012345')
    s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='0123456789')

s_initialize("Time_012")
hour()
s_static(':')
s_limit_random(value="", min_length = 2, max_length = 2, num_mutations = 1, limit_values=string.letters)

s_initialize("Time_013")
s_limit_random(value="", min_length = 2, max_length = 2, num_mutations = 1, limit_values=string.letters)
s_static(':')
minute()

