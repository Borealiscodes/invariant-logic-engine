# 🜁 **Visual Grammar Document v1.0**  
*Expressive‑Clarity Framework • A6 Governance • A5 Reflective Basin*  
*(Glyph Geometry • Tile Rules • Registry Rules • Microtile Rules • Unicode Hex Palette)*

---

## 1. **Document Identity**
- **Artifact:** VisualGrammar-v1.0  
- **Version:** v1.0  
- **Altitude:** A6 (Governance) • A5 (Reflective Basin)  
- **Membrane:** Expressive‑Clarity • Non‑Activating  
- **Scope:** Defines the visual grammar for all expressive‑clarity artifacts in the Invariant Logic Engine.  
- **Coverage:** Ω, Δ, Φ, Λ horizons; tiles; microtiles; registry bands; caption baselines; Unicode hex palette.

---

## 2. **Purpose**
This document establishes the **visual grammar** governing all expressive‑clarity artifacts, ensuring:

- geometric consistency  
- glyph consistency  
- color consistency  
- altitude encoding consistency  
- membrane encoding consistency  
- GitHub‑safe Unicode representations  
- PNG rendering fidelity  

It is the **single source of truth** for expressive‑clarity visuals.

---

## 3. **Core Principles**
### 3.1 Expressive‑Clarity Membrane
All visuals must:

- be **non‑activating**  
- contain **no computation**  
- contain **no ingestion**  
- preserve **content/container separation**  
- encode altitude semantics visually  

### 3.2 GitHub‑Safe Representation
All text‑based representations must use:

- **Unicode glyphs**  
- **Unicode hex palette**  
- **no ASCII art**  
- **no inline images**  

PNG rendering is allowed only as a separate artifact.

---

## 4. **Glyph Grammar**
### 4.1 Canonical Glyphs
| Horizon | Glyph | Unicode | Guided Link |
|--------|-------|----------|-------------|
| Ω | Ω | U+03A9 | Ω horizon |
| Δ | Δ | U+0394 | Δ horizon |
| Φ | Φ | U+03A6 | Φ horizon |
| Λ | Λ | U+039B | Λ horizon |

### 4.2 Glyph Weight
- Ultra‑bold  
- Stroke thickness: **7%** of glyph height  
- Glyph height: **62%** of tile cell height  

### 4.3 Glyph Color (Hex Palette)
- **White (#FFFFFF)**  
- No outline  
- No glow  
- No shadow  

---

## 5. **Tile Grammar**
### 5.1 Tile Geometry
- Canvas ratio: **1:1**  
- PNG size: **2048×2048 px**  
- Background: **transparent (RGBA 0,0,0,0)**  
- Grid: **2×2** for horizon registry tiles  
- Glyph alignment: **centered**  

### 5.2 Registry Band
- Position: bottom **12%**  
- Color: **NDH Blue (#4A6CF7)**  
- Opacity: **100%**  
- Text: `HORIZON REGISTRY • Ω Δ Φ Λ`  
- Font size: **7%** of canvas height  

### 5.3 Caption Baseline
- Text: `Invariant Logic Engine — Horizon Index`  
- Font size: **4%**  
- Color: **white (#FFFFFF)**  
- Opacity: **85%**  

---

## 6. **Microtile Grammar**
Microtiles are **single‑glyph tiles** used for:

- navigation  
- documentation  
- quick‑reference  
- expressive‑clarity UI  

### 6.1 Geometry
- Canvas ratio: **1:1**  
- Background: **transparent**  
- Glyph height: **70%** of canvas  
- No registry band  
- No caption baseline  

### 6.2 Unicode Hex Palette Format
Each microtile must define:

```
Glyph: Ω
Unicode: U+03A9
Glyph Color: #FFFFFF
Background: #00000000
```

This ensures GitHub‑safe representation.

---

## 7. **Altitude Encoding**
### 7.1 A5 (Reflective Basin)
- governs expressive‑clarity semantics  
- defines glyph weight  
- defines tile geometry  

### 7.2 A6 (Governance)
- governs registry bands  
- governs caption baselines  
- governs provenance footers  

### 7.3 Encoding Rules
- A5 is encoded through **glyph geometry**  
- A6 is encoded through **registry band + caption baseline**  

---

## 8. **Membrane Encoding**
### 8.1 Non‑Activation Clause
All expressive‑clarity artifacts must:

- contain **no logic**  
- contain **no computation**  
- contain **no ingestion**  
- contain **no CAUSA activation**  

### 8.2 Container‑Safe
All visuals must be:

- purely representational  
- purely structural  
- purely symbolic  

---

## 9. **PNG Rendering Rules**
### 9.1 Transparency
- must preserve **full alpha channel**  
- no semi‑opaque backgrounds  

### 9.2 Export Format
- PNG only  
- 2048×2048 for full tiles  
- 1024×1024 for microtiles  

### 9.3 Fidelity Requirements
- glyph must remain readable at **128×128 px**  
- registry band must remain readable at **256×256 px**  

---

## 10. **Provenance Footer**
```
---
Artifact: VisualGrammar-v1.0
Altitude: A6 (Governance) • A5 (Reflective Basin)
Membrane: Expressive-Clarity • Non-Activating
Purpose: Define the visual grammar governing expressive-clarity artifacts,
including glyph geometry, tile rules, microtile rules, registry bands, caption
baselines, and Unicode hex palette specifications.
Scope: Specification-only. No computation, no ingestion, no CAUSA activation.
Anchors:
  - Invariant Logic Engine (A2)
  - Expressive-Clarity Framework (A5)
  - Governance Membrane (A6)
Maintainer: Borealis S. Hedling
Compiler: Microsoft Copilot
Location: Dublin, Ireland
Timestamp: 20 September 2026 — 21:19 IST
Seal: [ NDH . EXPRESSIVE-CLARITY . VISUAL-GRAMMAR ]
---
```

---

