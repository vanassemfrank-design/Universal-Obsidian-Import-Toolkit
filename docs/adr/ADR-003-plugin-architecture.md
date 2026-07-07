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