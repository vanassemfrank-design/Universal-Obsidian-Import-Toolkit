# UNOBIT Roadmap

## Vision

Build the most reliable open-source toolkit for migrating knowledge into Obsidian while preserving content, metadata, attachments, links and history.

---

# Sprint 0 — Repository Foundation

**Status:** ✅ Completed

- Repository structure
- CLI foundation
- Packaging
- Documentation
- Configuration foundation
- Localization foundation

---

# Sprint 1 — Evernote MVP

**Status:** ✅ Completed

- Universal Knowledge Model
- ENEX parser
- Markdown exporter
- Attachment export
- YAML Frontmatter
- Localization support

---

# Sprint 2 — Processing Engine

**Status:** ✅ Completed

## Core

- ImportReport
- PipelineContext
- ProcessingPipeline
- PipelineFactory

## Validation

- Validation framework
- Validators
- Processing framework

## Testing

- Unit tests
- Integration tests

## Documentation

- Architecture documentation
- ADR foundation

---

# Sprint 3 — Evernote Production Ready

**Status:** ✅ Completed

## Added

- Pipeline integration
- Reference Resolution
- ENML conversion framework
- Internal Evernote links
- Media placeholder resolution
- Performance metrics
- JSON reports
- Regression framework
- Large ENEX validation

### Goal achieved

A user can archive Evernote completely and continue working only in Obsidian.

---

# Sprint 4 — CLI, Configuration & Beta Foundation

**Status:** ✅ Completed

## Added

- Nested CLI command structure
- ImportService abstraction
- `unobit.yaml` configuration
- Configuration validation
- HTML report generation
- HTML/JavaScript GUI prototype
- Report viewer
- CLI integration tests
- ImportService tests

### Goal achieved

Stable beta-ready architecture for command line usage and local GUI prototype.

---

# Sprint 5 — Public Beta & User Experience

**Status:** Planned

## 5.1 Professional HTML Reports

- Responsive report layout
- CSS styling
- Summary dashboard
- Warnings and errors tables
- Pipeline timings
- Performance overview
- Print-friendly output

## 5.2 GUI Import Wizard

- Select archive
- Select output folder
- Configuration options
- Import progress
- Start import

## 5.3 GUI Report Viewer

- Import summary
- Open HTML report
- Open output folder
- Import another archive

## 5.4 System Doctor

New command:

```text
unobit doctor
```

Checks:

- Python installation
- Dependencies
- Configuration
- Output permissions
- GUI availability
- Report writers

## 5.5 Beta Packaging

- Packaging cleanup
- Example configuration
- Installation improvements
- Release preparation

## 5.6 Documentation

- README
- User Guide
- Developer Guide
- FAQ
- Public Beta Checklist

## 5.7 Public Beta Release

### Definition of Done

- All tests green
- GUI functional
- HTML reports complete
- Documentation complete
- Large ENEX validated
- Public beta release

---

# Sprint 6 — AI Enhancement

- Automatic tagging
- Duplicate detection
- Metadata enrichment
- Knowledge graph support

---

# Sprint 7 — Community Edition

- Plugin SDK
- CI/CD
- Package distribution
- Example plugins
- Community extensions