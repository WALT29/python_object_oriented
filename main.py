"""
PYTHON OBJECT ORIENTED
Is a programming paradigm in which the data(state) and the methods(fuctions) that work on the data are bundled together under one unit 
the unit is given a name

class-a bundle of data and functionality.Can be copeid and modified to accomplish a wide range of variety tasks

initialize -create a working copy of class using __init__()

instance- a working copy of a class

object-commmon name of an instance

function-a series of steps that create ,transform and move data

method-a function that is defined inside a class

magic method-a special type of method in python that starts and ends with double underscores .These methods are called on objects under certain conditions without needing to use their name explcitly

attributes-variables that belong to an object

property-attributes that are controlled by methods


OBJECT EXAMPLE
EG 
ANIMALS -CLASS
Dogs,cats,birds-OBJECTS  ..OBJECTS lie under the class family

Each object has property which can be controlled by methods
property examples      methods examples
aiplane.speed=500      airplane.fly()
car.speed=50           car.drive()

a method and a property must be linked to an object inorder to use it

CREATING AN OBJECT
black_turtle=Turtle()
    black_turtle is the object
    Turtle() is the class ....should always capitalize and ends with parenthesis

black_turtle.color("black") //sets the color of the turtle black

CREATING A CLASS

class ClassName():
    def __init__(self,parameter): this is our constructor function this where we create the properties or variables
        self.parameter
    
    def class_methods(self):  self keyword allows us to use properties and variables anywhere throught the class 
        print(self.parameter)

object=ClassName(arguments) -here we create an instance of the class and the argument are given to the init function
object.class_methods -here we have linked the class methods to our object

"""
#EG
#Create a class for animals with properties name,pet,sound
#create a method called speak,print out the sound of the animal
#crate a method called pet info ,prints out the pet info (pet properties)
#create 2 objects with different values
#call the methods with your object
class Animals():
    def __init__(self,name,pet ,sound):
        self.name=name
        self.pet=pet
        self.sound=sound
    
    def speak(self):
        print(self.name,self.sound)
    
    def pet_info(self):
        print("Pet-Name :",self.name)
        print("Pet :",self.pet)
        print("Pet-sound :",self.sound)

dog=Animals("Miles","dog","barks")
dog.speak()
dog.pet_info()

cat=Animals("Medussa","cat","meows")
cat.speak()
cat.pet_info()
        
#we care working with the NBA ,we need a class called Player
#this class has three properties:name,score and team.Team is initially set to empty
#create a method called show_stats this will print of the info about the player
#create a method called select_team this will ask for an input  and set the value of the team property

#create an object for player
#call your methods
#how can you show the updated player details after entering a team

# class Player():
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#         self.team=None #or "-"
        
#     def show_stats(self):
#         print(f"The Player-Name is: {self.name} . The score is {self.score} . Team:{self.team}")
    
#     def select_team(self):
#         team=input("ENTER YOUR TEAM NAME: ")
#         self.team=team
        

# player=Player("John Doe",10)
# player.show_stats()

# player.select_team()
# player.show_stats()







#we are building a class to find the perimeter and area of the rectangle what parameter do we need to solve this
#create a method to print off the basic info about the rectangle
#create a method to calculate the perimeter (length + width *2) then return the value
#create a method to calculate the area (length*width) then return the value
#create a method that will shorten the length of the rectangle,it'll take one parameter and return the updated perimeter

#gather the length and width through 2 inputs
#create an object giving it the arguments that we need
#print off the basic info about the rectangle
#print of the perimeter of the rectangle 
#print of the area of the rectangle

#ask for input to reduce the lendth of the current rectangle
#print of the updated rectangle perimeter

# class Rectangle():
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
    
#     def print_info(self):
#         print(f"The dimensions of the rectangle:length:{self.length} Width:{self.width}")
        
#     def calc_perimeter(self):
#         self.perimeter=(self.length +self.width)*2
#         return self.perimeter
    
#     def calc_area(self):
#         self.area=self.length*self.width
#         return self.area
    
#     def update(self,length):
#         self.updated=(self.length-length)*self.width
#         return self.updated
    

# a=int(input("ENTER THE LENGTH:"))
# b=int(input("ENTER THE WIDTH:"))


