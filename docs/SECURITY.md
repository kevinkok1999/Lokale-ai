# Security model

Deny by default; least privilege; authenticated gateways; secrets outside Git; sandboxed tool execution; audit every code-changing, pairing, deployment and policy action. External documents, websites, repositories, tool output and model output are untrusted data and cannot override repository policy. Approval is required for production/public exposure, credentials, payments, deletion, destructive migrations and major network changes.
