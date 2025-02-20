# 1.explain about list (7examples)

#1
a=[1,2,3,4,5]
print(a)
print(type(a))


#2
b=['a','b','c','d']
print(b)


#3
c=[1.22,2.33,3.44,4.55]
print(c)


#4
d=[1j,3j,4j,9j]
print(d)


 #5
e=['vijay','naveen','murali','akhila','maheshwari',]
print(e)


#6
vijay=[1,2.3,'a','Vijay']
print(vijay)


#7
loc=[1,'vijay',22,'cse','khammam','21qp5a0514']
print(loc)


#Explain about index and slice (10examples)

#1
a=[1,2,3,4,5,6,7,8,9,0]
print(a)
print(a[2])
print(a[-9])
print(a[2:6])


#2
b=['a','b','c','d','e','f']
print(b)
print(b[4])
print(b[-3])
print(b[2:4])


#3
c=[1.2,2.3,3.4,4.5,5.6,6.7]
print(c)
print(c[3])
print(c[-4])
print(c[-3:-1])


#4
d=['a',1,2.3,4j,'vijay','naveen','akhila']
print(d)
print(d[4])
print(d[-6])
print(d[2:5])


#5
vijay=[1,2,3,4,5,6,7,8,'me','a','you']
print(vijay)
print(vijay[5])
print(vijay[-9])
print(vijay[0:9])


#6
hai=[1,2,3,3,33,'jnm','hkjn','kjno',1234,'ojnkm']
print(hai)
print(hai[-4])
print(hai[5])
print(hai[0:5])


#7
min=['hbjjnlm',8980,'b',234,646,53j,'jjnj','hbih']
print(min)
print(min[4])
print(min[-5])
print(min[2:4])


#8
max=['niojn',234,987,'hgfrd',234j,223.654,900]
print(max)
print(max[3])
print(max[-5])
print(max[2:5])


#9
teks=[1,2,3,4,5,6,7,8,9,9,979,56,342,21,7,9,34,798,55]
print(teks)
print(teks[6])
print(teks[-9])
print(teks[4:9])

#10
vm= [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vm)
print(vm[4])
print(vm[-5])
print(vm[-2:])


#3 explain all methods with examples

#1 append()
a=[1,2,3,4,5]
a.append(4)
print(a)

#2.extend()
a=[1,2,3,4,5,6,'vijay']
b=[3,4,5,6,7,8,9,'kanth']
a.extend(b)
print(a)
#3.pop()
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
a.pop()
print(a)

#4.len()
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
print(len(a))

#5.count()
a=[1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
print(a)