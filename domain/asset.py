from dataclasses import dataclass
from .mesh_metadata import MeshMetadata
from .asset_json_dict import AssetJsonDict
from .asset_type import AssetType


@dataclass(frozen=True)
class Asset:
    name: str
    path: str
    metadata: dict[str, object]
    size_in_bytes: int = 0


    def to_json(self) -> AssetJsonDict:
        return {
            "Type": AssetType.MESH,
            "Name": self.name,
            "Path": self.path,
            "SizeInBytes": self.size_in_bytes,
            "Metadata": self.metadata,
        }