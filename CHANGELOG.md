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