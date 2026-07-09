# Universal Obsidian Import Toolkit (UNOBIT)

Last updated: 2026-07-09

Project status: Sprint 3 Completed
Current version: v0.3.0-sprint3
Next milestone: v0.4.0-beta

---

# Vision

UNOBIT is an open-source toolkit for importing knowledge from multiple platforms into Obsidian while preserving as much metadata, structure and attachments as possible.

Current focus:
- Evernote

Planned:
- OneNote
- Markdown
- Chrome Bookmarks
- Future plugin architecture

---

# Current Architecture

Importer
    ↓
Validation
    ↓
Processing
    ↓
Resolution
    ↓
Exporter

Supporting components

- ImportReport
- Performance reporting
- JSON report writer
- ENML conversion framework
- Test data generator

---

# Implemented

## Evernote

✔ ENEX parsing

✔ Attachments

✔ Markdown export

✔ Internal note links

✔ ENML conversion

✔ Todo conversion

✔ Media placeholders

✔ Attachment resolution

✔ Performance metrics

✔ JSON import report

---

# Testing

Unit tests

Integration tests

Regression ENEX files

Generated test fixtures

Large ENEX testing (>1GB)

Current status

All tests green

---

# Repository Structure

src/unobit

core/

enml/

exporters/

importers/

processors/

reporters/

resolvers/

validators/

tests/

tools/

docs/

---

# Technical Debt

Notebook / Stack support

Streaming importer

Duplicate attachment detection

Incremental import

Filename conflict handling improvements

Parallel processing

HTML report

GUI

Configuration system

Plugin API

---

# Risks

Very large ENEX files (>2 GB)

Very large attachments

Evernote HTML edge cases

Unsupported ENML elements

---

# Coding Principles

Small commits

Test first

Regression tests

Pipeline based architecture

Importer independent models

Separation of concerns

---

# Sprint Summary

Sprint 0

Repository setup

Sprint 1

Evernote MVP

Sprint 2

Pipeline architecture

Validation

ImportReport

Sprint 3

Reference Resolution

ENML framework

Media resolution

Performance metrics

Regression framework

Status: Complete

---

# Sprint 4 Goals

CLI redesign

Configuration (unobit.yaml)

HTML/JavaScript GUI

HTML report

Public beta packaging

Documentation polish

---

# Definition of Done (Beta)

CLI stable

Configuration file

GUI prototype

Performance report

JSON report

Documentation complete

Regression suite green

Large ENEX validated

GitHub release

PyPI-ready packaging

---

# Nice-to-have after Beta

OneNote importer

Markdown importer

Chrome Bookmarks importer

Plugin API

Streaming pipeline

Duplicate detection

Incremental synchronization