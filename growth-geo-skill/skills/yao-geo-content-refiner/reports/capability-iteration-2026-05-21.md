# Capability Iteration 2026-05-21

## Trigger

User asked to address current limitations, especially whether the skill can obtain real data, and to improve report UI according to Kami.

## Capability Upgrade

| Limitation | Upgrade |
|---|---|
| Real data availability was described as a boundary but not operationalized. | Added `真实数据获取与核验计划` and `来源访问记录`. |
| Private/API/internal data could be misunderstood as automatically accessible. | Added data access modes: public web, user-provided files, authorized connectors/API, restricted data. |
| Evidence tables did not show data permission and freshness. | Added fields for permission boundary, freshness, extraction fields, access time, and failure handling. |
| HTML was functional but not editorial enough. | Adapted Kami principles while retaining white background: ink-blue accent, serif headings, warm borders, tighter line-height, no rgba, no hard shadows. |

## New Required Sections

- `data_access_plan`
- `source_access_log`

## Quality Gates Added

- HTML must contain Kami editorial tokens and no `rgba()`.
- Reports must include real-data plan and source access log.
- Unavailable or unauthorized data must remain `待核验`, `需授权`, or `不可访问`.

## Example Update

HubSpot demo now distinguishes:

- publicly verified HubSpot product and IR pages
- research references used for method design
- China pricing/compliance/integration items that require user or official local sources
- internal ROI/conversion data that requires authorized CRM/BI access
