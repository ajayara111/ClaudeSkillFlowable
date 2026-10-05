#!/usr/bin/env python3
"""Starter script.

This intentionally does not perform arbitrary BPMN rewriting yet.
Use it as the entry point for a project-specific implementation.

Recommended production implementation:
- parse namespaces
- inspect source/target flows
- insert the new BPMN element
- split the original sequence flow
- create BPMNShape
- create BPMNEdges
- preserve Flowable extension elements
- validate
"""

import sys

if len(sys.argv) < 2:
    print("Usage: add_node.py <file.bpmn20.xml> [arguments]")
    sys.exit(2)

print("Starter add_node.py: implement repository-specific BPMN insertion rules.")
