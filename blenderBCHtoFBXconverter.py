import bpy
import sys
 
#Get command line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:] # get all args after "—"
bvh_in = argv[0] 
fbx_out = argv[0].replace("ToConvert","Converted").replace(".bvh",".fbx")
 
# Import the BVH file
# See http://www.blender.org/documentation/blender_python_api_2_60_0/bpy.ops.import_anim.html
bpy.ops.import_anim.bvh(filepath=bvh_in, filter_glob="*.bvh", global_scale=1, frame_start=1, use_fps_scale=False, use_cyclic=False, rotate_mode='NATIVE', axis_forward='-Z', axis_up='Y')

# Testing Arguments
# print(argv[0])
# print(bvh_in)
# print(fbx_out)

# Export as FBX 
# See https://docs.blender.org/api/current/bpy.ops.export_scene.html
bpy.ops.export_scene.fbx(filepath=fbx_out, 
                            axis_forward='-Z', 
                            axis_up='Y', 
                            use_selection=True)
