from sulley import *

import string

limit_values = ""
limit_values = limit_values + string.ascii_letters
limit_values = limit_values + string.digits

# equal to '[a-zA-Z0-9]{0,6}'
s_initialize("regular data example 000")
s_limit_random(value="", min_length = 0, max_length = 6, num_mutations = 5, limit_values=limit_values)


