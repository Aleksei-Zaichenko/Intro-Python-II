# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, n_to=None, s_to=None, e_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = []

    def displayDescription(self):
        print(self.description)

    def displayRoomsItems(self):
        print(f'Here you can see the following items:')
        for item in self.items:
            print(item)

    def addItemToRoom(self,item):
        self.items.append(item)

    def removeItemFromRoom(self,item):
        self.items.remove(item)
