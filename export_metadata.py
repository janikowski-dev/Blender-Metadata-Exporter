import bpy
import json
from datetime import datetime
from bpy_extras.io_utils import ExportHelper
from .mesh_metadata import collect_mesh_metadata


class BME_OT_ExportMetadata(bpy.types.Operator, ExportHelper):
    bl_idname = "metadataexporter.export_metadata"
    bl_label = "Export Metadata"

    filename_ext = ".json"
    filter_glob: bpy.props.StringProperty(
        default="*.json",
        options={'HIDDEN'}
    )

    def invoke(self, context, event):
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filepath = f"Metadata_{timestamp}.json"
        return super().invoke(context, event)

    def execute(self, context):
        assets = []

        for exported_object in context.selected_objects:
            if exported_object.type != 'MESH':
                continue

            assets.append({
                "Type": "Mesh",
                "Name": exported_object.name,
                "Path": f"Blender/{exported_object.name}.fbx",
                "SizeInBytes": 0,
                "Metadata": collect_mesh_metadata(exported_object),
            })

        if not assets:
            self.report({'WARNING'}, "No mesh objects selected")
            return {'CANCELLED'}

        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(assets, f, indent=2, ensure_ascii=False)

        self.report({'INFO'}, f"Exported {len(assets)} assets")
        return {'FINISHED'}
