from sulley import *

import string
import random

limit_alpha_num = ""
limit_alpha_num = limit_alpha_num + string.ascii_letters
limit_alpha_num = limit_alpha_num + string.digits
one_nine = '123456789'
def randoms(a,b,c):
    s_limit_random(value="", min_length = a, max_length = b, num_mutations = 1, limit_values=c)

def year():
    randoms(1,1,'12')
    randoms(3,3,string.digits)

def month():
    a = random.randint(1,2)
    if a == 1:
        randoms(1,1,one_nine)
    else:
        s_static('1')
        randoms(1,1,'012')

def day():
    a = random.randint(1,3)
    if a == 1:
        randoms(1,1,one_nine)
    elif a == 2:
        randoms(1,1,'12')
        randoms(1,1,one_nine)
    else:
        s_static('3')
        randoms(1,1,'01')

def between():
    a = random.randint(1,3)
    if a == 1:
        s_static('/')
    elif a == 2:
        s_static(' ')
    else:
        s_static('-')

def newone(mode):
    if mode == 1:
        between()
        month()
        between()
        day()
    elif mode == 2:
        year()
        between()
    elif mode == 3:
        between()
        day()
    else:
        year()
        between()
        month()

#date
##########################################
#Year's part

s_initialize('Date_001')
year()
newone(1)

s_initialize('Date_002')
randoms(1,1,one_nine)
newone(1)

s_initialize('Date_003')
randoms(1,100,'0')
newone(1)

s_initialize('Date_004')
randoms(1,1,one_nine)
randoms(1,1,string.digits)
newone(1)

s_initialize('Date_005')
randoms(1,100,'0')
randoms(1,1,one_nine)
newone(1)

s_initialize('Date_006')
randoms(1,1,one_nine)
randoms(2,2,string.digits)
newone(1)

s_initialize('Date_007')
randoms(1,100,'0')
randoms(2,2,one_nine)
newone(1)

s_initialize('Date_008')
randoms(1,1,one_nine)
randoms(3,3,string.digits)
newone(1)

s_initialize('Date_009')
randoms(1,100,'0')
randoms(3,3,one_nine)
newone(1)

s_initialize('Date_010')
randoms(1,100,'0')
randoms(4,100,one_nine)
newone(1)

s_initialize('Date_011')
newone(1)

s_initialize('Date_012')
randoms(5,100,one_nine)
newone(1)
##########################################
#Month's part

s_initialize('Date_013')
newone(2)
newone(3)

s_initialize('Date_014')
newone(2)
randoms(1,100,'0')
newone(3)

s_initialize('Date_015')
newone(2)
randoms(1,1,one_nine)
newone(3)

s_initialize('Date_016')
newone(2)
randoms(1,100,'0')
randoms(1,1,one_nine)
newone(3)

s_initialize('Date_017')
newone(2)
s_static('1')
randoms(1,1,'012')
newone(3)

s_initialize('Date_018')
newone(2)
s_static('1')
randoms(1,1,'3456789')
newone(3)

s_initialize('Date_019')
newone(2)
randoms(2,2,one_nine)
newone(3)

s_initialize('Date_020')
newone(2)
randoms(3,100,one_nine)
newone(3)

s_initialize('Date_021')
newone(2)
month()
newone(3)

##########################################
#Day's part

s_initialize('Date_022')
newone(4)
randoms(1,100,'0')

s_initialize('Date_023')
newone(4)
randoms(1,100,'0')
randoms(1,1,one_nine)

s_initialize('Date_024')
newone(4)
s_static('3')
randoms(1,1,'23456789')

s_initialize('Date_025')
newone(4)
randoms(1,1,'456789')
randoms(1,1,one_nine)


s_initialize('Date_026')
newone(4)
randoms(3,100,one_nine)

##########################################
#middle term

s_initialize('Date_027')
newone(2)
while True:
    a = random.randint(1,2)
    if a == 1:
        between()
    else:
        break
month()
newone(3)

s_initialize('Date_028')
newone(4)
while True:
    a = random.randint(1,2)
    if a == 1:
        between()
    else:
        break
day()

s_initialize('Date_029')
newone(2)
while True:
    a = random.randint(1,2)
    if a == 1:
        between()
    else:
        break
month()
while True:
    a = random.randint(1,2)
    if a == 1:
        between()
    else:
        break
newone(3)

s_initialize('Date_30')
randoms(1,100,' ')
newone(1)

s_initialize('Date_31')
randoms(1,100,' ')
year()
newone(1)

s_initialize('Date_32')
s_static(' / / ')

s_initialize('Date_33')
s_static(' ')
randoms(1,1,'-/')
s_static(' ')
randoms(1,1,'-/')
s_static(' ')

s_initialize('Date_34')
newone(4)
randoms(2,2,limit_alpha_num)

s_initialize('Date_35')
newone(2)
randoms(2,2,limit_alpha_num)
newone(3)

s_initialize('Date_36')
randoms(4,4,limit_alpha_num)
newone(1)

s_initialize('Date_37')
s_static('1')
randoms(3,3,string.ascii_letters)
newone(1)

s_initialize('Date_38')
randoms(1,100,' ')
year()
newone(1)

s_initialize('Date_39')
newone(2)
randoms(1,100,' ')
newone(1)

s_initialize('Date_40')
newone(4)
randoms(1,100,' ')
day()
