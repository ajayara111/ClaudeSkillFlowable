#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET

BPMN = "http://www.omg.org/spec/BPMN/20100524/MODEL"

def local(tag):
    return tag.split("}", 1)[-1]

if len(sys.argv) != 2:
    print("Usage: inspect_bpmn.py <file.bpmn20.xml>")
    sys.exit(2)

root = ET.parse(sys.argv[1]).getroot()

print("NODES")
for e in root.iter():
    if e.tag.startswith("{" + BPMN + "}") and local(e.tag) != "sequenceFlow":
        if "id" in e.attrib:
            print(f"- {e.attrib['id']} [{local(e.tag)}] name={e.attrib.get('name','')}")

print("\nSEQUENCE FLOWS")
for e in root.iter("{%s}sequenceFlow" % BPMN):
    print(f"- {e.attrib.get('id')}: {e.attrib.get('sourceRef')} -> {e.attrib.get('targetRef')}")
