import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import math

def distance_between_points(point1, point2):
    xd = point2.x - point1.x
    yd = point2.y - point1.y
    zd = point2.z - point1.z
    return math.sqrt((xd*xd) + (yd*yd) + (zd*zd))

TOO_FAR_AWAY = 15
FRIEND_BLOCK = block.LAVA.id

mc = minecraft.Minecraft.create()
mcdrawing = minecraftstuff.MinecraftDrawing(mc)

blockmood = "happy"

friend = mc.player.getTilePos()
friend.x = friend.x + 5

friend.y = mc.getHeight(friend.x, friend.z)

mc.setBlock(friend.x, friend.y, friend.z, FRIEND_BLOCK)

mc.postToChat("<block> you smell")

target = friend.clone()
