# Sequence Flow Rules

For every sequence flow:

```xml
<bpmn:sequenceFlow
    id="flow_1"
    sourceRef="taskA"
    targetRef="taskB"/>
```

The source and target IDs must exist.

The flow must have a corresponding BPMN DI edge:

```xml
<bpmndi:BPMNEdge
    id="BPMNEdge_flow_1"
    bpmnElement="flow_1">
  <di:waypoint x="100" y="100"/>
  <di:waypoint x="250" y="100"/>
</bpmndi:BPMNEdge>
```
