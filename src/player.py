# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self,name,current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    
    def displayCurrentLocation(self):
        print(f'You are currently at: {self.current_room.name}')

    def movePlayerToRoom(self,room):
        self.current_room = room

    def displayPlayerItems(self):
        print('In your backpack you have the following items:')
        for item in self.items:
            print(item)

    def addItemToInventory(self,item):
        self.items.append(item)

    def removeItemFromInventory(self,item):
        searchedItem = self.findItem(item)
        return self.items.pop(self.items.index(searchedItem))

    def findItem(self,itemName):
        tempObject = None
        for itemObject in self.items:
            if itemObject.name == itemName:
                tempObject = itemObject
        return tempObject