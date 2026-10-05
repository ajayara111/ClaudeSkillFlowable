#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET
from collections import Counter

BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"
DI = "http://www.omg.org/spec/DD/20100524/DI"

def local(tag):
    return tag.split("}", 1)[-1]

if len(sys.argv) != 2:
    print("Usage: validate_bpmn.py <file.bpmn20.xml>")
    sys.exit(2)

path = sys.argv[1]

try:
    root = ET.parse(path).getroot()
except ET.ParseError as e:
    print(f"XML: FAIL - {e}")
    sys.exit(1)

ids = []
elements = {}
for e in root.iter():
    if "id" in e.attrib:
        ids.append(e.attrib["id"])
        elements[e.attrib["id"]] = e

duplicates = [x for x, n in Counter(ids).items() if n > 1]
if duplicates:
    print("IDs: FAIL - duplicate IDs:", ", ".join(duplicates))
    sys.exit(1)

errors = []

for flow in root.iter("{%s}sequenceFlow" % BPMN):
    source = flow.attrib.get("sourceRef")
    target = flow.attrib.get("targetRef")
    if source not in elements:
        errors.append(f"{flow.attrib.get('id')}: missing source {source}")
    if target not in elements:
        errors.append(f"{flow.attrib.get('id')}: missing target {target}")

# Basic DI reference check
for e in root.iter():
    if local(e.tag) in ("BPMNShape", "BPMNEdge"):
        ref = e.attrib.get("bpmnElement")
        if ref and ref not in elements:
            errors.append(f"DI {e.attrib.get('id')}: missing bpmnElement {ref}")

if errors:
    print("Validation: FAIL")
    for error in errors:
        print("-", error)
    sys.exit(1)

print("XML: PASS")
print("IDs: PASS")
print("Sequence flows: PASS")
print("BPMN DI references: PASS")
print("Validation: PASS")
