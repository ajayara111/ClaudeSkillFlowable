# Test Cases

## 1. Inspect

Input:

`tests/simple-process.bpmn20.xml`

Expected:

- `startEvent`
- `taskA`
- `taskB`
- `endEvent`
- three sequence flows

## 2. Add a node

Request:

Add `approveAccount` between `taskA` and `taskB`.

Expected:

```text
taskA -> approveAccount -> taskB
```

Expected DI:

- shape for `approveAccount`
- edge for taskA -> approveAccount
- edge for approveAccount -> taskB

## 3. Remove a node

Request:

Remove `taskB` and reconnect to `endEvent`.

Expected:

```text
taskA -> endEvent
```

## 4. Safety

A gateway, subprocess, boundary event, or multi-instance node must not be removed using simple linear reconnection logic without semantic inspection.
