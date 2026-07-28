#!/usr/bin/env python3
"""Executable negative cases for the OSB search baseline."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / "config/search-policy.json").read_text(encoding="utf-8"))
SOURCES = json.loads((ROOT / "config/source-classifications.json").read_text(encoding="utf-8"))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    security = POLICY["security"]
    query = POLICY["query"]
    ranking = POLICY["ranking"]
    limits = POLICY["rateLimits"]

    require(security["tenantFilterMandatory"], "Cross-tenant search protection is disabled")
    require(not security["requestTenantOverrideAllowed"], "Request tenant override must be rejected")
    require(security["rejectControlCharacters"], "Control-character queries must be rejected")
    require(security["rejectWildcardOnlyQueries"], "Wildcard-only queries must be rejected")
    require(security["escapeBackendQuerySyntax"], "Backend query syntax must be escaped")
    require(not security["logRawQueries"], "Raw queries must not be logged")
    require(query["maximumLength"] <= 256, "Oversized query protection is missing")
    require(query["maximumPageSize"] <= 100, "Unbounded result pages are forbidden")
    require(query["maximumOffset"] <= 10000, "Deep pagination protection is missing")
    require(query["timeoutMilliseconds"] <= 3000, "Query timeout is too high")
    require(ranking["minimumSemanticScore"] >= 0.5, "Semantic relevance floor is too low")
    require(ranking["maximumSemanticCandidates"] <= 200, "Semantic candidate fan-out is too high")
    require(limits["anonymousPerMinute"] == 0, "Anonymous search must remain disabled")
    require(limits["authenticatedPerMinute"] > 0, "Authenticated rate limit is missing")
    require(SOURCES["classifications"]["restricted"]["searchable"] is False, "Restricted content leaked into search")
    require(SOURCES["classifications"]["needs_review"]["rankingWeight"] < SOURCES["classifications"]["verified"]["rankingWeight"], "Unverified content must not outrank verified content")

    print("Negative search security cases passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
