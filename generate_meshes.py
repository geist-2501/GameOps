import bpy

class GO_OT_gen_meshes(bpy.types.Operator):
    """Generate a high and low poly mesh from the source mesh"""
    bl_idname = "object.GO_OT_gen_meshes"
    bl_label = "Generate Meshes"


    def execute(self, context):
        return {'FINISHED'}