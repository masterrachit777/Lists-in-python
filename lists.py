x = ['anuj','aman','abhishek']
print(x)
print(x[1])
print(x[2])

pow2 = [2**x for x in range(10)]
print(pow2)

table = [y**2 for y in range(11) if y%2==0]
print(table)

#Lists methods
table.append(23)
print(table)
print(table[4])
table.append('Rachit')
print(table[7])
print(table[2:7:1])

table.insert(2,45)
print(table)
del table[8]
table.sort()
print(table)
table.pop(3)
print(table)
print(table.pop(4))
print(table)

numb = [4,7,5,1,4,2,6]
numb.reverse()
print(numb)
print(numb.index(1))
print(numb.count(4))

#Lists Functions
print(len(numb))
print(max(numb))
print(min(numb))
print(sum(numb))

#for loop in lists
for item in numb:
    print(item**2)
    
