from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

for i in range(1, 5):
    # Number
    s_initialize("Number_001" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0')
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')

    s_initialize("Number_002" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdef')

    s_initialize("Number_003" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789ABCDEF')

    s_initialize("Number_004" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdefABCDEF')

    s_initialize("Number_005" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
    s_static('.')
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0123456789')

    s_initialize("Number_006" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
    s_static('.')

    s_initialize("Number_007" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='.')

    s_initialize("Number_008" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdef')
    s_static('.')
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789abcdef')

    s_initialize("Number_009" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
    s_static('.')
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='0123456789')

    s_initialize("Number_010" + str(i))
    s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789'+string.ascii_lowercase)
