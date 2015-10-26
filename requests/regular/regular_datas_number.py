from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

# Number
s_initialize("Number_001")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')

s_initialize("Number_002")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdef')

s_initialize("Number_003")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789ABCDEF')

s_initialize("Number_004")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdefABCDEF')

s_initialize("Number_005")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
s_static('.')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0123456789')

s_initialize("Number_006")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
s_static('.')

s_initialize("Number_007")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='.')

s_initialize("Number_008")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdef')
s_static('.')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdef')

s_initialize("Number_009")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
s_static('.')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0123456789')

s_initialize("Number_010")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789'+string.ascii_lowercase)
