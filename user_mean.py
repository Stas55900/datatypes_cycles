stream = [
    '2018-01-01,user1,3',
    '2018-01-07,user1,4',
    '2018-03-29,user1,1',
    '2018-04-04,user1,13',
    '2018-01-05,user2,7',
    '2018-06-14,user3,4',
    '2018-07-02,user3,10',
    '2018-03-21,user4,19',
    '2018-03-22,user4,4',
    '2018-04-22,user4,8',
    '2018-05-03,user4,9',
    '2018-05-11,user4,11',
]
ar = []
view_s = []
peoples = []
for item_s in stream:
    count = item_s.split(',')
    ar.append(count)
print(ar)
for num in ar:
    view_s.append(int(num[2]))
    peoples.append(num[1])
    set_people = set(peoples)
# print(set_people)
    if item == " ":
        del item
        numbers.append(item)