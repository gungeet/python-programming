insts = [1,2,3,4]

strings = ['kiwi', 'banana', 'mango']

dictionaries = [{'a':100, 'b':200}, {'a':50, 'b':300}]

#classes are templete
#create data type
#every class sould have __init__ to initialize the class data
#classes are used to create objects 
#HockeyTeam is used to create object team
#a function in a class in called a method

class HockeyTeam:
    no_of_teams = 0 #class variale is like a shared variable
    def __init__ (self, name): 
        self.name = name #if we call this class, the object needs a name

    #instance method
    def foo(self):
        print ('Yah!')

    #class method
    def bar():
        print ('I am a class function.')

my_team = HockeyTeam('Bruins') #this creates an instance when HockeyTeam is called followed by ('name')

my_team.foo() #can use data type above send it through the foo method

HockeyTeam.bar