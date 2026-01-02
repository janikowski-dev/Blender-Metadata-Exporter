import bpy
import json
from datetime import datetime
from bpy_extras.io_utils import ExportHelper
from typing import Iterable

from ..collectors.mesh_collector import collect_mesh_metadata
from ..domain.asset_type import AssetType
from ..domain.asset import Asset
from ..constants import OP_EXPORT_METADATA, UI_EXPORT_METADATA

JsonObject = dict[str, object]

class BME_OT_ExportMetadata(bpy.types.Operator, ExportHelper):  # type: ignore[misc]
    bl_idname = OP_EXPORT_METADATA
    bl_label = UI_EXPORT_METADATA

    filename_ext = ".json"
    filter_glob: str = bpy.props.StringProperty(
        default="*.json",
        options={'HIDDEN'}
    )

    def invoke(self, context: bpy.types.Context, event: bpy.types.Event) -> set[str]:
        self._set_default_filepath()
        super().invoke(context, event)
        return {'RUNNING_MODAL'}

    def execute(self, context: bpy.types.Context) -> set[str]:
        meshes = self._collect_meshes(context)

        if not meshes:
            self._report_fail()
            return {'CANCELLED'}

        self._export_to_file(meshes)
        self._report_success(len(meshes))
        return {'FINISHED'}

    def _set_default_filepath(self) -> None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filepath = f"Metadata_{timestamp}.json"

    def _collect_meshes(self, context: bpy.types.Context) -> list[Asset]:
        meshes: list[Asset] = []

        for selected_object in context.selected_objects:
            if selected_object.type.lower() != AssetType.MESH.lower():
                continue

            mesh = Asset(
                name=selected_object.name,
                path=f"Blender/{selected_object.name}.fbx",
                metadata=collect_mesh_metadata(selected_object).to_dict()
            )

            meshes.append(mesh)

        return meshes

    def _export_to_file(self, assets: list[Asset]) -> None:
        json_assets = [asset.to_json() for asset in assets]

        with open(self.filepath, "w", encoding="utf-8") as output_file:
            json.dump(json_assets, output_file, indent=2, ensure_ascii=False)

    def _report_fail(self) -> None:
        self.report({'WARNING'}, "No mesh objects selected")

    def _report_success(self, count: int) -> None:
        self.report({'INFO'}, f"Exported {count} assets")
