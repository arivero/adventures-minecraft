'''
Get the player's position

@author Charlie & Sammy
'''
import mcpi.minecraft as minecraft


def main():
    '''
    Main program
    '''
    mc = minecraft.Minecraft.create()
    position = mc.player.getTilePos()
    print(position)

if __name__ == '__main__':
    main()
