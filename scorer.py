import re

_STOPWORDS = {"the", "a", "an", "is", "are", "at", "in", "on", "of", "and", "to", "for"}

def _normalize(text: str) -> str:
    # TODO: lowercase, strip punctuation. Keep it simple —
    # str.lower() + a regex or str.translate to drop punctuation is enough.

    clean_text = re.sub(r'[^\w\s]', '', text)
    return clean_text.strip().lower()

def _keywords(text: str) -> set[str]:
    # TODO: normalize, split on whitespace, drop stopwords, return a set.
    normalize_text = _normalize(text)
    words = normalize_text.split(" ")
    filtered_words = [w for w in words if w not in _STOPWORDS]

    return set(filtered_words)




def judge(question: str, expects: str, answer: str, results: dict) -> bool:
    # results is actually a list of retrieved-chunk objects, not a dict —
    # fix the type hint on the parameter above too.
    if not expects:
        return False

    expected_words = _keywords(expects)
    answer_words = _keywords(answer)

    if not expected_words:
        return False  # nothing meaningful to check against

    overlap = expected_words & answer_words
    fraction_matched = len(overlap) / len(expected_words)

    return fraction_matched >= 0.7