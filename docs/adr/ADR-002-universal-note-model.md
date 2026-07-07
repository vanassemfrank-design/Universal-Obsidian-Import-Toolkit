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