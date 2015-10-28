from sulley import *

import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits
limit_num_af = 'abcdef' + string.digits
limit_num_AF = 'ABCDEF' + string.digits
limit_num_az = string.digits + string.ascii_lowercase
limit_num_AZ = string.digits + string.ascii_uppercase
limit_num_afAF = 'abcdefABCDEF' + string.digits

def num_af(a,b):
    s_limit_random(value="", min_length = a, max_length = b, num_mutations = 1, limit_values=limit_num_af)

def num_AF(a,b):
    s_limit_random(value="", min_length = a, max_length = b, num_mutations = 1, limit_values=limit_num_af)

def num_az(a,b):
    s_limit_random(value="", min_length = a, max_length = b, num_mutations = 1, limit_values=limit_num_az)

def num_AZ(a,b):
    s_limit_random(value="", min_length = a, max_length = b, num_mutations = 1, limit_values=limit_num_AZ)

def num_afAF(a,b):
    s_limit_random(value="", min_length = a, max_length = b, num_mutations = 1, limit_values=limit_num_afAF)

# Color
s_initialize("Color_001")
s_limit_random(value="", min_length = 0, max_length = 0, num_mutations = 1, limit_values=limit_num_afAF)
s_static('#')


s_initialize("Color_002")
s_static('#')
num_af(6,6)

s_initialize("Color_003")
s_static('#')
num_af(1,5)

s_initialize("Color_004")
s_static('#')
num_af(7,100)

s_initialize("Color_005")
s_static('#')
num_AF(6,6)

s_initialize("Color_006")
s_static('#')
num_AF(1,5)

s_initialize("Color_007")
s_static('#')
num_AF(7,100)

s_initialize("Color_008")
s_static('#')
num_az(6,6)

s_initialize("Color_009")
s_static('#')
num_az(1,5)

s_initialize("Color_010")
s_static('#')
num_az(7,100)

s_initialize("Color_011")
s_static('#')
num_AZ(6,6)

s_initialize("Color_012")
s_static('#')
num_AZ(1,5)

s_initialize("Color_013")
s_static('#')
num_AZ(7,100)

s_initialize("Color_014")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='#')
num_af(6,6)

s_initialize("Color_015")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='#')
num_af(1,5)

s_initialize("Color_016")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='#')
num_af(7,100)

s_initialize("Color_017")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='#')
num_AF(6,6)

s_initialize("Color_018")
s_static('@')
num_AF(6,6)

s_initialize("Color_019")
s_static('@')
num_af(6,6)

s_initialize("Color_020")
s_static('#')
num_AF(6,6)

s_initialize("Color_021")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='#')
num_AF(1,5)

s_initialize("Color_022")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='#')
num_AF(7,100)

s_initialize("Color_023")
num_af(6,6)

s_initialize("Color_024")
num_af(0,5)

s_initialize("Color_025")
num_af(7,100)

s_initialize("Color_026")
num_AF(6,6)

s_initialize("Color_027")
num_AF(0,5)

s_initialize("Color_028")
num_AF(7,100)

s_initialize("Color_029")
num_az(6,6)

s_initialize("Color_030")
num_az(0,5)

s_initialize("Color_031")
num_az(7,100)

s_initialize("Color_032")
num_AZ(6,6)

s_initialize("Color_033")
num_AZ(0,5)

s_initialize("Color_034")
num_AZ(7,100)

s_initialize("Color_035")
s_static('#')
num_afAF(1,5)

s_initialize("Color_036")
s_static('#')
num_afAF(6,6)

s_initialize("Color_037")
s_static('#')
num_afAF(7,100)

s_initialize("Color_038")
num_afAF(1,5)

s_initialize("Color_039")
num_afAF(6,6)

s_initialize("Color_040")
num_afAF(7,100)

