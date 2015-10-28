from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

for i in range(1, 3):
    # Password
    # Password - Number
    for j in range(1, 3):
        s_initialize("Password_001" + str(i) + str(j))
        s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.digits)
        s_initialize("Password_002" + str(i) + str(j))
        s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.digits)
        s_initialize("Password_003" + str(i) + str(j))
        s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.digits)

    # Password - Alpha
    for j in range(1, 3):
        s_initialize("Password_004" + str(i) + str(j))
        s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.ascii_letters)
        s_initialize("Password_005" + str(i) + str(j))
        s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.ascii_letters)
    s_initialize("Password_006" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.ascii_letters)

    # Password - Alpha and number
    s_initialize("Password_007" + str(i))
    s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num)
    s_initialize("Password_008" + str(i))
    s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num)
    s_initialize("Password_009" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

    # Password - Space
    s_initialize("Password_010" + str(i))
    s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=' ')
    s_initialize("Password_011" + str(i))
    s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=' ')
    s_initialize("Password_012" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=' ')

    # Password - Mix
    s_initialize("Password_013" + str(i))
    s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
    s_initialize("Password_014" + str(i))
    s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
    s_initialize("Password_015" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')

