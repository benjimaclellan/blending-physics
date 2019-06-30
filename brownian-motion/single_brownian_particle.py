## Import the Blender Python library, MathUtils for Vectors, and numpy to use
import bpy
import mathutils as mu
from mathutils import Matrix
import numpy as np

## These are our main parameters for the simulation
NUM_FRAMES          = 250 # the total number of frames to animate for
SKIP_FRAMES         = 2 # this controls how many locations to set as keyframes
BROWN_LOC_STRENGTH  = 0.2 # this is a dimensionless unit which controls how much the particle can move from the current position
BROWN_ROT_STRENGTH  = 0.25 # this is a dimensionless unit which controls how much the particle can move from the current position
LOC_SWITCH          = np.array([1, 1, 0]) # (X,Y,Z) Boolean values to constrain certain dimensions


## Now we get into changing the Blender settings
scene = bpy.context.scene # set a shorter variable to the whole scene

scene.frame_start, scene.frame_end = (1, NUM_FRAMES) # set our animation frame lengths
bpy.context.scene.frame_set(scene.frame_start) # move to the first frame

## Let's now ensure our Particle object is centered, and remove any old animations (if the script has been run multiple times)
obj = bpy.data.objects['Particle']
obj.delta_location = mu.Vector([0,0,0])
obj.location = mu.Vector([0,0,0])
obj.animation_data_clear()


def random_rot_loc_change(obj, BROWN_LOC_STRENGTH, BROWN_ROT_STRENGTH, INTERPOLATION):
    ## Calculate a random change from the current location, drawn from a normal distribution (and fixed in the desired dimensions)

    loc_mat = mu.Matrix.Translation(list(np.random.normal(0, BROWN_LOC_STRENGTH, 3) *  LOC_SWITCH))


    rot_mat = mu.Matrix.Rotation(np.random.normal(0,BROWN_ROT_STRENGTH), 4, 'X') @ mu.Matrix.Rotation(np.random.normal(0,BROWN_ROT_STRENGTH), 4, 'Y') @ mu.Matrix.Rotation(np.random.normal(0,BROWN_ROT_STRENGTH), 4, 'Z') 

    # decompose world_matrix's components, and from them assemble 4x4 matrices
    orig_loc, orig_rot, orig_scale = obj.matrix_world.decompose()
    orig_loc_mat = mu.Matrix.Translation(orig_loc)
    orig_rot_mat = orig_rot.to_matrix().to_4x4()
    orig_scale_mat = Matrix.Scale(orig_scale[0],4,(1,0,0)) @ Matrix.Scale(orig_scale[1],4,(0,1,0)) @ Matrix.Scale(orig_scale[2],4,(0,0,1))

    obj.matrix_world = loc_mat @ orig_loc_mat @ rot_mat @ orig_rot_mat @ orig_scale_mat
        
    obj.keyframe_insert(data_path="location")
    obj.keyframe_insert(data_path="rotation_euler")
     
    ## Change the interpolation type for smooth movement
    for fcurve in obj.animation_data.action.fcurves:
        kf = fcurve.keyframe_points[-1]
        kf.interpolation = INTERPOLATION



## Now we loop through each frame where we want the particle to have a new location
for frame in range(scene.frame_start, scene.frame_end+1, SKIP_FRAMES):
    
    # move to the current frame
    bpy.context.scene.frame_set(frame)
    random_rot_loc_change(obj, BROWN_LOC_STRENGTH, BROWN_ROT_STRENGTH, 'BEZIER')
    