# my_rectangle=Rectangle(a,b)
# my_rectangle.print_info()

# print("PERIMETER:",my_rectangle.calc_perimeter())
# print("AREA:",my_rectangle.calc_area())
# c=int(input("ENTER THE NUMBER TO SUBTRACT THE LENGTH:"))
# print("UPDATED AREA",my_rectangle.update(5))


##INHERITANCE -This is the transfer of properties and methods from the parent class to the derived/child class
"""
Types of inheritance 
    1)The child class is given new methods but new properties are not given(we define new methods in the child class but we dont define new properties)
        in this method we dont need to create a constructor __init__ within the child .we can use the parent __inti__
    
    2)The child is given new properties and methods(we define new properties and methods)
        in this method we create a constructor (__init__)within the the child class and also activate the parent constructor

dont not use self outside the class
"""
##EXAMPLE 1 -the child class recieves new methods but we dont define new properties so there is no need to create a constructor function __init__ in the child class
class Agent(): #parent
    def __init__(self,name,health,car):
        self.name=name
        self.health=health
        self.car=car
    
    def agent_info(self):
        print("Agent Name:",self.name)
        print("Agent Health:",self.health)
        print("Agent Car:",self.car)
        

class Spy(Agent):#child
    def spy_talk(self):
        print("My name is ",self.name)
    
    def shoot(self,bad_guy): #here we pass in an object as the bad_guy
        if bad_guy.health >0:
            bad_guy.health -=20
        elif bad_guy.health <=0:
            print(self.name,"has assasinated",bad_guy.name)

james_bond=Agent("James Bond",100,"Mercedes-Benz")
ethan_hunt=Spy("Ethan Hunt",40,"Ferrari")

ethan_hunt.shoot(james_bond)
print(james_bond.health) #health decrease from 100 to 80


##EXAMPLE 2 - in the child class we are defining new properties and methods

class Spy2(Agent):
    def __init__(self, name, health, car,location,agency): #location and agency are the new properties 
        super().__init__(name, health, car)
        self.location=location
        self.agency=agency
    
    def  spy_talk(self):
        print("I am",self.name, "based at",self.agency,"in",self.location)
        
        
romelu=Spy2("Romelu Lukaku",100,"VW","Belgium","FBI")
romelu.spy_talk()

##EXERCISE
"""
use the animal class
create a child class called fish
create a method called swim ,if the sound is equal to None,print I am a fish,I do not have a sound otherwise print are you sure you are fish

create a 2nd method called ocean,ask the fish which ocean they are from,print off
eg nemo is a fish who lives in the pacific ocean

create an object and call the four methods
"""
# class Fish(Animals):
#     def swim(self):
#         if self.sound ==None:
#             print("I am a fish,I do not have a sound")
#         else:
#             print("are you sure you are fish")
    
#     def ocean(self,ocean):
#             print(f"{self.name} is a fish who lives in the {ocean}") 
        
        
# tilapia=Fish("tilapia","fish",None)
# tilapia.swim()
# myInput=input("which ocean are you from :")
# tilapia.ocean(myInput)

"""
we need a superclass for vehicles
our constrctor has the following basic info make,model,year and price
create a method to check if the make is a ford ,chevy or tesla ,if so return American made otherwise return imported
create a method that returns the vehicle model
create a mthod that checks if the car years is greater than 2000 if so return car from the 21st century otherwise return this car is old
create a mthod that accpts max price you are willing to pay this method checks if the car price is under your budget if yes return within your budget otherwise return over budget

create a child class for the style
this class accepts the superclass and also a parameter of its own num_of_doors
create one method ,if num_of_doors is 4 return family car otherwise sports car
create three objects  1 object using the superclass ,call 2 methods
the 2 other objects use the child class ,call three or more methods
use the child method and get price method






"""

# class Vehicles():
#     def __init__(self,make,model,year,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price
        
#     def check_make(self):
#         if self.make == "ford" or self.make=="chevy" or self.make=="tesla":
#             return "American Made"
#         else:
#             return "Imported"
    
#     def check_model(self):
#         return self.model
        
