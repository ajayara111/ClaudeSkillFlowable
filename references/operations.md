# Operation Model

The recommended abstraction is a JSON operation.

## Add

```json
{
  "operation": "ADD_NODE",
  "node": {
    "type": "userTask",
    "id": "approveAccount",
    "name": "Approve Account"
  },
  "position": {
    "after": "validateAccount",
    "before": "createAccount"
  }
}
```

## Remove

```json
{
  "operation": "REMOVE_NODE",
  "nodeId": "approveAccount",
  "reconnect": true
}
```

## Update

```json
{
  "operation": "UPDATE_NODE",
  "nodeId": "approveAccount",
  "properties": {
    "name": "Approve Virtual Account"
  }
}
```
