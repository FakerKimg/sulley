from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

for i in range(1, 3):
    # Text
    # Text - Number
    for j in range(1, 3):
        s_initialize("Text_001" + str(i) + str(j))
        s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.digits)
        s_initialize("Text_002" + str(i) + str(j))
        s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.digits)
        s_initialize("Text_003" + str(i) + str(j))
        s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.digits)

    # Text - Alpha
    for j in range(1, 3):
        s_initialize("Text_004" + str(i) + str(j))
        s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.ascii_letters)
        s_initialize("Text_005" + str(i) + str(j))
        s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.ascii_letters)
    s_initialize("Text_006" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.ascii_letters)

    # Text - Alpha and number
    s_initialize("Text_007" + str(i))
    s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num)
    s_initialize("Text_008" + str(i))
    s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num)
    s_initialize("Text_009" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

    # Text - Space
    s_initialize("Text_010" + str(i))
    s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=' ')
    s_initialize("Text_011" + str(i))
    s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=' ')
    s_initialize("Text_012" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=' ')

    # Text - Mix
    s_initialize("Text_013" + str(i))
    s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
    s_initialize("Text_014" + str(i))
    s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
    s_initialize("Text_015" + str(i))
    s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')

