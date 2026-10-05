# BPMN Rules

The editor must preserve BPMN semantic structure.

Common elements:

- `bpmn:startEvent`
- `bpmn:endEvent`
- `bpmn:userTask`
- `bpmn:serviceTask`
- `bpmn:exclusiveGateway`
- `bpmn:parallelGateway`
- `bpmn:inclusiveGateway`
- `bpmn:subProcess`
- `bpmn:boundaryEvent`
- `bpmn:sequenceFlow`

A sequence flow connects exactly one source to exactly one target.

Do not change unrelated nodes or flows.
