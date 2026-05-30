<!--
Copyright © 2026 姚金刚. All rights reserved.
Project: yao-geoflow-cli
Created by: 姚金刚
Date: 2026-05-16
X: https://x.com/yaojingang
-->

# Operation Boundary

This skill is for operating a running GEOFlow system, not for developing the system itself.

## Allowed Actions

- Run `bin/geoflow` commands when the CLI exists
- Use Laravel `/api/v1` fallback when the current GEOFlow rewrite has no CLI wrapper
- Read command output
- Build JSON payload files when needed for task, material, or article operations
- Inspect resulting material, task, job, and article state through the CLI or API v1

## Disallowed Actions

- Direct SQL against the project database
- Editing backend PHP just to complete an operations request
- Replacing the CLI with raw `curl` when the CLI exists and already supports the action
- Exposing a full bearer token in user-facing summaries
- Claiming admin-only Distribution Management, target-site package, Analytics, URL import, or async title generation flows are available through API v1 unless the target workspace exposes matching routes

## Required Checks

Before the first mutating command in a workspace:

1. Verify whether `bin/geoflow` exists. If it does not, verify the workspace is a Laravel GEOFlow app with `artisan` and `routes/api.php`.
2. If CLI configuration is missing, run `geoflow login` first. If using API fallback, obtain a bearer token through `/api/v1/auth/login` or the provided token source.
3. If configuration exists but authenticated reads return `401`, `403`, or token-invalid output, refresh login/token.
4. If authenticated reads fail for another reason, report that failure instead of assuming login is the fix.
5. Verify the CLI resolves configuration, or verify the API base URL responds.
6. Verify an authenticated read such as `catalog` succeeds. `config show` or a public homepage check by itself is not sufficient.
7. For material operations, verify `materials:read` and `materials:write` through `GET /api/v1/materials` before writing.

After any mutating command:

1. Re-read the target resource.
2. Report the final persisted state.
3. If the action triggered a background job, inspect the job separately.
4. If the action published an article locally, verify the final frontend URL and report the `/article/{slug}` route rather than an `article.php?id=...` compatibility link.
5. For generated articles, the final article slug should be an 8-character short ASCII token such as `bc7af3fb`. User-supplied slugs may differ; report the persisted value.

## Error Interpretation

Keep these failure classes separate:

- CLI/runtime failure: command missing, config missing, permission problem, malformed args
- API fallback setup failure: missing `GEOFLOW_BASE_URL`, missing bearer token, wrong `/api/v1` base path
- API fallback routing failure: `/api/v1/catalog` returns HTML, proxy errors, login pages, or Laravel web pages instead of JSON
- API failure: 401, 403, 404, 409, 422, 500
- Business-data failure: task inactive, missing titles, invalid category, review state conflict
- Admin-only operation: distribution channel setup, target-site packages, Analytics, URL import, or async title generation not exposed by `/api/v1`

Do not conflate a downstream job-data failure with a CLI failure.
If a task is blocked by business data and the user only needs a publish smoke test, stop the task before switching to a direct article-create fallback.
