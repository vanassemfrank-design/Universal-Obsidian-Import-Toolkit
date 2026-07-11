# UNOBIT Sprint 4 Context Bundle

Generated: 2026-07-11T09:02:17

## Sprint 4 Focus

- CLI uitbreiden
- `unobit.yaml` configuratiebestand
- HTML/JavaScript GUI
- user-guide.md
- developer-guide.md
- public beta voorbereiding

---

# File: `README.md`

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

---

# File: `CHANGELOG.md`

# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on Keep a Changelog.

---

## 0.1.0 - Unreleased

### Added
- Initial repository structure.
- Basic project documentation.
- Roadmap.
- Configuration example.
- Python package name: `unobit`.

### Planned
- CLI skeleton.
- Universal Note model.
- Evernote ENEX parser.

---

## [0.2.0-dev] - Sprint 2

### Added

#### Core
- ImportReport model
- PipelineContext
- ProcessingPipeline
- PipelineFactory
- Timing support for pipeline steps

#### Validation
- Base Validator framework
- ValidationResult
- ValidationMessage
- ValidationStep
- NoteValidator
- AttachmentValidator
- MetadataValidator

#### Processing
- Base Processor framework
- ProcessingStep
- TitleCleanupProcessor
- ContentCleanupProcessor

#### Testing
- Pytest test framework
- Unit tests for all core pipeline components
- Integration test for default processing pipeline

#### Documentation
- Architecture Decision Records (ADR)
- Initial architecture documentation
- Sprint documentation updates

### Changed

- Refactored project architecture towards a modular processing pipeline.
- Processing is now separated into Validators, Processors and Exporters.
- Import reporting is centralized through ImportReport.

### Fixed

- Improved testability of the processing engine.
- Improved separation of responsibilities between pipeline components.

## [0.3.0-dev] - Sprint 3

### Added
- Evernote import integrated with ProcessingPipeline.
- ImportReport summary output.
- Timing and performance metrics.
- JSON import report.
- Reference Resolution framework.
- Evernote internal link resolver.
- ENML conversion framework.
- ENML todo conversion.
- ENML cleanup and postprocessing.
- ENML media placeholders.
- Media resolver for attachment links.
- ENEX test data generator.
- Regression fixtures for internal links, media, formatting and large titles.

### Fixed
- `body`/`content` mismatch in validators and processors.
- Invalid Windows attachment filenames.
- Excessively long Markdown filenames.
- BeautifulSoup XML parser warning.
- Unicode console output issue on Windows.

## [0.4.0-dev] - Sprint 4

### Added

- Nested CLI command structure.
- ImportService abstraction.
- unobit.yaml configuration.
- Configuration validation.
- HTML report writer.
- HTML/JavaScript GUI prototype.
- Report viewer command.
- CLI integration tests.
- ImportService tests.

### Changed

- CLI redesigned into logical command groups.
- Import logic separated from CLI.
- Configuration driven report generation.

### Fixed

- Configuration error handling.
- CLI usability.

---

# File: `ROADMAP.md`

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

---

# File: `Project-state.md`

_File not found yet._

---

# File: `session-handover.md`

_File not found yet._

---

# File: `docs/architecture.md`

_File not found yet._

---

# File: `docs/architecture-overview.md`

CLI
 │
 ▼
Importer
 │
 ▼
Pipeline
 ├── Validation
 ├── Processing
 ├── Resolution
 ▼
Exporter
 │
 ▼
Reports

---

# File: `docs/user-guide.md`

_File not found yet._

---

# File: `docs/developer-guide.md`

_File not found yet._

---

# File: `docs/public-beta-checklist.md`

# Public Beta Checklist

## Functionaliteit
- [ ] CLI getest
- [ ] Configuratiebestand werkt
- [ ] GUI start
- [ ] JSON report werkt
- [ ] HTML report werkt

## Testen
- [ ] Alle pytest-tests groen
- [ ] Grote ENEX (>1 GB) getest
- [ ] Windows 10
- [ ] Windows 11
- [ ] Linux (optioneel)

## Documentatie
- [ ] README
- [ ] Installatiehandleiding
- [ ] FAQ
- [ ] Changelog
- [ ] Roadmap

## Release
- [ ] Git tag
- [ ] GitHub Release
- [ ] Release Notes

---

# ADR Files

---

# File: `docs\adr\ADR-001-project-principles.md`

# ADR-001: Projectprincipes

## Status

Accepted

## Context

UNOBIT is bedoeld als duurzame importtoolkit voor persoonlijke kennisarchieven. Het project moet niet alleen Evernote naar Obsidian kunnen importeren, maar later ook andere bronnen ondersteunen zoals OneNote, Notion, HTML, ChatGPT exports en generieke Markdown-archieven.

De eerste werkende Evernote-importer is gerealiseerd in Sprint 1. Vanaf Sprint 2 verschuift de focus naar onderhoudbaarheid, testbaarheid en uitbreidbaarheid.

## Besluit

UNOBIT volgt de volgende projectprincipes:

