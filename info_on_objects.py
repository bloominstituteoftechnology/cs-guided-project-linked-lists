# The class is like a blueprint for objects. It doesn't make any new
# objects, but describes how to create them.
​
class House:
    def __init__(self, rooms):    # Constructor to initialize instances
        self.room_count = rooms   # Called when new objects are created
        self.foundation = "slab"  # from the blueprint
        self.roof = "composite"
​
    def print_room_count(self):   # "Method" on the class
        print(self.room_count)
​
​
# Create new houses from the blueprint (the class)
#
# We call this "instantiation".
#
# We're "instantiating" or "constructing" two new House objects
# from the blueprint that is the class:
​
house1 = House(4)  # house1 is an "instance" of a house
house2 = House(2)  # house2 is an "instance" of a house, as well
​
# Now call the print_room_count() method for each. "method" is a
# term that means "function that operates on an instance of a
# class". Methods are declared inside the class itself
​
house1.print_room_count()   # 4
house2.print_room_count()   # 2
​
# The "self" in the class is a tough concept at first. It means
# "the object that we're calling this method on."
#
# So when house2 calls print_room_count(), "self" in that method
# will be set to house2. That is "self is house2".
#
# If house1 called it, self would be house1.