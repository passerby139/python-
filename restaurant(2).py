from 面向对象 import Dog

class Restaurant():
    def __init__(self,name,number_served):
        self.name=name
        self.number_served=number_served
        self.numbered_served=0
    def set_number_served(self,qw):
        self.numbered_served+=qw
    def read(self):
        print("My raeataurant numbered served is "+str(self.numbered_served))

my_restaurant=Restaurant("蜀九门",6)

print("My restaurant name is"+my_restaurant.name)
print("My restaurant have "+str(my_restaurant.number_served)+" people is eating now.")


my_restaurant.set_number_served(8)
my_restaurant.read()
my_restaurant.set_number_served(3)
my_restaurant.read()



my_dog=Dog('zyj',6)
print("dog's name is"+my_dog.name+".")
print("dog's age is"+str(my_dog.age)+".")