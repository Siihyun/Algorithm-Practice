a = ['1','2','3','4','5']

d = dict()
d['cola'] = 3
d['aer'] = 5
d['bear'] = 1


print(sorted(d,key=lambda x: d[x],reverse=True))