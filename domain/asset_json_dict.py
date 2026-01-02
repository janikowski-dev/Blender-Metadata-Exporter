from typing import TypedDict
from .asset_type import AssetType
from .metadata import Metadata


class AssetJsonDict(TypedDict):
    Type: str
    Name: str
    Path: str
    SizeInBytes: int
    Metadata: dict[str, object]