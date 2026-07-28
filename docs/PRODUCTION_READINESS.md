# Search Production Readiness

Production remains **NO-GO** until every required item has evidence.

## Security and isolation

- Verified JWT issuer, audience and tenant claim.
- Mandatory tenant filter on lexical, vector, autocomplete and aggregation queries.
- Cross-tenant negative tests.
- Restricted-content exclusion tests.
- Managed backend credentials and TLS.
- Query injection and sensitive-log redaction tests.

## Data and indexing

- Versioned index schema and mappings.
- Idempotent ingestion and dead-letter handling.
- Source ID and source classification on every document.
- Deletion/tombstone propagation verified.
- Snapshot restore and alias rollback exercised.
- Index reconciliation report attached.

## Quality and performance

- English, Tamil and mixed-language evaluation completed.
- Recall, precision, MRR and NDCG thresholds approved.
- p95 latency and throughput load-tested.
- Zero-result and timeout rates reviewed.
- Ranking-change regression report attached.

## Operations

- Dashboards and alerts active.
- On-call ownership and escalation defined.
- Capacity limits and scaling triggers documented.
- Incident, rollback and recovery drills completed.
- Deployment commit, workflow and configuration versions recorded.
