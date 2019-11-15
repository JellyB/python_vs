class Dog:

    def __init__(self, name):
        self.name = name
        self.woofs = 0

    def speak(self):
        print("Woof!")

    def hear(self, words):
        print(words)
        self.speak()

    def count(self):
        self.woofs += 1
        for n in range(self.woofs):
            self.speak()

class Husky(Dog):
    origin = 'Sibera'

    def speak(self):
        print('Awoooo!')
   
class Chihuahua(Dog):
    
    origin = 'Mexico'
    
    def speak(self):
        print('Yip')

class Labrador(Dog):
    origin = 'New York'

    def speak(self):
        print('Jio!')

# print(isinstance(True, int))
