from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

# Password
# Password - Number
s_initialize("Password_001")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.digits)
s_initialize("Password_002")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.digits)
s_initialize("Password_003")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.digits)

# Password - Alpha
s_initialize("Password_004")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.ascii_letters)
s_initialize("Password_005")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.ascii_letters)
s_initialize("Password_006")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.ascii_letters)

# Password - Alpha and number
s_initialize("Password_007")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num)
s_initialize("Password_008")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num)
s_initialize("Password_009")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

# Password - Space
s_initialize("Password_010")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=' ')
s_initialize("Password_011")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=' ')
s_initialize("Password_012")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=' ')

# Password - Mix
s_initialize("Password_013")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
s_initialize("Password_014")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
s_initialize("Password_015")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')

