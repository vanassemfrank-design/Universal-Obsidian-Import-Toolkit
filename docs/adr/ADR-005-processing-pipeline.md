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