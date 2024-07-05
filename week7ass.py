#define  the parent class
def __init__(self,name):
    self.name=name


    def spaeak(self):
        print(f'i am {self.name}. I am a parent.')

#child class inherits from parent
    class Child(parent):

      def __init__ (self,name,age):
         super().__init__(name)
         self.age = age
         def speak(self):
                   print(f'i am {self.name}.i am a child.i am {self.age}years old.')


#granchild inherit from child
      def __init__(self,name,age,hobby): 
         super().__init__(name,age)
         self.hobby = hobby

    def speak(self):
         print(f'i am {self.name}, i am a grandchild. i am{self.age} years old and i love{self.hobby}.')

 #creating instances
    parent = parent('Abiola')
    child = child ('Dami',10)
    grandchild= grandchild('Bob',5,'music')

#calling the methods
    parent.speak()
    child.speak()
    grandchild.speak()
        

