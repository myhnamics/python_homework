# 8.1
e2f = {'dog':'chien', 'cat':'chat','walrus':'morse'}

# 8.2
print(e2f['walrus'])

# 8.3
# key = [list(e2f.items())[i][1] for i in range(0,3)]
# value = [list(e2f.items())[i][0] for i in range(0,3)]
f2e = {f:e for (e,f) in e2f.items()}
print(f2e)

# 8.4
print([e for e,f in e2f.items() if f == 'chien'])

# 8.5
print(e2f.keys())

# 8.6
life = {'animals':{'cats':'Henri','octopi':'Grumpy','emus':'Lucy'},'plants':{},'other':{}}

# 8.7
print(life.keys())
# 8.8
print(life['animals'].keys())
# 8.9
print(life['animals']['cats'])
# 8.10
squres = {x:x*x for x in range(10)}
print(squres)
# 8.11
odd_set = {i for i in range(10) if i % 2 == 1}
print(odd_set)
# 8.12
abc = (pair for pair in zip('Get',range(10)))
for thing in abc:
    print(thing)
# 8.13
key = ('optimist','pessimist','troll')
val = ('The glass is half full','The glass is half empty','How did you geet a glass?')
jip = dict(zip(key,val))
print(jip)

# 8.14
titles = ['Creature of Habit','Crewel Fate']
plots = ['A non turns into a mon ster','A haunted yarn shop']
movies = dict(zip(titles,plots))
print(movies)