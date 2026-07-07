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