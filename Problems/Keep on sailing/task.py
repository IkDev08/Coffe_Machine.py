# our class Ship
class Ship:
    def __init__(self, name, capacity, destination):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.destination = destination

    # the old sail method that you need to rewrite
    def sail(self):
        return "{} has sailed for {}!".format(self.name, self.destination)


black_pearl = Ship("The Black Pearl", 800, input())
print(black_pearl.sail())
