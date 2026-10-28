import re

TANDEM_REGEX = re.compile(r'\b(\w+)\w?\1\b', re.IGNORECASE)

def find_tandem_words(text: str) -> list[str]:
    """Находит все слова с тандемным повтором в тексте."""
    if not text:
        return []
    return list(dict.fromkeys([match.group(0) for match in TANDEM_REGEX.finditer(text)]))

def check_word(word: str) -> bool:
    """Проверяет, является ли одно слово тандемным повтором."""
    return bool(TANDEM_REGEX.fullmatch(word))