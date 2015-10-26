from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

# Range
s_initialize("Range_001")
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=string.digits)

s_initialize("Range_002")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')

s_initialize("Range_003")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='.')

s_initialize("Range_004")
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')
s_static('00.')
s_limit_random(value="", min_length = 2, max_length = 2, num_mutations = 1, limit_values='123456789')

s_initialize("Range_005")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')

s_initialize("Range_006")
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')
s_static('0')

s_initialize("Range_007")
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values='123456789')
s_static('00')

s_initialize("Range_008")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
s_static('00')

s_initialize("Range_009")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=string.ascii_letters)

s_initialize("Range_010")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

