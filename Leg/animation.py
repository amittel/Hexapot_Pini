from vpython import *

scene = canvas(title='Leg Animation', background=color.white, forward=vector(0,1,0), up=vector(0,0,1))

#x red y green z blue


ref_x = arrow(pos= vector(0,0,0), axis=vector(2,0,0), color= color.red)
text(text='x', pos=vec(2,0,0), color=color.red, height=0.5,billboard=True)
ref_y = arrow(pos= vector(0,0,0), axis=vector(0,2,0), color= color.green)
text(text='y', pos=vec(0,2,0), color=color.green, height=0.5,billboard=True)
ref_z = arrow(pos= vector(0,0,0), axis=vector(0,0,2), color= color.blue)
text(text='z', pos=vec(0,0,2), color=color.blue, height=0.5,billboard=True)

#alphaJoint = sphere(pos= vector(0,0,0), radius= 0.5, color=color.red)
#betaJoint = sphere(pos=vector(-3,4,0), radius=0.5, color = color.orange)
#gammaJoint = sphere(pos=vector(-6,6,0), radius=0.5, color= color.green)
scalefactor= 100
l_c = 0.035 * scalefactor
l_f = 0.065* scalefactor
l_t = 0.096* scalefactor

alphaP = vector(0,0,0)
betaP = vector(l_c,0,0)
gammaP = vector(l_f,0,0)
footP = vector(l_t,0,0)

#p1 = dict(pos=v1, color=color.red,  radius=0.1)
#p2 = dict(pos=v2, color=color.blue, radius=0.1)
#p3 = dict(pos=v3, color=color.blue, radius=0.1)

c = curve(visible=True, radius=0.1)
c.append(alphaP, betaP, gammaP, footP)
z=vector(0,0,1)
angle = 0.1
i =0
while (i <= 100):
    rate(10)
  

    c.rotate(angle=angle, axis = z)
    
    print("Angle: ", angle)
    i = i+1