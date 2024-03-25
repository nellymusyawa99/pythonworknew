#question 1
def find_largest_number(numbers):
    max_number = float('-inf')
    for num in numbers:
        if num > max_number:
            max_number = num

    return max_number

#e.g
my_list = [10, 200, 30, 40]
largest_number = find_largest_number(my_list)
print("largest number is:",largest_number)


#question 2
my_list = ["pens","pencils","eraser","eraser","eraser","pencils"]
repeated_elements = []

for item in my_list:
    if my_list.count(item)>1:
        repeated_elements.append(item)
        print(my_list)

#question 3
student_name=("nelly","eugene","rocky","ken")
y=list(student_name)
y.append ("howard")
student_name=tuple(y)

print(student_name)

#que3stion 4 converting lists to dict
list1=["pens","pencils","books"]
list2=["karry","jesse","yasmine"]
print(list1)
print(list2)
mydict=dict(zip(list1,list2))
print(mydict)


#exception handling
try:
    print(x)
except:
    print("an exception occurred")


#a class is like an object constructor, or a blueprint for creating objects
class  student:
    def __init__(self,studentid):
        print("student constructor has been called when class is called",studentid)
stud1=student(2000)


class student:
    student_id = 0
    student_name = ""
    student_age = 0
    def __init__(self, student_id, student_name, student_age):
        self.student_id = student_id
        self.student_name =student_name
        self.student_age =student_age

    def displayStudent(self):
        print("this is the student details:Name:",self.student_name,"Age:",self.student_age)

student1=student("9936","Dante","22")
student1.displayStudent()

#polymorphism
class Animal:
    limbs=4
    eyes=2
    def __init__(self,limbs,eyes):
        self.limbs=limbs
        self.eyes=eyes

    def speak(self):
        print(" i speak")

class Dog(Animal):
    toes="claws"
    def speak(self):
        print("i bark")


class Cat(Animal):

    def __init__(self,limbs,eyes):
        self.limbs=limbs
        self.eyes=eyes1
    def speak(self):
        print("i meow")

dog1=Dog(4,2)
dog1.printProperties()
dog1.speak()

cat1=cat(2,2)
cat1.speak()











