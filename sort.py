boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
s_boys = sorted(boys)
s_girls = sorted(girls)
peoples = list(zip(s_boys, s_girls))
if len(s_girls) == len(s_boys):
    print('Идеальные пары:')
    for pepl in peoples:
        print(pepl[0] + ' и ' + pepl[1])
else:
    print('Внимание, кто-то может остаться без пары!')


