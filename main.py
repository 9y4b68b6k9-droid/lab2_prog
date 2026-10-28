import re
import urllib.request
import urllib.error

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
                result.append(word_lower)
    return list(set(result))

def check_word(word: str) -> bool:
    word_lower = word.lower()
    length = len(word_lower)
    if length < 4:
        return False
    if length % 2 == 0:
        half = length // 2
        return word_lower[:half] == word_lower[half:]
    else:
        return False

def process_file(filepath: str) -> None:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            text = f.read()
        print(f"\nПоиск в файле: {filepath}")
        words = find_tandem_words(text)
        print(f"Найдено {len(words)} слов: {', '.join(words)}" if words else "Не найдено.")
    except FileNotFoundError:
        print(f"Ошибка: файл {filepath} не найден.")

def process_url(url: str) -> None:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8', errors='ignore')
        text = re.sub(r'<[^>]+>', ' ', html)
        print(f"\nПоиск по URL: {url}")
        words = find_tandem_words(text)
        print(f"Найдено {len(words)} слов: {', '.join(words)}" if words else "Не найдено.")
    except urllib.error.URLError:
        print("Ошибка: не удалось подключиться к сайту.")

def main() -> None:
    print("=== Поиск тандемных повторов ===")
    while True:
        print("\n1. Проверить слово\n2. Ввести текст\n3. Файл\n4. URL\n0. Выход")
        choice = input("Выбор: ").strip()
        if choice == "1":
            word = input("Слово: ").strip()
            print(f"'{word}' - {'ДА' if check_word(word) else 'НЕТ'}")
        elif choice == "2":
            text = input("Текст: ").strip()
            print(find_tandem_words(text))
        elif choice == "3":
            process_file(input("Путь к файлу: ").strip())
        elif choice == "4":
            process_url(input("URL: ").strip())
        elif choice == "0":
            break

if __name__ == "__main__":
    main()