#     def check_year(self):
#         if self.year >2000:
#             return "car from 21st century"
#         else:
#             return "This car is old"
    
#     def check_price(self):
#         entered_price=int(input("Please Enter Your Maximum price :"))
#         if entered_price >=self.price:
#             return "Within your budget"
#         else:
#             return "Try again increase funds"
    
    
# class Style(Vehicles):
#     def __init__(self, make, model, year, price,num_of_doors):
#         super().__init__(make, model, year, price)
#         self.num_of_doors=num_of_doors
    
#     def check_doors(self):
#         if self.num_of_doors ==4:
#             return "family car"
#         else:
#             return "sports car"
        

# nissan=Vehicles("isuzu","box",2010,130000)
# print(nissan.check_model())
# print(nissan.check_make())

# convertible=Style("mercedes","e-class",2025,7500000,2)
# print(convertible.check_price())
# print(convertible.check_model())
# print(convertible.check_make())

# pickup=Style("chevy","track",1997,300000,4)
# print(pickup.check_price())
# print(pickup.check_model())
# print(pickup.check_doors())


"""
BUILDING CLASS METHODS AND ATTRIBUTES
Instance Attributes- is responsible for holding info about the instance 
    -Variable that is available in the scope for all instance methods in a class

Class Attributes - A class attribute is accessible in entire class ,it has a class scope
    -store info about the class a a whole

Class methods -A class method is a method that is called on the class itself not on the instances of the class 

"""

###############################################################################################################################################################

"""
Defining a class attribute
    a class attribute must be declared outside any methods in the class
"""

class Album():
   
    album_count=0 #class attribute
    def __init__(self, date):
        self.release_data=date
        
joshua=Album(2008);
print(Album.album_count)
print(joshua.album_count)

"""
Manipulating class methods from instance methods

    here I want the game count to increase everytime a game is created or initialized
    
    using the className and dot notation we can access the class attribute from anywhere in our class (both class and instances)
        Game.game_count
"""
# class Game():
#     game_count=0
#     def __init__(self,date) :
#         Game.game_count +=1
#         self.date=date

# Game(2008)
# Game(2001)
# print(Game.game_count) # 2

"""       
Defining a Class Method

@classmethod
def class_method_name(cls):
    #code
    
cls -refers to the entire class itself not an instance of the class ,in this case we are not in the instance scope but the class scope

lets refactor so that the game_count can be changed by the class itself

"""
class Game():
    game_count=0
    def __init__(self,date) :
        self.increase_game_count()
        self.date=date
    
    @classmethod
    def increase_game_count(cls,increment=1):
        cls.game_count +=increment
        

Game(2004)
Game(2006)
print(Game.game_count)

"""
CLASS CONSTANTS
similiar to class attributes 
    # defined in the body of the class
    # accessed from within the class method 
    # accessed from within the instance method 
    
Defined using all capital letters
   class User:
       USERS=["Admin","Moderator","Contributor"] 
       
store values which cannot change
scope-wise constants can be accessed from outside of the class
"""
class Album2():
    GENRES=['Hip-Hop','Jazz','Reggea'] # class constants
    album_count=0 #class attributes
    def __init__(self,year,genre) -> None:
        if self.check_genre(genre):
            self.increase_count()
            self.genre=genre
            self.year=year
    
    @classmethod
    def check_genre(cls,genre):
        return genre in cls.GENRES
    
    @classmethod
    def increase_count(cls,increment=1):
        cls.album_count +=increment
        

sorry=Album2(2015,"Hip-Hop")
print(dir)

"""
USING CLASS VARIABLES TO STORE INSSTANCES OF A CLASS
imagine you want to create a music app that manages user's music ,our app should keep track of all songs that a user enters and allow the user to browse through their songs

"""
class Song():
    all=[]# a list is good for storing a large collection of related data
    def __init__(self,name):
        self.name=name
        self.add_song_to_all(self) # self refers to the created object
        
        """
        in the __init__ we use self keyword to refer to the new created object
        when a new object is instantiated,it creates a  new instance of the class and then calls __init__on the new instance
        so __init__ is technically an instance method .Inside an instance method we are in what is called a mthod scope and self refer to whichever instance the method is being called on
        """
    
    @classmethod
    def add_song_to_all(cls,song):
        cls.all.append(song)
    
    @classmethod
    def show_song_name(cls):
        print([song.name for song in cls.all])
    
