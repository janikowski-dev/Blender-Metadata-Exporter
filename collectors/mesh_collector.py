import bpy
from ..domain.mesh_metadata import MeshMetadata


def collect_mesh_metadata(mesh: bpy.types.Object) -> MeshMetadata:
    dependencies_graph = bpy.context.evaluated_depsgraph_get()
    evaluated_object = mesh.evaluated_get(dependencies_graph)
    evaluated_mesh = evaluated_object.to_mesh()

    try:
        triangle_count = sum(
            len(poly.vertices) - 2
            for poly in evaluated_mesh.polygons
        )

        ngon_count = sum(
            1 for poly in evaluated_mesh.polygons
            if len(poly.vertices) > 4
        )

        uv_map_count = len(evaluated_mesh.uv_layers)
        vertex_count = len(evaluated_mesh.vertices)

    finally:
        evaluated_object.to_mesh_clear()

    return MeshMetadata(
        vertex_count=vertex_count,
        triangle_count=triangle_count,
        ngon_count=ngon_count,
        uv_map_count=uv_map_count,
        scale=tuple(mesh.scale),
        rotation=tuple(mesh.rotation_euler)
    )