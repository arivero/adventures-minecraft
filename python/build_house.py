'''
build a home

@author Charlie & Sammy
'''
import mcpi.minecraft as minecraft
import mcpi.block as block

def main():
    '''
    Main program
    '''
    mc = minecraft.Minecraft.create()
    position = mc.player.getTilePos()
    size = 20

    x = position.x + 2
    y = position.y
    z = position.z

    for i in range(1):
        new_house(mc, size, x + i * (size + 5), y, z)

def new_house(mc, size, x, y, z):
    '''
    builds a new house
    '''
    mid  = size / 2

    # eeoutside of house
    mc.setBlocks(x, y, z, x + size, y + size, z + size, block.TNT.id)

    # fill with air
    mc.setBlocks(x + 1, y, z + 1, x + size - 1, y + size - 1, z + size - 1, block.TNT.id)

    # door
    #mc.setBlocks(x + mid - 1, y, z, x + mid, y + 1, z, block.AIR.id)

    # floor
    #mc.setBlocks(x + 1, y - 1, z + 1, x + size - 1, y - 1, z + size - 1, block.COBBLESTONE.id)

    # windows
    #mc.setBlocks(x + 3, y + size - 2, z, x + 6, y + size - 6, z, block.GLASS_PANE.id)
    #mc.setBlocks(x + size - 3, y + size - 2, z, x + size - 6, y + size - 6, z, block.GLASS_PANE.id)

if __name__ == '__main__':
    main()
