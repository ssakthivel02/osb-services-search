# Search Quality Evaluation

## Evaluation sets

Maintain versioned English, Tamil and mixed-language query sets. Include exact-title, phrase, spelling variation, transliteration, synonym, ambiguous, zero-result and adversarial queries. Each case records tenant, locale, expected source class and relevant document identifiers.

## Metrics

Track Recall@10, Precision@10, MRR, NDCG@10, zero-result rate, restricted-result count, cross-tenant-result count, p95 latency and result stability. Cross-tenant and restricted-result counts must always be zero.

## Release gates

- No security leakage.
- No material regression against the previous approved baseline.
- Tamil and English evaluated separately and together.
- Verified sources must not be systematically displaced by needs-review sources.
- Tie-breaking must be deterministic.
- Every ranking or embedding change requires an evaluation report.

## Bias and safety review

Inspect deity, scripture, temple, Siddhar, child-learning and life-guidance queries for source attribution, language parity and inappropriate confidence. Search results must preserve source classification and must not convert oral or needs-review content into verified claims.
