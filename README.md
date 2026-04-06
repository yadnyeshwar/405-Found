# 🏗️ MEP Guard — AI-Based Clash Detection & Rerouting System

Orchathon Hackathon 2025 | Team: 405-Found\*\*

---

## What This Does

Reads a real **Autodesk Revit IFC file**, extracts every pipe, duct, and cable tray in 3D, then:

1. Detects all clashes (physical overlaps + clearance violations)
2. Classifies severity using ASHRAE 90.1 / NFPA 13 / NBC India rules
3. Automatically reroutes clashing elements

---

## How to Load Your IFC File

```
Revit → File → Export → IFC → Save as model.ifc
python run.py --input model.ifc
```

That's it. The system handles everything else.

---

## Quick Start

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 2. Install dependencies
pip install flask flask-cors numpy pytest

# 3. Run with sample data (no IFC needed)
python run.py

# 4. Run with your real IFC file
python run.py --input path/to/model.ifc

# 5. Launch dashboard
python ui/dashboard.py
# Open http://localhost:5000
```

---

## Project Structure

```
mep-guard/
├── src/
│   ├── core/
│   │   ├── element.py         ← MEPElement, BoundingBox, Point3D
│   │   └── aabb_clash.py      ← AABB clash detection engine
│   ├── dataset/
│   │   └── generator.py       ← Synthetic MEP model (7 clash zones)
│   ├── parser/
│   │   └── ifc_parser.py      ← Real IFC file parser (IfcOpenShell)
│   ├── rerouting/
│   │   └── rerouter.py        ← Z-offset + lateral shift rerouting
│   └── rules/
│       └── rule_engine.py     ← ASHRAE/NFPA/NBC India standards
├── ui/
│   ├── dashboard.py                 ← Flask REST API (9 endpoints)
│
├── run.py                     ← Main pipeline entry point
└── requirements.txt
```

---

## Clash Types Detected

| Type               | Detected | Rerouted   |
| ------------------ | -------- | ---------- |
| Pipe vs Pipe       | ✅       | ✅         |
| Duct vs Duct       | ✅       | ✅         |
| Pipe vs Duct       | ✅       | ✅         |
| Cable Tray vs Pipe | ✅       | ✅         |
| Cable Tray vs Duct | ✅       | ✅         |
| MEP vs Structure   | ✅       | ⚠️ flagged |
| Soft (clearance)   | ✅       | ✅         |

---

## Algorithm

```
AABB Overlap Test:
Two elements CLASH if ALL are true:
  A.max_x > B.min_x  AND  A.min_x < B.max_x
  A.max_y > B.min_y  AND  A.min_y < B.max_y
  A.max_z > B.min_z  AND  A.min_z < B.max_z

Soft clash: expand bounding box by clearance_mm, then overlap test.
```

---
