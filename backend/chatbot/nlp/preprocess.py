import re
import string

PUNCT_TABLE = str.maketrans("", "", string.punctuation)

def normalize(text: str) -> str:
text = text.lower().strip()
text = text.translate(PUNCT_TABLE)
text = re.sub(r"\s+", " ", text)
return text