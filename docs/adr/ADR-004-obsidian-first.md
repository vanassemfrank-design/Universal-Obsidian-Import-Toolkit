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