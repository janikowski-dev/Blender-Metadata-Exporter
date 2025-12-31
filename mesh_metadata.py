import bpy


def collect_mesh_metadata(mesh: bpy.types.Object) -> dict:
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

        rotation_applied = mesh.rotation_euler == (0.0, 0.0, 0.0)
        scale_applied = mesh.scale == (1.0, 1.0, 1.0)
        uv_map_count = len(evaluated_mesh.uv_layers)
        vertex_count = len(evaluated_mesh.vertices)

    finally:
        evaluated_object.to_mesh_clear()

    return {
        "Mesh.VertexCount": vertex_count,
        "Mesh.TriangleCount": triangle_count,
        "Mesh.NgonCount": ngon_count,
        "UV.MapCount": uv_map_count,
        "Transform.ScaleApplied": scale_applied,
        "Transform.RotationApplied": rotation_applied
    }
