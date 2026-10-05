# BPMN DI Rules

BPMN DI is required for visual rendering.

A task/event/gateway generally requires:

```xml
<bpmndi:BPMNShape
    id="BPMNShape_nodeId"
    bpmnElement="nodeId">
  <dc:Bounds x="100" y="100" width="100" height="80"/>
</bpmndi:BPMNShape>
```

A sequence flow requires:

```xml
<bpmndi:BPMNEdge
    id="BPMNEdge_flowId"
    bpmnElement="flowId">
  <di:waypoint x="200" y="140"/>
  <di:waypoint x="300" y="140"/>
</bpmndi:BPMNEdge>
```

Never leave orphaned BPMNShape or BPMNEdge elements.
