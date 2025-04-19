from BasicPhysics import bodies
from BasicPhysics import plotting
from BasicPhysics import Wall
from BasicPhysics import ForTest
import math
#radian

firstbody = bodies(Position=(0,0,100), Velocity=(0,2,0))
thewall = Wall(firstbody, Position=(0,10,0), Rotation=(0,1,0))
p = ForTest(firstbody, Wall)
p.update(25)
