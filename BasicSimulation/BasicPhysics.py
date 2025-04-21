#The API
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import tkinter.messagebox as tkmsg

Gravity = -9.8
Wind = 1
col = False

class bodies:
  Mass = 5
  DisplaySize = 0.5
  resistance = 0.1

  def __init__(self, Position=(0,0,0), Velocity=(0,0,0)):
    self.Position = list(Position)
    self.Velocity = list(Velocity)
  
  def move(self):
    self.Position[0] += self.Velocity[0]
    self.Position[1] += self.Velocity[1]
    self.Position[2] += self.Velocity[2]
  
  def deflectionFromGround(self):
    self.Velocity[2] *= -1
    self.Velocity[2] *= (1 - self.resistance)
    self.Position[2] = 0
  
  def Acceleration(self):
    self.Velocity[2] = self.Velocity[2] + Gravity
    self.Velocity[0] += Wind

class Wall:
  def __init__(self, body, Position=(0,0,0), rotation=(0,0)):
    self.Position = list(Position)
    self.rotation = list(rotation)
    self.body = body

  def Plane(self, x, y):
    z = math.tan(self.rotation[0]) * ( x - self.Position[0] ) + math.tan(self.rotation[1]) * ( y - self.Position[1]) + self.Position[2]
    return z

  def VectorReflection(self):
    global col

    Normal = (math.tan(self.rotation[0]), math.tan(self.rotation[1]), -1)
    if self.body.Position[2] <= self.Plane(self.body.Position[0], self.body.Position[1]):
      col = True

    if col == True:
      self.body.Position[2] = self.Plane(self.body.Position[0], self.body.Position[1])
      #reflection
      self.body.Velocity[0] = self.body.Velocity[0] + (-2 * Normal[0] * (self.body.Velocity[0] * Normal[0]))
      self.body.Velocity[1] = self.body.Velocity[1] + (-2 * Normal[1] * (self.body.Velocity[1] * Normal[1]))
      self.body.Velocity[2] = self.body.Velocity[2] + (-2 * Normal[2] * (self.body.Velocity[2] * Normal[2]))
      col = False

class plotting:
  def __init__(self, body, Wall):
    self.body = body
    self.history = [list(body.Position)]
    self.Wall = Wall

  def draw(self):
    self.history.append(list(self.body.Position))
    xs, ys, zs = zip(*self.history)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    x = np.linspace(-100, 100, 100)
    y = np.linspace(-100, 100, 100)
    X, Y = np.meshgrid(x, y)
    Z = self.Wall.Plane(X, Y)

    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)
    plt.show()
  
  def update(self, steps=100):
    for _ in range(steps):
      self.body.Acceleration()
      self.body.move()
      if self.body.Position[2] <= 0:
        self.body.deflectionFromGround()
      self.history.append(list(self.body.Position))
      self.Wall.VectorReflection()
    self.draw()
