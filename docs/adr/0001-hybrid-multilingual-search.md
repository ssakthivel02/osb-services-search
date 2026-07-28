# ADR 0001: Hybrid Multilingual Search

## Status

Accepted for baseline validation; production implementation remains pending.

## Context

The OSB platform requires English and Tamil discovery across verified, scholarly, traditional, oral and needs-review content while preserving tenant isolation and source provenance.

## Decision

Use hybrid lexical and semantic retrieval behind a versioned API. Normalise text with Unicode NFC, preserve Tamil script, support optional transliteration, apply tenant and restricted-content filters before ranking, and require source metadata on every result. Cap semantic candidates and boosts, penalise needs-review content and use deterministic document-ID tie-breaking.

## Consequences

- Ranking changes require bilingual evaluation evidence.
- Vector and lexical indexes must share document, tenant and source identifiers.
- Semantic-model failure must degrade safely to lexical search.
- Client-supplied tenant overrides are forbidden.
- Restricted content is removed before scoring and highlighting.
- Production needs a selected search backend, embedding model, index schema and capacity plan.
