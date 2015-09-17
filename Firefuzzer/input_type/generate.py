import exrex
import os
type_list = ['text','password','tel','email','url','date','time','number','range','color']
#type_list = ['number']
fout = {}
for k in type_list:
    fout[k] = open(k,'w')

def getone(regular):
    return exrex.getone(regular) + '\n'

#Type:text
text = []
#text.append('15\n')
#number
text.append(getone('\d{0,6}'))
text.append(getone('\d{6,17}'))
text.append(getone('\d{17,}'))

#alpha
text.append(getone('[a-zA-Z]{0,6}'))
text.append(getone('[a-zA-Z]{6,17}'))
text.append(getone('[a-zA-Z]{17,}'))

#alpha and number
text.append(getone('[a-zA-Z0-9]{0,6}')) 
text.append(getone('[a-zA-Z0-9]{6,17}'))
text.append(getone('[a-zA-Z0-9]{17,}'))

#space
text.append(getone('\s{0,6}'))
text.append(getone('\s{6,17}'))
text.append(getone('\s{17,}'))

#mix 
text.append(getone('(\s | [a-zA-Z0-9_]){0,6}'))
text.append(getone('(\s | [a-zA-Z0-9_]){6,17}'))
text.append(getone('(\s | [a-zA-Z0-9_]){17,}'))

fout['text'].write("".join(text))
fout['password'].write("".join(text))
##########################################
#Type:tel
tel = []
#tel.append('36\n')
#number only
tel.append(getone('[1-9]\d{0,8}'))
tel.append(getone('[1-9]\d{9}'))
tel.append(getone('[1-9]\d{10,}'))
tel.append(getone('0\d{0,8}'))
tel.append(getone('0\d{9}'))
tel.append(getone('0\d{10,}'))

#number with one division( - or space)
tel.append(getone('[1-9]\d{3}( |-)+\d{6}'))
tel.append(getone('0\d{3}( |-)+\d{6}'))
tel.append(getone('[1-9]\d{3}-\d{6}'))
tel.append(getone('0\d{3} \d{6}'))
tel.append(getone('[1-9]\d{3}-+\d{6}'))
tel.append(getone('0\d{3} +\d{6}'))

#number with two division
tel.append(getone('[1-9]\d{3}( |-)+\d{3}( |-)+\d{3}'))
tel.append(getone('0\d{3}( |-)+\d{3}( |-)+\d{3}'))
tel.append(getone('[1-9]\d{3}-\d{3}-\d{3}'))
tel.append(getone('0\d{3} \d{3} \d{3}'))
tel.append(getone('[1-9]\d{3} \d{3}-\d{3}'))
tel.append(getone('0\d{3} \d{3}-\d{3}'))
tel.append(getone('[1-9]\d{3}-\d{3} \d{3}'))
tel.append(getone('0\d{3}-\d{3} \d{3}'))
tel.append(getone('[1-9]\d{3}-+\d{3}-+\d{3}'))
tel.append(getone('0\d{3} +\d{3} +\d{3}'))

#wrong division position
tel.append(getone('0\d{2} \d{4} \d{3}'))
tel.append(getone('[1-9]\d{2} \d{4} \d{3}'))
tel.append(getone('0\d{2}-\d{4}-\d{3}'))
tel.append(getone('[1-9]\d{2}-\d{4}-\d{3}'))
tel.append(getone('0\d{2}-\d{4} \d{3}'))
tel.append(getone('[1-9]\d{2}-\d{4} \d{3}'))
tel.append(getone('0\d{2} \d{4}-\d{3}'))
tel.append(getone('[1-9]\d{2} \d{4}-\d{3}'))
tel.append(getone('[1-9]\d{2}( |-)+\d{4}( |-)+\d{3}'))
tel.append(getone('0\d{2}( |-)+\d{4}( |-)+\d{3}'))


#not number
tel.append(getone('[^0-9]{10}'))
tel.append(getone('([1-9])([^0-9]|\d){9}'))
tel.append(getone('0([^0-9]|\d){9}'))
tel.append(getone('[^0-9]\d{9}'))


fout['tel'].write("".join(tel))

##########################################
#Type:email
email = []
#email.append('3\n')
email.append(getone('[a-zA-Z0-9]*@[a-zA-Z0-9]*'))
email.append(getone('[a-zA-Z0-9]*@+[a-zA-Z0-9]*'))
email.append(getone('[_]*@[_]*'))
fout['email'].write("".join(email))

