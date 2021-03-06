import bpy


class GO_OT_gen_meshes(bpy.types.Operator):
    """Generate a high and low poly mesh from the source mesh"""
    bl_idname = "object.go_ot_gen_meshes"
    bl_label = "Generate Meshes"
    bl_options = {'REGISTER', 'UNDO'}

    go_coll_high = "High"
    go_coll_low = "Low"

    def execute(self, context):

        # Use for naming objects.
        name_img = bpy.data.collections[0].all_objects

        # Make the collections and fill them.
        self.make_collections(self.go_coll_high)
        self.make_collections(self.go_coll_low)

        # Switch to the High collection and select everything.
        bpy.ops.object.hide_collection(bpy.data.collections.find(self.go_coll_high))
        sel = bpy.data.collections[self.go_coll_high].all_objects

        # Apply modifiers.
        for obj in sel:
            bpy.context.view_layer.objects.active = obj
            for mod in obj.modifiers:
                mod_name = mod.name
                bpy.ops.object.modifier_apply(modifier=mod_name)
                pass
            pass

        # Switch to the Low collection and select everything.
        bpy.ops.object.hide_collection(bpy.data.collections.find(self.go_coll_low))
        sel = bpy.data.collections[self.go_coll_low].all_objects

        # Edit / remove modifiers.
        for obj in sel:
            bpy.context.view_layer.objects.active = obj
            for mod in obj.modifiers:
                mod_name = mod.name

                # Remove bevels for a low poly.
                if mod.type == 'BEVEL':
                    bpy.ops.object.modifier_remove(modifier=mod_name)
                    pass
                
                # Reduce subD for a low poly.
                if mod.type == 'SUBSURF':
                    mod.levels = 1
                    pass
                
                pass
            pass

        # Apply modifiers.
        for obj in sel:
            bpy.context.view_layer.objects.active = obj
            for mod in obj.modifiers:
                mod_name = mod.name
                bpy.ops.object.modifier_apply(modifier=mod_name)
                pass
            pass

        # Split the mesh up.
        self.auto_split(self.go_coll_high)
        self.auto_split(self.go_coll_low)

        self.report({'INFO'}, 'Success!')
        return {'FINISHED'}

    @classmethod
    def poll(cls, context):
        ob = context.active_object
        return ob is not None and ob.mode == 'OBJECT'

    def make_collections(self, name):

        present = bpy.data.collections.find(name)
        # present is -1 if the collection doesn't exist.

        if present == -1:  # Create collection.

            bpy.ops.object.collection_objects_select()
            bpy.ops.object.duplicate()
            bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name=name)

        else:  # Wipe collection.

            objs = bpy.data.collections[name].all_objects
            for obj in objs:
                bpy.data.objects.remove(obj)
                pass
            pass

            bpy.data.collections.remove(bpy.data.collections[name])

            bpy.ops.object.collection_objects_select()
            bpy.ops.object.duplicate()
            bpy.ops.object.move_to_collection(collection_index=0, is_new=True, new_collection_name=name)

            pass

        pass

    def auto_split(self, coll_name):

        self.deselect()

        objs = bpy.data.collections[coll_name].all_objects

        for obj in objs:
            obj.select_set(True)
            pass

        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.separate(type='LOOSE')
        bpy.ops.object.editmode_toggle()

        pass

    def deselect(self):
        for ob in bpy.context.selected_objects:
            ob.select_set(False)
            pass
        pass

    def select_all(self, objs):
        for obj in objs:
            obj.select_set(True)
            pass
        pass 