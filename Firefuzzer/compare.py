import sys
import difflib as diff

def compare(a,b):
    s = diff.SequenceMatcher(None,a,b)
    d = diff.Differ()
    print a.split(),b.split()
    result = list(d.compare(a.split(),b.split()))
    pp.pprint(result)
    print s.ratio()
    print s.real_quick_ratio()
    #print 'Fuzzy:',fuzz.ratio(b,a),fuzz.partial_ratio(b,a)
    #print fuzz.token_sort_ratio(a,b)
    
def similar(a,b):
    a = a.split()
    b = b.split()
    d = diff.Differ()
    result = list(d.compare(a,b))
    #print result
    same = 0.0
    total_len = 0.0
    for k in result:
        if k[0] == '?':
            continue
        total_len += len(k)-2
        if k[0] == ' ':
            same += len(k)-2
    #print same,total_len
    return same/total_len

inputs = ['login','password','tel','email','url','week','month','date','time','datetime','datetime_local','number','range','color']
ans = {}
option = {}
ans['login'] = 'Account is valid!!'
option['login'] = ['Please do not leave the account empty!!','Your account must contain at least one number!!','Your account must contain at least one letter!!','Account is too short or inlcudes invalid chars!!','Account is too long or includes invalid chars!!','The account includes invaid chars!!']

ans['password'] = 'Password is valid!!'
option['password'] = ['Please do not leave the password empty!!','Your password must contain at least one number!!','Your password must contain at least one letter!!','Password is too short or inlcudes invalid chars!!','Password is too long or includes invalid chars!!','The password includes invaid chars!!']

ans['tel'] = 'The phone number * is valid!!'
option['tel'] = ['You leave the phone number empty!!','The phone number - is invalid!!']

ans['email'] = '* is a valid email address!!'
option['email'] = ['You leave the email empty!!','- is not a valid email address!!']

ans['url'] = '* is a valid URL!!'
option['url'] = ['You leave the URL empty!!','- is not a valid URL!!']

ans['week'] = 'Week is valid!!'
option['week'] = ['You leave the week empty!!','Week is invalid']

ans['month'] = 'Month is valid!!'
option['month'] = ['You leave the month empty!!','Month is invalid']

ans['date'] = 'Date is valid!!'
option['date'] = ['You leave the date empty!!','Date is invalid']

ans['time'] = 'Time is valid!!'
option['time'] = ['You leave the time empty!!','Time is invalid']

ans['datetime'] = 'Datetime : *'
option['datetime'] = ['Datetime : -']

ans['datetime_local'] = 'Datetime-local is valid!!'
option['datetime_local'] = ['You leave the datetime-local empty!!','Datetime-local is invalid!!']

ans['number'] = 'Number is valid!!'
option['number'] = ['You leave the number empty!!','Number is invalid!!']

ans['range'] = 'Range is valid!!'
option['range'] = ['You leave the range empty!!','Range is invalid!!']

ans['color'] = 'Color is valid!!'
option['color'] = ['You leave the color empty!!','Color is invalid!!']

max = 0.0
for k in inputs:
    print ''
    print k,':',ans[k]
    for v in option[k]:
        print v,similar(ans[k],v),similar(v,ans[k])
