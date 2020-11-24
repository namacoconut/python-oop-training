class Dog:
  def __init__(self, gender, color):
    self.gender = gender
    self.color = color
    # Instance method
    def description(self):
        return f"{self.gender} is {self.color} "

    # Another instance method
    def speak(self, sound):
        return f"{self.gender} says {sound}"

my_dog = Dog('male', 'black')
print(my_dog.gender)








