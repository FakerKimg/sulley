from sulley import *
import random
import string

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits

def alpha_1dot():
    r = random.randint(0,11,)
    for i in range(r):
        s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
        s_static('.')
def alpha_dots():
    r = random.randint(0,11,)
    for i in range(r):
        s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values=limit_alpha_num)
        s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='.')

def dot_num():
    r = random.randint(0,11)
    for i in range(r):
        s_static('.')
        s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
# url
s_initialize("Url_001")
s_static('www.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_002")
s_static('www')
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_003")
s_static('www.')
alpha_dots()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_004")
s_static('www')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values='w')
s_static('.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_005")
s_static('httpwww.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_006")
s_static('http:www.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_007")
s_static('http:/www.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_008")
s_static('http://')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values='/')
s_static('www.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_009")
s_static('http:www')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values='w')
s_static('.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_010")
s_static('ftp:www.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_011")
s_static('ftp:/www.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_012")
s_static('ftp://')
s_limit_random(value="", min_length = 0, max_length = 100, num_mutations = 1, limit_values='/')
s_static('.')
alpha_1dot()
s_limit_random(value="", min_length = 1, max_length = 1, num_mutations = 1, limit_values=limit_alpha_num)

s_initialize("Url_013")
s_limit_random(value="", min_length = 1, max_length = 100, num_mutations = 1, limit_values='123456789')
dot_num()