##########################################
#Type:url
url = []
#url.append('10\n')
url.append(getone('www\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('www\.*([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('www\.([a-zA-Z0-9]*\.*)*[a-zA-Z0-9]'))
url.append(getone('wwww*\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('httpwww\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('http:www\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('http:/www\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('http://*www\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('http:www*\.([a-zA-Z0-9]*\.)*[a-zA-Z0-9]'))
url.append(getone('[a-zA-Z0-9]*'))
fout['url'].write("".join(url))

##########################################
#Type:date
date = []
#date.append('31\n')
#correct
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
#year
date.append(getone('[1-9](/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('0+(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-9][0-9](/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('0+[1-9](/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-9][0-9]{2}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('0+[1-9]{2}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-9][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('0+[1-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('0+[1-9]*(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('(/| |-)([1-9]|1[0-2])(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-9]{5,}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))

#month
date.append(getone('[1-2][0-9]{3}(/| |-)(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)0+(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)[1-9](/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)0+[1-9](/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)1[0-2](/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)1[3-9](/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)[1-9]{2}(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)[1-9]{3,}(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|1[0-2])(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))

#day
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)(0+)'))
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)(0+[1-9])'))
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)(3[2-9])'))
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)([4-9][0-9])'))
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]{3,})'))

#middle term
date.append(getone('[1-2][0-9]{3}(/| |-){2,}([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-){2,}([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone('[1-2][0-9]{3}(/| |-){2,}([1-9]|(1[0-2]))(/| |-){2,}([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone(' +(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))
date.append(getone(' +[1-2][0-9]{3}(/| |-)([1-9]|(1[0-2]))(/| |-)([1-9]|([1-2][0-9])|(3[0-1]))'))

fout['date'].write("".join(date))
##########################################
#time
time = []
#time.append('10\n')
time.append(getone('(([0-1][1-9])|(2[0-4])):(([0-5][0-9])|(60))'))
time.append(getone('(([0-1][1-9])|(2[0-4])):{2,}(([0-5][0-9])|(60))'))
time.append(getone('(0+(([0-1][1-9])|(2[0-4])):(([0-5][0-9])|(60)))'))
time.append(getone('([1-9]):(([0-5][0-9])|(60))'))
time.append(getone('([1-9]{3,}):(([0-5][0-9])|(60))'))
time.append(getone('(([0-1][0-9])|(2[0-4])):(0+([1-5][1-9])|(60))'))
time.append(getone('(([0-1][0-9])|(2[0-4])):[1-9]'))
time.append(getone('(([0-1][0-9])|(2[0-4])):[6-9][1-9]'))
time.append(getone('(([0-1][0-9])|(2[0-4])):[1-9]{3,}'))
time.append(getone(':'))

fout['time'].write("".join(time))
##########################################
#number
number = []
#number.append('9\n')
number.append(getone('0+[1-9]+'))
number.append(getone('[1-9a-f]+'))
number.append(getone('[1-9A-F]+'))
number.append(getone('[1-9a-fA-F]+'))
number.append(getone('[1-9]+\.[0-9]+'))
number.append(getone('[1-9]+\.'))
number.append(getone('[1-9a-f]+\.[1-9a-f]+'))
number.append(getone('[1-9]+\.+[0-9]+'))
number.append(getone('[1-9a-z]+'))
fout['number'].write("".join(number))


##########################################
#Type:range
ranges = []
#ranges.append('8\n')
ranges.append(getone('[0-9]'))
ranges.append(getone('[1-9]*'))
ranges.append(getone('0+[1-9]*'))
ranges.append(getone('[1-9]0'))
ranges.append(getone('[1-9]00'))
ranges.append(getone('[1-9]+00'))
ranges.append(getone('[a-zA-Z]+'))
ranges.append(getone('[a-zA-Z0-9]+'))
fout['range'].write("".join(ranges))


##########################################
#Type:color
color = []
#color.append('25\n')
color.append(getone('#'))
color.append(getone('#[0-9a-f]{6}'))
color.append(getone('#[0-9a-f]{1,5}'))
color.append(getone('#[0-9a-f]{7,}'))
color.append(getone('#[0-9A-F]{6}'))
color.append(getone('#[0-9A-F]{1,5}'))
color.append(getone('#[0-9A-F]{7,}'))
color.append(getone('#[0-9a-z]{6}'))
color.append(getone('#[0-9a-z]{1,5}'))
color.append(getone('#[0-9a-z]{7,}'))
color.append(getone('#[0-9A-Z]{6}'))
color.append(getone('#[0-9A-Z]{1,5}'))
color.append(getone('#[0-9A-Z]{7,}'))
color.append(getone('[0-9a-f]{6}'))
color.append(getone('[0-9a-f]{0,5}'))
color.append(getone('[0-9a-f]{7,}'))
color.append(getone('[0-9A-F]{6}'))
color.append(getone('[0-9A-F]{0,5}'))
color.append(getone('[0-9A-F]{7,}'))
color.append(getone('[0-9a-z]{6}'))
color.append(getone('[0-9a-z]{0,5}'))
color.append(getone('[0-9a-z]{7,}'))
color.append(getone('[0-9A-Z]{6}'))
color.append(getone('[0-9A-Z]{0,5}'))
color.append(getone('[0-9A-Z]{7,}'))
fout['color'].write("".join(color))

    
