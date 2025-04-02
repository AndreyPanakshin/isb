def read(file_path: str) -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read().strip()
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return ""


def write(data: str, file_path: str) -> None:
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)
    except Exception as e:
        print(f"Ошибка при записи в файл {file_path}: {e}")
