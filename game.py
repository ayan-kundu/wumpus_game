# game.py
#
# The top level loop that runs the game until Link wins or loses.
#
# run this using:
#
# python3 game.py
#
# Written by: Simon Parsons
# Last Modified: 25/08/20

from world import World
from link  import Link
from dungeon import Dungeon
import utils
import time

# How we set the game up. Create a world, then connect player and
# display to it.
gameWorld = World()
player = Link(gameWorld)
display = Dungeon(gameWorld)

# Now run...
while not(gameWorld.isEnded()):
    gameWorld.updateLink(player.makeMove())
    gameWorld.updateWumpus() #if commented it’s static world
    # Uncomment this for a printout of world state
    # utils.printGameState(gameWorld)
    display.update()
    time.sleep(1)

if gameWorld.status == utils.State.WON:
    print("You won!")
else:
    print("You lost!")

