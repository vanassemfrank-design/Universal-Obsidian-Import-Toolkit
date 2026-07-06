# Universal Obsidian Import Toolkit (UNOBIT)

> Import your knowledge. Preserve your history.

## Overview

Universal Obsidian Import Toolkit (UNOBIT) is an open-source toolkit that imports knowledge from multiple platforms into a structured Obsidian vault while preserving metadata, attachments, relationships, and history.

The project is designed around one core principle:

> **Import once, preserve forever.**

Instead of creating one-off conversion scripts for individual platforms, UNOBIT converts every supported source into a universal internal note model. This allows new importers to be added without changing the rest of the application.

---

# Goals

* Preserve as much information as possible during migration.
* Support multiple knowledge platforms.
* Produce clean, readable Markdown.
* Preserve attachments and media.
* Preserve metadata.
* Preserve relationships between notes.
* Generate validation reports after every import.
* Be extensible through a plugin architecture.

---

# Supported Sources (planned)

* Evernote (.enex)
* Notion
* ChatGPT exports
* OneNote
* HTML
* Markdown
* Microsoft Word
* PDF
* Google Docs
* Generic ZIP archives

---

# Core Features

* Universal internal note model
* Modular importer architecture
* Metadata preservation
* Attachment management
* WikiLink restoration
* YAML frontmatter generation
* Duplicate detection
* Broken link reporting
* Import validation reports
* Batch processing
* Configurable import rules

---

# Project Structure

```text
Universal-Obsidian-Import-Toolkit/

config/
docs/
samples/
src/
tests/

README.md
ROADMAP.md
CHANGELOG.md
CONTRIBUTING.md
LICENSE
pyproject.toml
requirements.txt
```

---

# Development Principles

* Python 3.12+
* Typed code
* Modular architecture
* Configuration over hardcoded logic
* Test-driven where practical
* Open-source friendly
* Platform independent

---

# Project Status

Current version:

**Pre-Alpha (Sprint 0)**

Current milestone:

Repository foundation and Evernote importer architecture.

---

# License

UNOBIT is released under the MIT License.

---

# Contributing

Contributions are welcome after the initial architecture is completed.

---

# Vision

UNOBIT aims to become a universal migration toolkit for personal knowledge management systems by providing reliable, transparent, and repeatable imports into Obsidian without unnecessary data loss.
