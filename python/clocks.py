import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as minecraftstuff
import time
import datetime
import math

def find_point_on_circle(cx, cy, radius, angle):
    x = cx + math.sin(math.radians(angle)) * radius
    y = cy + math.cos(math.radians(angle)) * radius
    x = int(round(x, 0))
    y = int(round(y, 0))
    return(x,y)

mc = minecraft.Minecraft.create()

modrawing = minecraftstuff.MinecraftDrawing(mc)

pos = mc.player.getTilePos()

clock_middle = pos
clock_middle.y = clock_middle.y + 25

CLOCK_RADIUS = 20
HOUR_HAND_LENGTH = 10
MIN_HAND_LENGTH = 15
SEC_HAND_LENGTH = 18

modrawing.drawCircle(clock_middle.x, clock_middle.y, clock_middle.z, CLOCK_RADIUS, block.DIAMOND_BLOCK.id)


while True:
    now = datetime.datetime.now()
    hours = now.hour
    if hours >= 12:
        hours = now.hour - 12

    minutes = now.minute

    seconds = now.second

    # hour hand
    hour_hand_angle = 360 / 12 * hours
    hour_hand_x, hour_hand_y = find_point_on_circle(clock_middle.x, clock_middle.y, HOUR_HAND_LENGTH,hour_hand_angle)
    modrawing.drawLine(clock_middle.x, clock_middle.y, clock_middle.z,hour_hand_x, hour_hand_y, clock_middle.z, block.DIRT.id)

    minute_hand_angle = 360 / 60 * minutes
    minute_hand_x, minute_hand_y = find_point_on_circle(clock_middle.x, clock_middle.y, MIN_HAND_LENGTH,minute_hand_angle)
    modrawing.drawLine(clock_middle.x, clock_middle.y, clock_middle.z,minute_hand_x, minute_hand_y, clock_middle.z, block.WOOD_PLANKS.id)

    second_hand_angle = 360 / 60 * seconds
    second_hand_x, second_hand_y = find_point_on_circle(clock_middle.x, clock_middle.y, SEC_HAND_LENGTH,second_hand_angle)
    modrawing.drawLine(clock_middle.x, clock_middle.y, clock_middle.z,second_hand_x, second_hand_y, clock_middle.z, block.WOOD.id)

    time.sleep(1)
    modrawing.drawLine(clock_middle.x, clock_middle.y, clock_middle.z,second_hand_x, second_hand_y, clock_middle.z, block.AIR.id)
    modrawing.drawLine(clock_middle.x, clock_middle.y, clock_middle.z,minute_hand_x, minute_hand_y, clock_middle.z, block.AIR.id)
    modrawing.drawLine(clock_middle.x, clock_middle.y, clock_middle.z,hour_hand_x, hour_hand_y, clock_middle.z, block.AIR.id)
