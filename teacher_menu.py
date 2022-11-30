from imp import imp
from exp import exp

# Добавление ученика
def add_student(l):
    s = '_'.join(l)
    di = exp()
    di.setdefault(s,{})
    imp((di))
    return di

# Добавление оценок
def add_grade(l):
    if len(l)>6:
        print(f'Невозможно добавить более одной оценки за раз, будет добавлена только одна оценка по предмету {l[4]}')
    k = '_'.join(l[0:4])
    di = exp()
    if k in di:
        if l[5] in di:
            z = di[k][l[4]]
            o = z.append(l[5])
            (di[k]).setdefault(l[4],[]).append(o)
        else:
            (di[k]).setdefault(l[4],[]).append(l[5])
    else:
        di.setdefault(k,{})
        (di[k]).setdefault(l[4],[]).append(l[5])
    imp(di)
    return di