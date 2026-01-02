import bpy
from typing import Any

from ..constants import OP_EXPORT_METADATA


class BME_PT_MainPanel(bpy.types.Panel): # type: ignore[misc]
    bl_label = "Metadata Exporter"
    bl_idname = "BME_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Metadata Exporter'

    def draw(self, context: Any) -> None:
        self.layout.operator(OP_EXPORT_METADATA)
