
# m = monedas
# me = mesas
m, me = map(int, input("Enter m and me: ").split())
mo = []
me2=[]

for i in range(m):
    mo.append(int(input()))
for i in range(me):
    me2.append(int(input()))

# Now, mo contains the input values
print("monedas:", mo)
print("mesas:", me2)



