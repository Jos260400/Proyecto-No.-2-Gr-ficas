#Univerversidad del Valle de Guatemala
#Graficas por Computadoras
#Proyecto No. 2
#Fernando Jose Garavito Ovando 18071

from gl import Raytracer, V3
from obj import *
from figures import *

# Dimensiones
width = 512
height = 512

# Materiales
wood = Material(diffuse = (0.6,0.2,0.2), spec = 1)
stone = Material(diffuse = (0.4,0.4,0.4), spec = 1)

gold = Material(diffuse = (1, 0.8, 0 ),spec = 1, matType = REFLECTIVE)
mirror = Material(spec = 1, matType = REFLECTIVE)

water = Material(spec = 1, ior = 1, matType = TRANSPARENT)
glass = Material(spec = 1, ior = 1, matType = TRANSPARENT)
diamond = Material(spec = 1, ior = 2, matType = TRANSPARENT)

redball = Material(texture = Texture('red.bmp'))
metallicball = Material(texture = Texture('themetal.bmp'))
normalball = Material(texture = Texture('thenormal.bmp'))
bitball = Material(texture = Texture('the8bit.bmp'))
stoneball = Material(texture = Texture('thestone.bmp'))
box = Material(texture = Texture('wood.bmp'))


# Inicializacion
rtx = Raytracer(width,height)
rtx.envmap = EnvMap('room.bmp')


# Luces
rtx.ambLight = AmbientLight(strength = 0.1)
rtx.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 1)
rtx.pointLights.append( PointLight(position = V3(0, 2, 0), intensity = 1))

# Objetos
rtx.scene.append( Sphere(V3(-3,-2.5,-8), 0.2, stoneball) )
rtx.scene.append( Sphere(V3(-2.5,-2.5,-8), 0.2, stoneball) )
rtx.scene.append( Sphere(V3(-2,-2.5,-7), 0.2, metallicball) )
rtx.scene.append( Sphere(V3(-1.5,-2.5,-8), 0.2, normalball) )
rtx.scene.append( Sphere(V3(-1,-2.5,-8), 0.2, bitball) )
rtx.scene.append( Sphere(V3(-0.5,-2.5,-6), 0.2, redball) )
rtx.scene.append( Sphere(V3(-0.25,-2.5,-6), 0.2, redball) )
rtx.scene.append( Sphere(V3(0,-2.5,-8), 0.2, stoneball) )
rtx.scene.append( Sphere(V3(0.25,-2.5,-8), 0.2, stoneball) )
rtx.scene.append( Sphere(V3(0.5,-2.5,-6), 0.2, metallicball) )
rtx.scene.append( Sphere(V3(1,-2.5,-5), 0.2, normalball) )
rtx.scene.append( Sphere(V3(1.5,-2.5,-8), 0.2, bitball) )
rtx.scene.append( Sphere(V3(2,-2.5,-7), 0.2, redball) )
rtx.scene.append( Sphere(V3(2.5,-2.5,-7), 0.2, redball) )

rtx.scene.append( AABB(V3(0,-3,-8), V3(8,0.1,5), box) )

 
# Terminar
rtx.glRender()
rtx.glFinish('Proyecto No. 2.bmp')



