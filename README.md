# Flowable BPMN Editor Claude Skill

A Claude Code skill for safely adding, removing, reconnecting, and validating Flowable BPMN nodes.

## Purpose

This skill is designed for repositories containing Flowable `.bpmn20.xml` workflow definitions. It teaches Claude to:

- Inspect an existing BPMN process before changing it.
- Add and remove BPMN nodes.
- Reconnect sequence flows safely.
- Preserve Flowable-specific extension properties.
- Preserve BPMN DI (`BPMNShape`, `BPMNEdge`, waypoints) so the process remains visually renderable.
- Validate XML structure, IDs, sequence flows, and DI consistency.
- Produce a clear change summary.

## Installation

Copy this directory into your repository:

```text
.claude/skills/flowable-bpmn-editor/
```

Expected location:

```text
your-project/
├── .claude/
│   └── skills/
│       └── flowable-bpmn-editor/
│           ├── SKILL.md
│           ├── references/
│           ├── scripts/
│           ├── templates/
│           └── tests/
├── src/
└── ...
```

## Example requests

```text
Add a User Task named "Approve Account" between validateAccount and createAccount.
```

```text
Remove sendApprovalEmail and reconnect its predecessor directly to endEvent.
```

```text
Add a 1-hour timer boundary event to submitRequest.
```

```text
Show me all nodes and sequence flows in this BPMN file.
```

## Safety principles

1. Never rewrite unrelated BPMN elements.
2. Preserve existing IDs unless an explicit change requires them.
3. Generate unique IDs for new elements.
4. Never add a BPMN node without its BPMN DI shape.
5. Never add a sequence flow without its BPMN DI edge.
6. Never remove a node while leaving orphaned DI elements.
7. Do not automatically reconnect complex gateway/subprocess structures without checking semantics.
8. Validate the result before reporting success.

## Initial implementation

The included Python scripts are intentionally conservative starter tools. They use standard XML processing and are designed to be extended with project-specific Flowable conventions.

For production use, add your repository's actual BPMN examples and Flowable extension conventions under `references/` and `tests/`.

## Recommended future enhancements

- Use Flowable Java model APIs for advanced editing.
- Add schema/BPMN validation.
- Add automated XML formatting.
- Add layout/coordinate calculation.
- Add gateway-aware reconnection.
- Add subprocess and boundary-event support.
- Add unit tests for every supported operation.
