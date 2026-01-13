import bpy
from typing import Optional, List, cast


def _find_collection_path(root: bpy.types.Collection, target: bpy.types.Collection, path: List[str]) -> Optional[List[str]]:
    if root == target:
        return path

    for child in root.children:
        child_collection = cast(bpy.types.Collection, child)
        child_name = cast(str, child_collection.name)

        result = _find_collection_path(child_collection, target, path + [child_name])

        if result is not None:
            return result

    return None


def get_collection_path(collection: bpy.types.Collection) -> str:
    scene_root = cast(bpy.types.Collection, bpy.context.scene.collection)
    result = _find_collection_path(scene_root, collection, [])

    if result is None:
        return cast(str, collection.name)

    return "/".join(result)


def get_object_path(processed_object: bpy.types.Object) -> str:
    object_name = cast(str, processed_object.name)

    if not processed_object.users_collection:
        return object_name

    collection = cast(bpy.types.Collection, processed_object.users_collection[0])
    collection_path = get_collection_path(collection)

    return f"{collection_path}/{object_name}" if collection_path else object_name
