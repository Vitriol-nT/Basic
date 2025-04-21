from BasicPhysics import bodies
from BasicPhysics import plotting
from BasicPhysics import Wall

firstbody = bodies(Position=(0,0,100), Velocity=(0,2,0))
thewall = Wall(firstbody, Position=(300,80,100), rotation=(0,1))
visualize = plotting(firstbody, thewall)
visualize.update(35)