tiktoker=Song("Tiktoker")
setit=Song("Set it")

Song.show_song_name() #prints all song names
################################################################################################################################################
################################################################################################################################################
"""
#ATTRIBUTES AND PROPERTIES
Atributes -variables that belong to an object
Property -attributes that are controlled by methods

CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE
class human takes name as an argument for its iniatilaization method and saves it as an attribute of self.This attribute varies from one instance of human class to the next -INSTANCE ATTRIBUTE
since species is the set outside the scope of any method its a CLASS ATRIBUTE.All members of the human class have the same species

"""
class Human:
    species="Homo Sapien"
    def __init__(self,name):
        self.name=name
        
my_name=Human("DAVE")
print(my_name.name)#DAVE
print(my_name.species) #homo sapien
print(Human.species)#Homo Sapien
#print(Human.name) error since its an instance attribute 

"""
SETTING & GETTING ATTRIBUTE
many programming language tend to rpotect their object's attributes and methods(members).They accomplish this by making distinction between,public,private and protected

Public-availble to everyone who can access the class 
Private-availbe to the class that instantiated them
Protected -availble to the class that instantiated them and the object that inherits from the class but its not accessible otherwise

python doesnt make distinction btwn public,private and protected .This makes it easy to manipulate members of a clss/object with dot notation
"""
#changing values using dot notation
my_name.name="Irungu"
print(my_name.name)

#adding new attributes
my_name.nationality="kenyan"
print(my_name.nationality)

"""
BUILT IN FUNCTIONS TO MANIPULATE ATTRIBUTES

getattr()-retrieves the value of an attribute
setattr()-changes the value of an attribute ,like with dot notation
delattr()-deletes the attribute from a class/object
hasattr()-checks for presence of an attribute

GETTING AN ATTRIBUTE
getattr(object_name,"attribute_name")

getattr()has an optional third argument as a default value ,if the attribute doesnt exist
getattr(object_name,"attribute_name",FALSE)


#setting AN ATTRIBUTE
setattr(object_name,"attribute_name","attribute_value")

attr()
checks for presence of an attribute

"""
print(getattr(my_name,"name"))#Irungu
setattr(my_name,"name","dave")
print(my_name.name) #dave
print(hasattr(my_name,"name")) #true

"""
PROPERTEIS-attributes that are controlled by methods
"""
class Human2():
    def __init__(self,age):
        self.age=age #invokes the setter method
    
    def get_age(self):
        print("Retrieving age")
        return self._age
    
    def set_age(self,age):
        # print(f"setting age to {age}")
        # self._age=age
        if (type(age) in (float,int)) and 0<=age<=120:
            print(f"setting age to {age}")
            self._age=age
            print("age is set")
        else:
            print("Please enter a valid age between 0-120")
        
    age=property(get_age,set_age)
    
"""
self._age -the single underscore placed before age tells other programmers tht the attribute will be treated as private member ,but its a way of telling coworkers that this is property and there methods that depends on it

get_age()-is compiled by the property function and prints "Retrieving age" whenever access age thru dot notation
set_age*()-is complied by the property function and prints "setting age to .."when we change the human2 age

property()-compiles our getter and setter and calls them whenever we access our human age
"""

chege=Human2(20);
chege.age=34
#print(chege.age)
#chege.set_age(500)
#chege.age=False
###############################################################################################################################################################3
"""
ROUGHWORK

print(type("heloo") in (float, int, str, list, dict, tuple))
print(isinstance("hello",(float, int, str, list, dict, tuple)))
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]
print("Pug"in APPROVED_BREEDS)

"""
############################################################################################################################################################
"""
FUNCTION DECORATOR
Decorator is a function that takes another function as an argument and returns a new function often attaching pre/post functionality

@decorator
def func(a,b):
    return a
    
PROPERTY()-DECORATOR
WE use @property as a property getter method
the method should use the public name for the underlying manage attribute

@property decorator should decorate the getter method which should have the same name as the attribute
setter & deleter must be decorated with the same name as the getter method plus .setter ,.deleter
"""
class Animals():
    def __init__(self,name):
        self.name=name #invokes our setter function
    
    @property #this is our getter function
    def name(self):
        return self._name
    
    @name.setter #this is our setter function
    def name(self,name):
        if isinstance(name,str) and 1<=len(name)<=24:
            self._name=name
        
        else:
            print("Please enter a valid name")

