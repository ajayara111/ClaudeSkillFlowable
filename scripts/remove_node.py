#!/usr/bin/env python3
"""Starter script.

Production implementation should:
- locate the node
- inspect incoming/outgoing flows
- reject unsafe gateway/subprocess cases
- remove semantic node
- remove affected sequence flows
- optionally reconnect simple linear A -> B -> C as A -> C
- remove BPMNShape/BPMNEdge
- validate
"""

import sys

if len(sys.argv) < 2:
    print("Usage: remove_node.py <file.bpmn20.xml> [arguments]")
    sys.exit(2)

print("Starter remove_node.py: implement repository-specific removal rules.")
