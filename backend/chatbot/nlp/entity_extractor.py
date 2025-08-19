import re

def extract_entities(text: str):
entities = {}
sem = re.findall(r"\bsemester\s*(\d+)\b", text.lower())
if sem:
entities["semester"] = sem
return entities