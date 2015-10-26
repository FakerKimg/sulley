from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

# Text
# Text - Number
s_initialize("Text_001")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.digits)
s_initialize("Text_002")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.digits)
s_initialize("Text_003")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.digits)

# Text - Alpha
s_initialize("Text_004")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=string.ascii_letters)
s_initialize("Text_005")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=string.ascii_letters)
s_initialize("Text_006")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=string.ascii_letters)

# Text - Alpha and number
s_initialize("Text_007")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num)
s_initialize("Text_008")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num)
s_initialize("Text_009")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)

# Text - Space
s_initialize("Text_010")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=' ')
s_initialize("Text_011")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=' ')
s_initialize("Text_012")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=' ')

# Text - Mix
s_initialize("Text_013")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
s_initialize("Text_014")
s_limit_random(value="", min_length = 6, max_length = 17, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')
s_initialize("Text_015")
s_limit_random(value="", min_length = 17, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num+' '+'_')

