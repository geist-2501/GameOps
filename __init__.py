# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy

from . button_panel import GO_PT_Panel
from . zip_splits import GO_OT_zip_splits
from . generate_meshes import GO_OT_gen_meshes
from . auto_name import GO_OT_auto_name

classes = (GO_PT_Panel, GO_OT_zip_splits, GO_OT_gen_meshes, GO_OT_auto_name)

register, unregister = bpy.utils.register_classes_factory(classes)

bl_info = {
    "name": "GameOps",
    "author": "geist-2501",
    "description": "A suite of tools for HardOps game asset modelling.",
    "blender": (2, 80, 0),
    "version": (0, 0, 4),
    "location": "Toolshelf > Utilities",
    "warning": "",
    "category": "View3D"
}