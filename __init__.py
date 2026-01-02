bl_info = {
    "name": "Metadata Exporter",
    "author": "Adam Janikowski",
    "version": (1, 1, 0),
    "blender": (4, 5, 0),
    "location": "View3D > Sidebar > Metadata Exporter",
    "description": "Exports asset metadata",
    "category": "Object",
}

import bpy
from .ui.panel import BME_PT_MainPanel
from .operators.export_metadata import BME_OT_ExportMetadata

classes = (
    BME_PT_MainPanel,
    BME_OT_ExportMetadata
)

def register() -> None:
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister() -> None:
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
