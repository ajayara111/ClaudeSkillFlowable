# Node Types

## User Task

```xml
<bpmn:userTask id="approveAccount" name="Approve Account"/>
```

Project-specific properties should be copied from existing examples.

## Service Task

```xml
<bpmn:serviceTask id="createAccount" name="Create Account"/>
```

Possible Flowable implementations include delegate expression, Java class, or expression.

## Exclusive Gateway

```xml
<bpmn:exclusiveGateway id="approvalDecision" name="Approved?"/>
```

Conditions belong on outgoing sequence flows where appropriate.

## Parallel Gateway

```xml
<bpmn:parallelGateway id="parallelGateway" name="Parallel Processing"/>
```

Do not apply simple linear-node removal logic to gateways.
