
# Blender Metadata Exporter

**Blender Metadata Exporter** is a Blender addon that connects Blender-authored assets to an external, engine-agnostic asset validation pipeline.

The addon handles **DCC-side integration and asset metadata export only**.  
All validation logic runs outside Blender.

----------

## What It Does

-   Integrates with Blender’s UI (3D Viewport sidebar)
-   Exports selected mesh asset **metadata** to JSON
    

Blender-specific code is kept minimal and focused on authoring-time data extraction.

----------

## Pipeline Overview

`Blender (metadata export) → JSON → Asset  Validator` 

-   Blender: asset selection and metadata extraction
-   Asset Validator: rule evaluation and reporting
    

Core validation logic lives here:  
https://github.com/janikowski-dev/Asset-Validator

----------

## Design Principles

-   Clear separation between export and validation
-   No DCC-specific validation rules
-   Consistent JSON schema across tools
-   Reusable across pipelines and projects
    

----------

## Scope

This addon intentionally contains **no validation logic**.

It exists solely to bridge Blender with an external asset validation system.