Irungu=Animals("sdd")
Irungu.name=34

####################################################################################3###################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
"""
OBJECT RELATIONSHIPS 
Domain -a domain is a visualization of a set of relationship used to solve a problem.A python domain will show all of the classes involved in an application and how they relate to one another

one to many relationship - is a type of relationship btween objects whereby an object in class is connected to multiple objects in clss B
EG Dog arranging its toys

many to many relationship - is a type of relationship between objects whereby multiple objects in class A are connected to multiple objects in other classes
EG : students have many instructors and many instructors have many students  

"""
"""
ONE TO MANY RELATIONSHIP
Represented with the following techniques
1)Association
2)Aggregation
3)Composition

Assocition
Refers to a relationship whereby 2 objects are related but not in a way one object owns the other
EG:A library has an association with books as it stores them but it doesnt own them

AGGREGATION
Is a relationship whereby one object is part of another object ,the first object can exist independently
EG A car can have many wheels but the wheels can be used in different in other cars

COMPOSITION
Is a relationship whereby one object is made up of another object and the first object cannot exist without the second object
EG A house and rooms - A hse is composed of rooms and each room is part of the hse

"""
"""
ASSOCIATION 
Is a weak relationship between unrelated objects whre objects have their own lifetime and their is no parent object
1)One way one to many relationship
2)two way one to many relationship
"""
#ONE WAY ONE TO MANY RELATIONSHIP
"""
EG A shopper and a grocery item.
It makes no sense for the grocery item to have the name of the shopper hence its a one way one to many relationship
"""
class Grocery_item():
    def __init__(self,name,price):
        self.name=name
        self.price=price
        
class Shopper():
    def __init__(self,name):
        self.name=name
        self.grocery_list=[]
        
davey=Shopper("DAVE")  
kales=Grocery_item("kales",20)
cake=Grocery_item("cake",25)
##adding the grocery item in the shoppers grocery list
davey.grocery_list.append(kales)
davey.grocery_list.append(cake)
#printing the list
for item in davey.grocery_list:
    print(item.name,item.price)

"""
TWO WAY ONE TO MANY RELATIONSHIP
EG A Tr and Student rltnship .Student may need to know who the tr is
"""
class Student():
    all=[]
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._teacher=None
        self.all.append(self)
    
    @property
    def teacher(self):
        return self._teacher
    
    @teacher.setter
    def teacher(self,value):
        if not isinstance(value,Teacher):
            raise TypeError("Teacger Must be an instance of Teacher Class")
        self._teacher=value
    
class Teacher():
    def __init__(self,name):
        self.name=name
    
    def students(self):
        return[student for student in Student.all if student.teacher == self]
    
    def display(self):
        for student in self.students():
            print(student.name,student.age)
    
    def add_students(self,student):
        if not isinstance(student,Student):
            raise TypeError("Student must be an instance of student class")
        student.teacher=self

mwaniki=Student("mwaniki",23)
kebaso=Student("kebaso",25)
Nyambati=Teacher("nyambati")
mumbo=Teacher("mumbo")

mumbo.add_students(kebaso)
mumbo.add_students(mwaniki)
mumbo.display()

##REVISIT SINGLE SOURCE OF TRUTH

"""
2)Aggregation
Is a relationship between objects whereby one object is part of another object and the first object cannot exist without the second object

Is a form of association whereby each object has its own lifecycle but exists ownership as well
similar to objct relationship we can call a parent child relationship but instead of attributes the parent contains an instance of the child

"""
##EG A CAR AND ENGINE RELATIONSHIP
class Car():
    def __init__(self,engine): #takes in an engine object
        self.engine=engine
    
class Engine():
    def __init__(self,cylinders,fuel_type):
        self.cylinders=cylinders
        self.fuel_type=fuel_type
    
