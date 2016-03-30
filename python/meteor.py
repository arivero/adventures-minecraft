import mcpi.minecraft as minecraft
import mcpi.block as block
import time

BLOCK = block.BEDROCK.id
mc = minecraft.Minecraft.create()


def start_meteor(x, z):
    floor = mc.getHeight(x, z)
    y = 100 + floor
    while y > floor:
        mc.setBlock(x, y, z, block.AIR.id)
        y = y - 1
        mc.setBlock(x, y, z, BLOCK)
        time.sleep(0.1)

position = mc.player.getTilePos()
start_meteor(position.x, position.z + 1)
