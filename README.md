# Blender Metadata Exporter

**Blender Metadata Exporter** is a Blender addon that connects Blender-authored assets to an external, engine-agnostic asset validation pipeline.

The addon handles **DCC-side integration and asset metadata export only**.  
All validation logic runs outside Blender.

---

## What It Does

- Integrates with Blender’s UI (3D Viewport sidebar)
- Exports selected mesh asset **metadata** to JSON

Blender-specific code is kept minimal and focused on authoring-time data extraction.

---

## Pipeline Overview

`Blender (metadata export) → JSON → Asset Validator`

- Blender: asset selection and metadata extraction  
- Asset Validator: rule evaluation and reporting  

Core validation logic lives here:  
https://github.com/janikowski-dev/Asset-Validator

---

## Design Principles

- Clear separation between export and validation
- No DCC-specific validation rules
- Consistent JSON schema across tools
- Reusable across pipelines and projects

---

## Scope

This addon intentionally contains **no validation logic**.

It exists solely to bridge Blender with an external asset validation system.

---

## Installation (for Artists)

### Requirements

- **Blender 3.x or newer**
- No additional dependencies required

---

### Installation Steps

1. **Download the addon**
   - Click **Code → Download ZIP** on this repository
   - Extract the ZIP file somewhere on your computer

2. **Open Blender**

3. Go to **Edit → Preferences**

4. Select the **Add-ons** tab

5. In the top-right corner, click the **down arrow (▼)** menu

6. Choose **Install from Disk…**

7. Select the extracted addon folder **or** the `.zip` file and confirm

8. Find **Blender Metadata Exporter** in the addon list and **enable it** (checkbox)

9. Close Preferences

---

### Verifying Installation

- Open the **3D Viewport**
- Press **`N`** to open the sidebar
- Look for a tab or panel labeled **Metadata Exporter**

If you see the exporter panel, the addon is installed correctly.

---

### Updating the Addon

1. Disable the addon in **Preferences → Add-ons**
2. Remove the old version
3. Install the new version using the steps above

---

### Notes for Artists

- This addon **does not validate assets inside Blender**
- It only **exports metadata**
- Validation results come from the external **Asset Validator** tool
- Validation errors usually mean:
  - required metadata is missing, or
  - naming / structure rules were violated

---

## For Technical Artists / Developers

- The addon is intentionally lightweight
- No validation rules should be added here
- Changes to metadata schema should stay in sync with the Asset Validator
- Blender code should remain focused on:
  - UI
  - selection
  - data extraction
  - JSON export
