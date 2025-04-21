from BasicPhysics import bodies
from BasicPhysics import plotting
from BasicPhysics import Wall

firstbody = bodies(Position=(0,0,100), Velocity=(3,-1,3))
thewall = Wall(firstbody, Position=(0,0,30), rotation=(-0.1,0.5))
visualize = plotting(firstbody, thewall)
visualize.update(35)
