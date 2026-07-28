# Search Operations Runbook

## Service checks

Confirm the API health endpoint, backend connectivity, index alias, document count, queue lag, tenant-filter enforcement and query latency before declaring the service healthy.

## Core signals

Monitor request rate, success rate, p50/p95/p99 latency, zero-result rate, timeout rate, rejected-query rate, backend saturation, index freshness lag, ingestion failures, semantic-model failures and cross-tenant denial events.

## Incident response

- **Cross-tenant or restricted-content exposure:** Severity 1. Disable affected routes, preserve evidence, revoke credentials where needed, identify impacted tenants and begin the security incident process.
- **Index corruption or ranking regression:** Freeze writes, switch to the last verified alias or snapshot, compare document counts and run the quality evaluation suite.
- **High latency:** Reduce semantic candidate count, disable non-essential enrichments, inspect backend saturation and apply rate limiting.
- **Ingestion backlog:** Pause non-critical sources, scale consumers and reconcile failed document identifiers.

## Recovery

Use immutable snapshots and alias-based rollback. Restore into an isolated index, validate schema and counts, run tenant-isolation and restricted-content tests, then atomically move the read alias.

## Deployment evidence

Record commit SHA, workflow run, configuration version, index schema version, evaluation report, load-test result, rollback test and approving operator.

## Data deletion

Deletion requests must create a tombstone, remove the document from all lexical and vector indexes, invalidate caches and produce reconciliation evidence.
