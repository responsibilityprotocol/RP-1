# CHANGELOG.md

All notable changes to this repository are documented in this file.

This project intentionally changes at different speeds:
- Constitution and Articles are **slow-changing** (amendment governed).
- Handbook and Engine are **iterative** (clarity governed).
- Research whitepapers are **supplemental** (scholarship governed).

---

## 2025-12-17

### Fixed
- Index and README navigation hardened: added consistent, clickable links to canonical layers and subfolders.
- Normalized references to `ARTICLES/` subfolder placement and ensured filenames are referenced consistently.

### Notes
- This entry is an integrity hardening pass. No normative doctrine changes are implied by navigation fixes alone.

---
## 2025-10-30 — Repository Structure & Index Alignment

### Updated
- Rewrote `README.md` using stable, mobile-safe formatting.
- Replaced `RP-1_INDEX.md` with a fully linked version matching the exact repository file structure.

### Notes
- No changes were made to the content of constitutional articles, handbook documents, engine specifications, or EII framework.
- This update is **non-substantive**: formatting, navigation, and usability improvements only.

### Reason
These updates were made to ensure:
- Accurate internal references
- Consistent document hierarchy presentation
- Accessibility across GitHub mobile, desktop, and external markdown viewers

---

## 2025-10-30
### Added
- Added RESEARCH_WHITEPAPERS/ directory.
- Added RP-1_vs_EU_AI_Act_Comparative_Whitepaper.md.

### Updated
- README.md to reflect:
  - Accurate directory structure
  - Correct filenames and link paths
  - Inclusion of DIAGRAMS and Research sections
- RP-1_INDEX.md rebuilt to match repository exactly.

### No Changes
- No renames or relocations of EII_SPECIFICATION.md (remains separate from ENGINE).

---

## [Unreleased]
### New
- Added `/HANDBOOK/` directory containing the full RP-1 Handbook (Sections 00–10).
- Added Handbook reference tables to `README.md`, formatted to match the Articles section.
- Added linked Handbook entries to `RP-1_INDEX.md`, ensuring full navigability.

### Changed
- Updated `RP-1_INDEX.md` to use consistent *relative-path links* to all documents.
- Standardized terminology across Handbook entries for harm scale (H0–H5) and intervention tiers (T0–T2).
- Improved consistency of headings and phrasing in the Handbook to align with the Constitution’s tone and scope.

### Removed
- None.

---

## [v1.0.0] — Initial Public Structure
### New
- Added **RP-1 Constitution** establishing core ethical and structural commitments.
- Added `/ARTICLES/` directory containing Articles 01–06 as modular constitutional components.
- Added `EII_SPECIFICATION.md` defining the Ethical Integrity Infrastructure.
- Added supporting documents:
  - `APPENDIX_I_FOUNDATIONAL_PRINCIPLES.md`
  - `OATH_OF_CONTINUANCE.md`
  - `EPILOGUE_THE_LONG_CONTINUANCE.md`
- Added repository orientation + navigation index (`RP-1_INDEX.md`).

### Changed
- None (initial release).

### Removed
- None.