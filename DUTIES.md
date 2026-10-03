# Duties and Responsibilities for Distributed Tracing Root Cause Agent

## Dual-Control Architecture
Maker:
span-path-decomposer

Checker:
bottleneck-verifier

## Operational Workflow
1. The Maker (span-path-decomposer) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (bottleneck-verifier) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
