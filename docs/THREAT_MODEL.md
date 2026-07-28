# Search Threat Model

## Security boundary

The search service accepts authenticated, tenant-scoped queries and returns only documents authorised for the caller's tenant and permissions. It does not trust client-supplied tenant identifiers, backend query syntax, index metadata or semantic-model output.

## Principal threats and controls

1. **Cross-tenant disclosure** — derive tenant context from the verified token; apply a mandatory tenant filter to lexical, semantic, autocomplete and aggregation paths; reject request overrides.
2. **Query injection** — parse allow-listed filters, escape backend syntax, reject control characters and default-deny unknown operators.
3. **Resource exhaustion** — enforce query length, term, filter, page-size, offset, candidate, timeout and rate limits.
4. **Sensitive-query leakage** — do not log raw queries; redact credentials, tokens, personal data and recovery codes from telemetry.
5. **Semantic poisoning** — index only documents with required provenance metadata; preserve source classification; penalise needs-review content.
6. **Restricted-content exposure** — exclude restricted documents before ranking and highlighting, not after result generation.
7. **Ranking manipulation** — cap freshness and semantic boosts; use deterministic tie-breaking; monitor score-distribution drift.
8. **Prompt or content injection** — treat indexed content as untrusted data; do not execute instructions embedded in documents.
9. **Enumeration** — apply authentication, rate limiting, minimum query length and stable error responses.
10. **Stale or deleted data** — use idempotent indexing, tombstones and reconciliation jobs; verify deletion propagation.

## Trust assumptions

- JWT validation and tenant claims are supplied by the authentication and gateway services.
- Index credentials are stored in a managed secret store.
- Transport encryption is mandatory between clients, gateway, search service and backend.
- Source classification is produced by an authorised content-governance workflow.

## Required negative evidence

Production approval requires tests proving cross-tenant denial, restricted-content exclusion, unknown-filter rejection, wildcard-only rejection, oversized-query rejection, timeout enforcement, deletion propagation and log redaction.
