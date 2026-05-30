<!--
Copyright © 2026 姚金刚. All rights reserved.
Project: yao-geoflow-cli
Created by: 姚金刚
Date: 2026-05-16
X: https://x.com/yaojingang
-->

# Command Map

## Current Capability Rule

Prefer `bin/geoflow` only when it exists and `--help` confirms the requested action. The current Laravel 2.0.x public repository usually exposes `/api/v1` without a `bin/geoflow` wrapper, so API fallback is expected there.

Do not invent CLI subcommands for actions that only exist in API v1. When the CLI is absent, use `curl` with explicit bearer auth and `X-Idempotency-Key` for writes.

## Preflight

```bash
scripts/geoflow_preflight.sh "<workspace>" [config] [checks]
```

`checks` is optional and comma-separated for API fallback. Examples:

```bash
scripts/geoflow_preflight.sh "/path/to/GEOFlow"
scripts/geoflow_preflight.sh "/path/to/GEOFlow" "" catalog,materials
GEOFLOW_PREFLIGHT_CHECKS=catalog,materials scripts/geoflow_preflight.sh "/path/to/GEOFlow"
```

The preflight supports two modes:

- CLI mode when `<workspace>/bin/geoflow` exists.
- API fallback mode when the CLI is absent and `GEOFLOW_BASE_URL` plus `GEOFLOW_API_TOKEN` are available.

For the Laravel rewrite without a CLI wrapper, `GEOFLOW_BASE_URL` must point to the public web root, for example `http://127.0.0.1:18080`, not `/geo_admin`, not `/api/v1`, and not a proxy error page.

## First Login

Interactive password prompt:

```bash
"/path/to/workspace/bin/geoflow" login --base-url https://your-geoflow-host --username admin
```

Explicit password:

```bash
"/path/to/workspace/bin/geoflow" login --base-url https://your-geoflow-host --username admin --password <PASSWORD>
```

When config exists but the token is invalid or expired, refresh it in place:

```bash
"/path/to/workspace/bin/geoflow" login --base-url https://your-geoflow-host --username admin --force
```

API fallback login:

```bash
curl -sS -X POST \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  --data '{"username":"admin","password":"<password>"}' \
  "$GEOFLOW_BASE_URL/api/v1/auth/login"
```

Do not print the full token in user-facing output.

## Catalog

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config catalog
```

Use this as the authoritative authenticated-read check before mutating commands. Only jump to `login --force` when the failure is clearly `401`, `403`, or token-invalid.

API fallback:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/catalog"
```

Current catalog response includes `models`, `prompts`, `keyword_libraries`, `title_libraries`, `image_libraries`, `knowledge_bases`, `authors`, and `categories`.

If this returns HTML such as `<!doctype html>`, treat it as a base URL/proxy/routing problem, not an AI response-format problem. See [laravel-api-v1-docker.md](laravel-api-v1-docker.md).

## Material Operations

Material API types:

- `categories`
- `authors`
- `keyword-libraries`
- `title-libraries`
- `image-libraries`
- `knowledge-bases`

Aliases accepted by the API include `keywords`, `titles`, `images`, and `knowledge`.

Required scopes:

- read: `materials:read`
- write: `materials:write`

Summary:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/materials"
```

List one material type:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries?search=geo&per_page=20"
```

Create a material library:

```bash
curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: material-keyword-library-001" \
  --data '{"name":"API Keywords","description":"Created from API"}' \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries"
```

Get, update, or delete a material:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries/12"

curl -sS -X PATCH \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: material-keyword-library-update-12" \
  --data '{"description":"Updated from API"}' \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries/12"

curl -sS -X DELETE \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "X-Idempotency-Key: material-keyword-library-delete-12" \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries/12"
```

List material items:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries/12/items?per_page=50"
```

Create material items:

```bash
curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: keyword-item-create-001" \
  --data '{"keyword":"geo automation"}' \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries/12/items"

curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: title-item-create-001" \
  --data '{"title":"GEO automation guide","keyword":"geo automation"}' \
  "$GEOFLOW_BASE_URL/api/v1/materials/title-libraries/34/items"
```

Delete material items:

```bash
curl -sS -X DELETE \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: keyword-items-delete-001" \
  --data '{"ids":[101,102]}' \
  "$GEOFLOW_BASE_URL/api/v1/materials/keyword-libraries/12/items"
```

