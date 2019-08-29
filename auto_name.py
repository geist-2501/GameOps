import bpy


class GO_OT_auto_name(bpy.types.Operator):
    """Add the correct suffixes automatically"""
    bl_idname = "object.go_ot_auto_name"
    bl_label = "Auto Name"
    bl_options = {'REGISTER', 'UNDO'}

    go_coll_high = "High"
    go_coll_low = "Low"

    go_suffix_high: bpy.props.StringProperty(name='High Poly Suffix', default='high')
    go_suffix_low: bpy.props.StringProperty(name='Low Poly Suffix', default='low')

    def execute(self, context):
        
        self.auto_name(self.go_coll_high)
        self.auto_name(self.go_coll_low)

        self.report({'INFO'}, 'Success!')
        return {'FINISHED'}

    def auto_name(self, coll_name):

        objs = bpy.data.collections[coll_name].all_objects

        for obj in objs:
            if coll_name == self.go_coll_high:
                obj.name = obj.name + '_' + self.go_suffix_high
            else:
                obj.name = obj.name + '_' + self.go_suffix_low
            pass

        pass

    pass