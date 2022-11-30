import json
import os

def exp ():
    global di
    if os.stat('database.json').st_size==0:
        di = {}
    else: di = json.load(open('database.json'))
    return di

def grade_exp(l):
    di = exp()
    k = '_'.join(l[0:4])
    if k in di.keys():
        print (' '.join(map(str,di[k][l[4]])))
    else: print('Ученик не найден в журнале')