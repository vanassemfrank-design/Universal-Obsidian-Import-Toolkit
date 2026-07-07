# UNOBIT Project State

> Laatst bijgewerkt: 2026-07-07
> Sprint: 2
> Versie: 0.2.0-dev

---

# Current Status

Sprint 0
- [x] Repository
- [x] CLI
- [x] Packaging
- [x] Documentation

Sprint 1
- [x] Universal Note Model
- [x] Evernote ENEX streaming parser
- [x] Markdown Exporter
- [x] Attachment export
- [x] Localization foundation

Sprint 2
- [x] ImportReport
- [x] PipelineContext
- [x] ProcessingPipeline
- [x] Validator base
- [ ] ValidatorStep
- [ ] Performance profiler
- [ ] Pipeline refactor

---

# Current Architecture

Importer
→ Pipeline
→ Validators
→ Processors
→ Exporter
→ ImportReport

---

# Important Decisions

- Universal Note Model is the canonical data model.
- Obsidian is the primary export target.
- Streaming parsing is preferred over full-memory parsing.
- Architecture decisions are documented as ADRs.

---

# Current Folder Structure

src/
docs/
tests/
samples/

---

# Active TODO

1. ValidatorStep
2. Pipeline integration
3. Performance profiler
4. Refactor Evernote importer
5. Sprint 3 planning

---

# Known Technical Debt

- Evernote importer still bypasses parts of the new pipeline.
- ImportReport not yet integrated everywhere.
- Validators are not yet executed by the pipeline.

---

# Next Session Start

Continue with:
Sprint 2.5 - ValidatorStep

Do NOT redesign:
- Universal Note Model
- Plugin Architecture
- ADR structure

Assume these are accepted.

---

# Future Roadmap

Sprint 3
- Evernote archive-quality import
- Internal note links
- Notebook/Stack support
- Tag refinement
- Validation report
- Archive verification

Sprint 4
- OneNote Importer

Sprint 5
- ChatGPT Importer

Sprint 6
- Plugin SDK