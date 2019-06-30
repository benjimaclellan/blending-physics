# Simple Brownian Motion in Blender

In this first tutorial we will create 
Open new file.

![Image](images/brownian_1.png)

Delete Default Cube and Default Light - we will make our own. I also used Cycles Render here, which is an excellent render engine, but the new Eevee engine has some great features as well. 

Add IcoSphere and change Subdivisions > 3
Change name to Particle

Go to Modifiers, Add Subdivision Surface, then Displace, then another Subdivision Surface
The Displace modifier should have a Texture, which we can leave as the Default name of Texture. This is what will actually give us some bumpiness in our 'particle'
Switch to Texture, and the texture which is being used by the Displace Modifier should be open (if not, change the current texture). Switch to a Voronoi texture and reduce the Intensity to around 0.4. Now we have a bumpy-ish sphere. And now let's add a quick Material. 

Navigate to Materials and add a Principled Shader. We will just use a simple metallic-type material, as below. 

Now we'll quickly add a floor and a light.

For the floor, we add a Plane, scale by 15, and move down Z by -1. We then add a simple Material which is meant to look kinda of like a matte gold finish.
For the 360 lights, we add a cylinder and scale by 15. Set the Material to Emission with Strength 1.0. One of the things with physics simulations is that they often represent things which humans have never seen directly - and are instead models. This means that there is plenty of creative control with the scene, so materials, geometry, and texture are largely up to you. This is not meant to be a photo-realistic image. Plus this tutorial is more about the scripting. 

So now our scene is set, lets get to the scripting and making our objects move.




