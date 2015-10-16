from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

# Email
s_initialize("Email_001")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_static('@')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_002")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='@')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_003")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_static('@')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_static('@')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_004")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_limit_random(value="", min_length = 3, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num+'@')

s_initialize("Email_005")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_static('.')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_006")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=' ')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
s_static('@')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_007")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_008")
s_static('@')

s_initialize("Email_009")
s_static('@')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Email_010")
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values='_')
s_static('@')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values='_')

