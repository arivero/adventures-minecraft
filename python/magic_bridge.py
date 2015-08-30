'''
build a magic bridge

@author Charlie & Sammy
'''
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

bridge = []
bridge_block = block.LAVA_STATIONARY.id

def main():
    '''
    Main program
    '''
    mc = minecraft.Minecraft.create()
    while True:
        time.sleep(0.1)
        build_bridge(mc)

def build_bridge(mc):
    position = mc.player.getTilePos()
    current_block = mc.getBlock(position.x, position.y - 1, position.z)

    if current_block == block.WATER_STATIONARY.id or current_block == block.COBBLESTONE.id:
        mc.setBlock(position.x, position.y-1, position.z, bridge_block)
        coordinate = [position.x, position.y-1, position.z]
        bridge.append(coordinate)
    elif current_block != bridge_block:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.COBBLESTONE.id)
            time.sleep(0.1)

if __name__ == '__main__':
    main()