Knowledge-base items are generated chunks and are read-only through `/items`. To change chunks, update the knowledge-base `content`.

## Task Operations

List tasks:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task list --status active --per-page 20
```

API fallback:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/tasks?status=active&search=geo&per_page=20"
```

Create task:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task create --json ./task.json --idempotency-key task-create-001
```

Useful task JSON fields:

```json
{
  "name": "API task",
  "title_library_id": 1,
  "prompt_id": 2,
  "ai_model_id": 3,
  "status": "paused",
  "category_mode": "smart",
  "publish_scope": "local_and_distribution",
  "draft_limit": 5,
  "article_limit": 10
}
```

`author_id`, `image_library_id`, `knowledge_base_id`, and `fixed_category_id` are optional. `publish_scope` is one of `local_and_distribution`, `distribution_only`, or `local_only`.

API fallback:

```bash
curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: task-create-001" \
  --data @./task.json \
  "$GEOFLOW_BASE_URL/api/v1/tasks"
```

Get task:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task get 12
```

Update task:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task update 12 --json ./task-patch.json --idempotency-key task-update-12
```

Delete task:

```bash
curl -sS -X DELETE \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "X-Idempotency-Key: task-delete-12" \
  "$GEOFLOW_BASE_URL/api/v1/tasks/12"
```

Task deletion moves visible task articles to trash, unlinks trashed task articles, and deletes schedule/material queue records when those tables exist.

Start task:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task start 12 --idempotency-key task-start-12
```

API fallback:

```bash
curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: task-start-12" \
  --data '{"enqueue_now":true}' \
  "$GEOFLOW_BASE_URL/api/v1/tasks/12/start"
```

Start and enqueue immediately:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task start 12 --enqueue-now --idempotency-key task-start-12
```

Stop task:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task stop 12 --idempotency-key task-stop-12
```

Manual enqueue:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task enqueue 12 --idempotency-key task-enqueue-12
```

List task jobs:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config task jobs 12 --limit 20
```

Get job:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config job get 88
```

## Article Operations

List articles:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article list --task-id 12 --per-page 20
```

API fallback:

```bash
curl -sS \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  "$GEOFLOW_BASE_URL/api/v1/articles?task_id=12&status=draft&review_status=pending&per_page=20"
```

Create article from markdown:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article create \
  --title "标题" \
  --content-file ./article.md \
  --task-id 12 \
  --author-id 5 \
  --category-id 2 \
  --idempotency-key article-create-001
```

Create article from JSON:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article create --json ./article.json --idempotency-key article-create-001
```

API fallback create:

```bash
curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: article-create-001" \
  --data @./article.json \
  "$GEOFLOW_BASE_URL/api/v1/articles"
```

Update article:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article update 101 --json ./article-patch.json --idempotency-key article-update-101
```

Review article:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article review 101 --status approved --note "pass" --idempotency-key article-review-101
```

API fallback review body uses `review_status` and `review_note`:

```bash
curl -sS -X POST \
  -H "Authorization: Bearer $GEOFLOW_API_TOKEN" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "X-Idempotency-Key: article-review-101" \
  --data '{"review_status":"approved","review_note":"API review pass"}' \
  "$GEOFLOW_BASE_URL/api/v1/articles/101/review"
```

Publish article:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article publish 101 --idempotency-key article-publish-101
```

Then verify persisted state:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article get 101
```

Then verify the final local frontend URL using `/article/{slug}` from the persisted article slug or the page's canonical URL when `status=published`. Generated article slugs should be 8-character short ASCII tokens, but user-supplied slugs may differ. Do not return `article.php?id=...` as the published URL.

Trash article:

```bash
"/path/to/workspace/bin/geoflow" --config /path/to/config article trash 101 --idempotency-key article-trash-101
```

## Distribution Boundary

GEOFlow 2.0.1 includes Distribution Management, target-site packages, static target sites, and distribution queues, but those admin operations are not exposed through the current `/api/v1` surface.

API task fields can set `publish_scope`, which affects worker-driven task publishing:

- `local_and_distribution`: publish locally and enqueue distribution when task channels exist.
- `distribution_only`: worker publishing may mark local articles `private` while still eligible for distribution.
- `local_only`: skip distribution.

Do not claim the API can create distribution channels, rotate secrets, download target-site packages, or inspect Analytics unless the target workspace exposes separate routes for those actions.
