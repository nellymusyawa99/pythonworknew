#tuples
fruits=['apple','banana','oranges']
print(fruits)
#lists are changable but tuples are not
#change tuple to list
myfruits=list(fruits)
myfruits[-1]='grapes' #i have changed oranges to grapes
myfruits.append('strawberries')
#change list to tuple
fruits=tuple(myfruits)
print(fruits)



#sets are unchangable, they are unordered, do not have index, duplicates not allowed

#dict they are changable,have key value pairs,

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["year"])

#funtion is a piece of code that we write
def addition(x,y):
  return x+y #shows the values

#calling a funtion
print('the sum is:',addition(x:12, y:12))

#modules
/





