from vpython import *

c1 = canvas(title="Scene 1", width = 300, height = 300, center=vector(0,0,0))
c2 = canvas(title = "Scene 2", width = 100, height = 100, center = vector(5,0,0))

sphere(canvas = c1,radius = 0.5, pos=vector(0,2,0))
sleep(1)
sphere(canvas = c1,radius = 0.4, pos=vector(0,3,0))
sleep(1)
sphere(canvas = c1,radius = 0.3, pos=vector(0,4,0))
sleep(1)
sphere(canvas = c1,radius = 0.2, pos=vector(0,5,0))
sleep(1)
helix(canvas = c2)

