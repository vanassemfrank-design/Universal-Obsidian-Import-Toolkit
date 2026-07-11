# Universal Obsidian Import Toolkit (UNOBIT)

Last updated: 2026-07-11

**Current Version:** v0.4.0-dev

**Current Milestone:** Sprint 4 Completed

**Next Milestone:** Sprint 5 — Public Beta & User Experience

---

# Vision

**Import once. Preserve forever.**

UNOBIT is an open-source toolkit that migrates knowledge from multiple platforms into Obsidian while preserving metadata, attachments, links and history.

## Current production focus

- Evernote

## Planned

- OneNote
- Markdown
- ChatGPT exports
- Chrome Bookmarks
- Plugin architecture

---

# Current Architecture

```text
CLI / GUI
      │
      ▼
 ImportService
      │
      ▼
   Importer
      │
      ▼
 Validation
      │
      ▼
 Processing
      │
      ▼
 Resolution
      │
      ▼
  Exporter
      │
      ▼
 Reports
```

## Supporting Components

- Configuration system
- Processing Pipeline
- ImportReport
- JSON Report
- HTML Report
- Performance monitoring
- ENML conversion framework

---

# Current Functionality

## Evernote

- ✅ ENEX parsing
- ✅ Attachments
- ✅ Metadata
- ✅ Markdown export
- ✅ Internal links
- ✅ ENML conversion
- ✅ Todo conversion
- ✅ Media resolution
- ✅ YAML Frontmatter

## CLI

- ✅ Nested command structure
- ✅ Import commands
- ✅ Configuration commands
- ✅ Report commands
- ✅ GUI launcher

## GUI

- ✅ Local HTML prototype
- ✅ JSON report viewer

## Reporting

- ✅ JSON report
- ✅ HTML report
- ✅ Performance metrics
- ✅ Pipeline timings

---

# Testing

- ✅ Unit tests
- ✅ Integration tests
- ✅ CLI tests
- ✅ ImportService tests
- ✅ Regression tests
- ✅ Large ENEX archives (>1 GB)

**Current Status:** All tests green.

---

# Technical Debt

- Professional HTML report
- GUI Import Wizard
- GUI Report Viewer
- Streaming importer
- Notebook / Stack support
- Duplicate attachment detection
- Incremental import
- Plugin API

---

# Risks

- Extremely large ENEX archives (>2 GB)
- Unsupported ENML edge cases
- Very large attachments
- Platform-specific filesystem limitations

---

# Coding Principles

- Small commits
- Test first
- Regression testing
- Pipeline architecture
- Importer-independent models
- Separation of concerns
- Configuration over hardcoded behaviour

---

# Definition of Done (Public Beta)

- Stable CLI
- Stable configuration
- HTML reports
- Functional GUI
- Documentation complete
- All tests green
- Large ENEX validated
- GitHub beta release