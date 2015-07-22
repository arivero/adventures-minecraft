'''
Print a welcome message when our player gets home

@author Charlie & Sammy
'''
import mcpi.minecraft as minecraft
import time

class Place(object):
    '''
    '''
    def are_we_here(self, position):
        '''
        @param {Minecraft.position} position
        '''
        if self.x == position.x and self.z == position.z:
            return True
        else:
            return False

    def __init__(self, x, z, message):
        '''
        Constructor
        '''
        self.x = x
        self.z = z
        self.message = message

def main():
    '''
    Main program
    '''
    mc = minecraft.Minecraft.create()

    places = []
    places.append(Place(-39, 25, 'Welcome Sammy'))
    places.append(Place(-119, 60, 'Welcome Charlie'))

    while True:
        time.sleep(0.5)
        position = mc.player.getTilePos()
        for place in places:
            if place.are_we_here(position):
                mc.postToChat(place.message)

if __name__ == '__main__':
    main()
