# Example VAM Workflow

A representative VAM approval process:

```text
Start
  |
Submit Request
  |
Get Approvers
  |
Approval
  |
Approved?
 /       \
No       Yes
 |         |
Reject    Create Account
Email       |
 |        Finacle Create
End         |
          Approval Email
             |
            End
```

Use actual repository BPMN files as the authoritative source for namespaces,
Flowable extensions, IDs, and project-specific conventions.
