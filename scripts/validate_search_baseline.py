#!/usr/bin/env python3
"""Validate the OSB search policy and source classification registry."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    policy = json.loads((ROOT / "config/search-policy.json").read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "config/source-classifications.json").read_text(encoding="utf-8"))

    require(policy["apiPrefix"].startswith("/api/v1/"), "Search API must be versioned")
    require({"en-GB", "ta-IN"}.issubset(policy["supportedLocales"]), "English and Tamil locales are required")
    require(policy["normalisation"]["unicodeForm"] == "NFC", "Unicode NFC normalisation is required")
    require(policy["normalisation"]["preserveTamilScript"] is True, "Tamil script must be preserved")

    query = policy["query"]
    require(1 <= query["minimumLength"] <= query["maximumLength"] <= 512, "Unsafe query length limits")
    require(query["maximumTerms"] <= 64, "Query term limit is too high")
    require(query["maximumFilters"] <= 20, "Filter limit is too high")
    require(query["defaultPageSize"] <= query["maximumPageSize"] <= 100, "Unsafe page-size limits")
    require(query["timeoutMilliseconds"] <= 5000, "Search timeout must not exceed five seconds")

    security = policy["security"]
    for key in (
        "authenticationRequiredByDefault",
        "tenantFilterMandatory",
        "defaultDenyUnknownFilters",
        "rejectControlCharacters",
        "rejectWildcardOnlyQueries",
        "escapeBackendQuerySyntax",
        "redactSensitiveTerms",
    ):
        require(security[key] is True, f"Security control must be enabled: {key}")
    require(security["requestTenantOverrideAllowed"] is False, "Request tenant override must be forbidden")
    require(security["logRawQueries"] is False, "Raw search queries must not be logged")

    ranking = policy["ranking"]
    require(ranking["hybridEnabled"] is True, "Hybrid search must be enabled")
    require(0.0 <= ranking["minimumSemanticScore"] <= 1.0, "Invalid semantic threshold")
    require(ranking["maximumSemanticCandidates"] <= 500, "Semantic candidate limit is too high")
    require(ranking["needsReviewPenalty"] > 0, "Needs-review content must be penalised")
    require(ranking["deterministicTieBreak"] == "document_id", "Tie-breaking must be deterministic")

    results = policy["results"]
    for key in ("requireSourceId", "requireSourceClassification", "requireLocale", "requireTenantId"):
        require(results[key] is True, f"Required result metadata missing: {key}")
    require(results["maximumSnippetCharacters"] <= 500, "Snippet limit is too high")

    classes = sources["classifications"]
    require({"verified", "needs_review", "restricted"}.issubset(classes), "Required source classes missing")
    require(classes["verified"]["rankingWeight"] > classes["needs_review"]["rankingWeight"], "Verified sources must outrank needs-review sources")
    require(classes["restricted"]["searchable"] is False, "Restricted content must not be searchable")
    require("tenant_id" in sources["requiredDocumentFields"], "Documents must carry tenant_id")
    require("source_id" in sources["requiredDocumentFields"], "Documents must carry source_id")

    print("Search baseline validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