1. Obsidian-first output.
2. Import once, preserve forever.
3. Modulair ontwerp.
4. Universeel intern notitiemodel.
5. Importers, processors, validators en exporters zijn los gekoppeld.
6. Metadata en attachments worden zo veel mogelijk behouden.
7. Validatie en rapportage zijn standaard onderdeel van elke import.
8. Code moet testbaar zijn met pytest.
9. Architectuurbesluiten worden vastgelegd in ADR’s.
10. Documentatie groeit mee met de code.

## Gevolgen

Deze principes betekenen dat snelle scripts worden vermeden wanneer ze later technische schuld veroorzaken. Nieuwe functionaliteit moet passen binnen het universele model, de pipeline en de validatorstructuur.

Dit maakt ontwikkeling in het begin iets langzamer, maar voorkomt dat elke importer een losstaand conversiescript wordt.

---

# File: `docs\adr\ADR-002-universal-note-model.md`

# ADR-002: Universal Note Model

## Status

Accepted

## Context

UNOBIT ondersteunt meerdere importformaten. Iedere bron heeft een eigen datastructuur en metadata. Wanneer iedere exporter rechtstreeks afhankelijk zou zijn van een specifieke importer ontstaat een complexe en moeilijk onderhoudbare codebasis.

## Besluit

Alle importers converteren hun brongegevens naar één universeel intern Note-model.

Exporters, validators en processors werken uitsluitend met dit model en zijn volledig onafhankelijk van de oorspronkelijke bron.

Bronspecifieke informatie wordt opgeslagen als metadata.

## Alternatieven

- Voor iedere importer een eigen exporter ontwikkelen.
- Bronafhankelijke processors.

Beide alternatieven leiden tot veel dubbele code en een sterke onderlinge afhankelijkheid.

## Gevolgen

Voordelen:

- Eén centrale datastructuur.
- Hergebruik van exporters.
- Hergebruik van validators.
- Nieuwe importers zijn eenvoudiger toe te voegen.
- Minder technische schuld.

Nadelen:

- Importers moeten een extra conversiestap uitvoeren.
- Het universele model moet zorgvuldig worden beheerd.

---

# File: `docs\adr\ADR-003-plugin-architecture.md`

# ADR-003: Plugin Architecture

## Status

Accepted

## Context

UNOBIT zal in de toekomst meerdere importers, exporters, validators en processors bevatten.

Het project moet uitbreidbaar blijven zonder bestaande code aan te passen.

## Besluit

UNOBIT gebruikt een plugin-architectuur.

De volgende componenten worden als plugins beschouwd:

- Importers
- Exporters
- Validators
- Processors

Iedere plugin heeft een duidelijke verantwoordelijkheid en communiceert uitsluitend via de publieke interfaces van de pipeline.

## Alternatieven

- Grote centrale importfunctie.
- Hardcoded verwerking per bestandstype.

Deze alternatieven beperken uitbreidbaarheid en verhogen de onderhoudslast.

## Gevolgen

Voordelen:

- Losse componenten.
- Hoge testbaarheid.
- Eenvoudig uitbreidbaar.
- Geschikt voor community-bijdragen.

Nadelen:

- Iets complexere architectuur.
- Meer interfaces.

---

# File: `docs\adr\ADR-004-obsidian-first.md`

# ADR-004: Obsidian First

## Status

Accepted

## Context

UNOBIT is ontworpen als migratietool voor gebruikers die hun kennis duurzaam willen bewaren.

Hoewel de interne architectuur generiek is, heeft het project één primair doel.

## Besluit

UNOBIT richt zich primair op het produceren van een hoogwaardige Obsidian Vault.

Dit betekent onder andere:

- Markdown als standaardformaat.
- YAML Frontmatter.
- Correcte Wikilinks.
- Correcte attachment-structuur.
- Compatibiliteit met Obsidian-conventies.

Andere exportformaten blijven mogelijk, maar mogen de kwaliteit van de Obsidian-export niet negatief beïnvloeden.

## Alternatieven

- Volledig generieke export zonder voorkeursplatform.
- Gelijke ondersteuning voor alle kennisplatformen.

Deze alternatieven maken het project omvangrijker zonder direct voordeel voor de primaire doelgroep.

## Gevolgen

Voordelen:

- Heldere projectfocus.
- Consistente output.
- Minder ontwerpkeuzes.
- Betere gebruikerservaring.

Nadelen:

- Sommige platformspecifieke optimalisaties worden pas later ontwikkeld.

---

# File: `docs\adr\ADR-005-processing-pipeline.md`

# ADR-005: Processing Pipeline

## Status

Accepted

## Context

UNOBIT importeert kennis uit meerdere bronnen naar Obsidian. In Sprint 1 werkte de Evernote-importer als directe conversiestroom van ENEX naar Markdown en attachments.

Vanaf Sprint 2 is gekozen voor een modulaire architectuur waarin importers, validators, processors en exporters losgekoppeld zijn. Hierdoor kunnen toekomstige importers zoals OneNote, Notion en ChatGPT dezelfde verwerking gebruiken.

## Besluit

Alle geïmporteerde notities worden verwerkt via een centrale Processing Pipeline.

De standaard gegevensstroom is:

```text
Importer
↓
Universal Note Model
↓
ProcessingPipeline
↓
ValidationStep
↓
ProcessingStep
↓
Exporter
↓
ImportReport

---
