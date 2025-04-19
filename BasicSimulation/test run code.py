#testing
#need UI after this.
from BasicPhysics import bodies
from BasicPhysics import plotting

firstbody = bodies(Position=(0,0,100), Velocity=(-50,2,3))
p = plotting(firstbody)
p.update(25)

