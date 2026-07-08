import json
import re


def extract_json(text: str) -> dict:
    try:
        json_match = re.search(r"\{[\s\S]*\}", text)
        if json_match:
            return json.loads(json_match.group())
        return json.loads(text)
    except Exception:
        return {}
