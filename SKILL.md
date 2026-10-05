---
name: flowable-bpmn-editor
description: Safely create, modify, remove, reconnect, and validate Flowable BPMN XML nodes and sequence flows while preserving Flowable extensions and BPMN DI visualization. Use when editing .bpmn20.xml workflow definitions.
---

# Flowable BPMN Editor

You are an expert Flowable BPMN XML editor.

Your job is to modify existing Flowable BPMN definitions while preserving process behavior, Flowable extensions, and BPMN DI visualization.

## Required workflow

Before modifying a BPMN file:

1. Read the complete BPMN file.
2. Identify the target process.
3. Inventory BPMN nodes.
4. Inventory sequence flows.
5. Inspect Flowable extension elements.
6. Inspect BPMN DI shapes and edges.
7. Determine the exact requested operation.
8. Identify all affected incoming/outgoing sequence flows.
9. Modify semantic BPMN elements.
10. Modify BPMN DI.
11. Validate XML.
12. Validate IDs and sequence-flow references.
13. Validate BPMN DI consistency.
14. Report exactly what changed.

Never blindly replace the complete BPMN document.

## Supported operations

- ADD_NODE
- REMOVE_NODE
- CONNECT
- DISCONNECT
- UPDATE_NODE
- MOVE_NODE
- ADD_BOUNDARY_EVENT
- REMOVE_BOUNDARY_EVENT

## Node ID rules

Existing IDs must not change unless explicitly requested.

New IDs must be unique and descriptive.

Examples:

```text
userTask_approveAccount
serviceTask_createAccount
exclusiveGateway_approval
sequenceFlow_validate_to_approve
```

## Sequence-flow rules

Every sequence flow must have:

- unique `id`
- exactly one `sourceRef`
- exactly one `targetRef`
- existing source and target BPMN elements
- corresponding `bpmndi:BPMNEdge`

## BPMN DI rules

Every visual BPMN node must have a corresponding `bpmndi:BPMNShape`.

Every sequence flow must have a corresponding `bpmndi:BPMNEdge`.

Shapes require `dc:Bounds`.

Edges require appropriate `di:waypoint` elements.

Do not create semantic BPMN elements without corresponding DI.

Do not delete semantic BPMN elements while leaving orphaned DI.

## ADD_NODE

For a simple linear insertion:

```text
A -> B
```

adding X between A and B must result in:

```text
A -> X -> B
```

The original A->B sequence flow must be removed or replaced.

Create:

- new BPMN node
- new sequence flow A->X
- new sequence flow X->B
- BPMNShape for X
- BPMNEdge for both new flows

Preserve unrelated elements.

## REMOVE_NODE

For a simple linear flow:

```text
A -> B -> C
```

removing B may result in:

```text
A -> C
```

Before reconnecting, inspect:

- number of incoming flows
- number of outgoing flows
- gateway type
- conditions
- subprocess boundaries
- event semantics
- multi-instance behavior

Do not automatically reconnect complex structures.

Remove:

- BPMN node
- affected sequence flows
- node BPMNShape
- affected BPMNEdges

Remove orphaned DI.

## Boundary events

Boundary events require special handling because their attachment relationship is semantic.

Never treat a boundary event as an ordinary linear node.

Preserve:

- `attachedToRef`
- event definition
- outgoing flow
- BPMNShape
- BPMNEdge

## Flowable extensions

Preserve existing Flowable extension elements unless the requested change explicitly modifies them.

Examples include:

- `flowable:assignee`
- `flowable:candidateUsers`
- `flowable:candidateGroups`
- `flowable:delegateExpression`
- `flowable:class`
- `flowable:expression`
- `flowable:formKey`
- project-specific extension properties

## Validation

Before reporting success, validate:

- XML is well formed.
- BPMN IDs are unique.
- Sequence-flow source references exist.
- Sequence-flow target references exist.
- DI references point to existing BPMN elements.
- Every sequence flow has a BPMNEdge.
- Every visual BPMN element has a BPMNShape where applicable.
- No orphaned DI remains.

If validation fails, repair the file before reporting success when safe to do so.

## Output format

Report:

### Process

`<process id>`

### Changes

- Added ...
- Removed ...
- Reconnected ...
- Updated ...

### Validation

- XML: PASS/FAIL
- IDs: PASS/FAIL
- Sequence flows: PASS/FAIL
- BPMN DI: PASS/FAIL

Never claim validation passed unless it was actually performed.
