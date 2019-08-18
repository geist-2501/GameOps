import bpy


class GO_PT_Panel(bpy.types.Panel):
    bl_idname = "object.go_pt_panel"
    bl_label = "GameOps"
    bl_category = "Utilities"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator('object.go_ot_zip_splits', text="Zip Splits")
        row = layout.row()
        row.operator('object.go_ot_gen_meshes', text="Generate Meshes")
