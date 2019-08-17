import bpy
import mathutils


class GO_OT_zip_splits(bpy.types.Operator):
    
    """Eliminate small gaps in meshes"""
    bl_idname = "object.go_ot_zip_splits"
    bl_label = "Zip Splits"
    bl_options = {'REGISTER', 'UNDO'}

    merge_dist : bpy.props.FloatProperty(name="Group distance", default=0.01)
    
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

    def execute(self, context):
        zip(self.merge_dist)
        self.report({'INFO'}, 'Splits zipped!')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        ob = context.active_object  
        return ob is not None and ob.mode == 'EDIT' 
    
def merge_verts(v1, v2):
    #Find average co.
    avg_x = (v1.co.x + v2.co.x) / 2
    avg_y = (v1.co.y + v2.co.y) / 2
    avg_z = (v1.co.z + v2.co.z) / 2
    
    v1.co = (avg_x, avg_y, avg_z)
    v2.co = (avg_x, avg_y, avg_z)
    pass

def zip(dist):
    print("zipping!")
    
    objs = bpy.context.objects_in_mode

    bpy.ops.object.editmode_toggle()

    mesh_data = []
    for obj in objs:
        mesh_data += obj.data.vertices
        
        
    size = len(mesh_data)
    kd = mathutils.kdtree.KDTree(size)

    for i, v in enumerate(mesh_data):
        kd.insert(v.co, i)

    kd.balance()

    

    for vert in mesh_data:
        close_verts = kd.find_range(vert.co, dist)

        #First vert is the vert itself.
        if len(close_verts) == 2:
            merge_vert = close_verts[1]
            v2 = mesh_data[merge_vert[1]]
            merge_verts(vert, v2)
        
    bpy.ops.object.editmode_toggle()
    pass
    

