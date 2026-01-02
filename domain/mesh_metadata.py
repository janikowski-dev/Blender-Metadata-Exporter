from typing import TypedDict
from dataclasses import dataclass
from .metadata import Metadata


@dataclass()
class MeshMetadata(Metadata):
    vertex_count: int
    triangle_count: int
    ngon_count: int
    uv_map_count: int
    scale: tuple[float, float, float]
    rotation: tuple[float, float, float]

    def to_dict(self) -> dict[str, object]:
        return {
            "Mesh.VertexCount": self.vertex_count,
            "Mesh.TriangleCount": self.triangle_count,
            "Mesh.NgonCount": self.ngon_count,
            "UV.MapCount": self.uv_map_count,
            "Transform.Scale": [float(value) for value in self.scale],
            "Transform.RotationEuler": [float(value) for value in self.rotation],
        }