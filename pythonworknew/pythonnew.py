# lerning about variables

x=5 #integer
y="5" #string
x=5.0 #float

x=y=z= "blue"
print (x)
print (y)
print (z)



# == means asking if the two values are equal
#comparisons
r=7
a=4
print(r==a)

#COMPARIOSON STATEMENTS
age=30

#elif statement

if age > 18:
    print("adult")
elif age < 18:
    print("child")


#if...elif...else statement
t=200
e=20
if t>e:print("true")
elif t<e:print("false")
else :print("error")

#using the and statement
presidentage=40
nationality="norway"

if presidentage>=20 and nationality=="kenyan":print("eligible")
else: print("not eligible")

#checking or statement
nationality="uganda"
if nationality=="Kenya" or nationality=="uganda"or nationality=="Tanzania":
    print("you qualify for cecafa") #executes if one of the conditions is met
else:
    print("you dont qualify for cecafa")

#checking whether a number is odd or even
f=18
if f%2==0:
    print("even")
else:print("odd")

#casting in python(concatination)
firstname="Nelly"
secondname=9
fullname=firstname+" "+str(secondname)
print(fullname)

#string to integer(convatination)
penstotal=20
bookstotoal="20"
total=penstotal+int(bookstotoal)
result=str(total)+" "+"ksh"
print(result)

#looping in python with break statement
i=0
while i<11:
    print(i)
    i +=1

"""
multi line comments
multi line comments
"""



def count_nationalities(people):
    kenyans=0
    ugandans=0
    for person in people:
        if person["nationality"].lower()=="kenyan":
            kenyans+=1
        elif person["nationality"].lower()=="ugandan":
            ugandans+=1

    return kenyans,ugandans



kenyans,ugandans=count_nationalities(people)
print("number of kenyans:",kenyans)
print("number of ugandans:",ugandans)

#for looop
for x in students
    print(x)

#range function
for x in range(5)
    print(x)
