import mcpi.minecraft as minecraft
import random
from time import sleep

mc = minecraft.Minecraft.create()

PHRASES = ('gowies', 'hi', 'what\'s up',':)','hello','I am cool','wowweeee')

for i in range(100):
    print(i)
    phrase = PHRASES[random.randint(0,len(PHRASES))-1]
    mc.postToChat(phrase)
    sleep(2)