four_cylinder_engine=Engine(4,"regular")
isuzu=Car(four_cylinder_engine) #takes four_cylinder_engine as the instance of the class
print(isuzu.engine.fuel_type)

"""
3)COMPOSITION
composition is a part of relationship whereby both entities are interdependent on each other 

EG : a cpu is part of a computer and both are dependent on each other
"""
class CPU():
    def __init__(self,cpu_type):
        self.cpu_type2=cpu_type
    
class Computer():
    def __init__(self,cpu_type):
        self.CPU=CPU(cpu_type) #the computer gets the attributes of the cpu
        
intel=CPU("coreI9")
hp_zbook=Computer("corei7")
print(hp_zbook.CPU.cpu_type2)

######################################################MANY TO MANY RELATIONSHIP ####################################################################################
"""
Many to many relationship is a form of relationship whereby many instances of a class (users) are related to multiple instances of another class(websites) and vice versa
It important to consider wheter to use an intermediary class 
    INTERMEDIARY CLASS - is a class in between 2 other classes in many to many rltnship
        it provides more info abt the relationshi[]

"""
################# WITHOUT INTERMEDIARY CLASS ##########################
"""
use a list to store references of the related objects
EG PARENT AND CHILD 
"""
class Parent():
    all=[] #stores all the instances of the parent
    def __init__(self,name,children=None):
        self.name=name
        self._children=[] #i have added an underscore before the children attribute  to for purposes of encapsulation and access control .the children list should not be modified or accessd outside the class
        if children: #checks if the children is entered ,if its true it appends the child into the children attribute
            for child in children:
                self.add_child(child)
        Parent.all.append(self)
            
    def children(self): #returns a list of the children associated with a parent
        return self._children
    
    def add_child(self,child):
        if isinstance(child,Children):
            self._children.append(child)
        else:
            raise ValueError("The child must be an instance of the Child class ")


class Children():
    def __init__(self,name):
        self.name=name
        
    def parents(self):
        return[parent for parent in Parent.all if self in parent.children()]
    
    def add_parent(self,parent_object):
        if isinstance(parent_object,Parent):
            parent_object.add_child(self)
        else:
            raise ValueError("Parent must be an instance of parent class")

Davie=Parent("Dave")
Bobby=Parent("Bobby")

franchish=Children("Franchis")
miles=Children("miles")

Davie.add_child(franchish)
Bobby.add_child(miles)

franchish.add_parent(Bobby)
miles.add_parent(Davie)

[print(parent.name) for parent in miles.parents()]

[ print(child.name) for child in Davie.children()]

############################## WITH INTERMEDIARY 
"""
Student course relationship with the intermediary being the enrollment class

AGGREGATE METHODS 
Are methods that allow us to perform calculations and gather info abt relationships betweeen objects in an efficient manner

def course_count(self):
    return len(self._enrollments)  this method helps us to keep count of the number of enrollments


"""
from datetime import datetime
class Enrollment():
    all=[]
    def __init__(self,student,course):
        self.student=student
        self.course=course
        self.enrollment_date=datetime.now
        Enrollment.all.append(self)
    
class Student():
    all=[]
    def __init__(self,name):
        self.name=name
        Student.all.append(self)
    
    def enroll_in_course(self,course):
        Enrollment(self,course)
    
    def enrollments(self): ##returns all the enrollments of the student
        return[enrollment for enrollment in Enrollment.all if enrollment.student ==self]
    
    def course(self):
        return[enrollement.course for enrollement in self.enrollments()]
    
class Course ():
    all=[]
    def __init__(self,name) :
        self.name=name
        Course.all.append(self)
    
    def enrollements(self): # returns all the enrollements with the course enrolled
        return[enrollement for enrollement in Enrollment.all if enrollement.course==self]
        
    def students(self):
        return[enrollement.student for enrollement in self.enrollements()]
    
    def enroll_student(self,student):
        Enrollment(student,self)
    
mwangi=Student("Mwangi")
brayo=Student("Brayo")
eng=Course("Engineering")
tr=Course("Teaching")
eng.enroll_student(brayo)

print(brayo.enrollments()[0].course.name) ##[0] accesses the first enrollement
