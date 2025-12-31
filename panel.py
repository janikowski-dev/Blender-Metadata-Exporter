import bpy


class BME_PT_MainPanel(bpy.types.Panel):
    bl_label = "Metadata Exporter"
    bl_idname = "BME_PT_main"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Metadata Exporter'

    def draw(self, context):
        self.layout.operator("metadataexporter.export_metadata")
