import re

def find_tandem_words(text: str) -> list[str]:
    if not text:
        return []
    words = re.findall(r'\b[а-яА-ЯёЁa-zA-Z]+\b', text)
    result = []
    for word in words:
        word_lower = word.lower()
        length = len(word_lower)
        if length >= 4 and length % 2 == 0:
            half = length // 2
            if word_lower[:half] == word_lower[half:]:
                result.append(word)
        elif length >= 5 and length % 2 != 0:
            half = length // 2
            if word_lower[:half] == word_lower[half+1:]:
                result.append(word)
    return list(dict.fromkeys(result))

def check_word(word: str) -> bool:
    word_lower = word.lower()
    length = len(word_lower)
    if length >= 4 and length % 2 == 0:
        half = length // 2
        return word_lower[:half] == word_lower[half:]
    elif length >= 5 and length % 2 != 0:
        half = length // 2
        return word_lower[:half] == word_lower[half+1:]
    return False