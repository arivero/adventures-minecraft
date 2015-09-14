import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

GAP = block.STONE.id
WALL = block.GOLD_BLOCK.id
FLOOR = block.GOLD_BLOCK
FILENAME = '../resources/mazes/sam1.csv'
filehandle = open(FILENAME, 'r')

pos = mc.player.getTilePos()
ORIGIN_X = pos.x + 1
ORIGIN_Y = pos.y
ORIGIN_Z = pos.z

z = ORIGIN_Z

for line in filehandle.readlines():
    data = line.split(',')
    x = ORIGIN_X

    for cell in data:
        if cell == '0':
            block = GAP
        else:
            block = WALL

        mc.setBlock(x, ORIGIN_Y, z, block)
        mc.setBlock(x, ORIGIN_Y + 1, z, block)
        mc.setBlock(x, ORIGIN_Y - 1, z, FLOOR)
        x = x + 1
    z = z + 1
