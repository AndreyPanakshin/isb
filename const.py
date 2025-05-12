cpp_subs="cpp_subs.txt"
java_subs="java_subs.txt"

test_result_cpp = "test_result_cpp.txt"
test_result_java = "test_result_java.txt"

PI = [0.2148, 0.3672, 0.2305, 0.1875]

def read_file(filename: str) -> str:
    """
    Reads the sequence
    :param filename: Path to the file to read.
    :return: The sequence
    """

    try:

        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()

    except Exception as e:

        print(f"Error reading file: {e}")


def write_file(filename: str, text: str) -> None:
    """
    Writes the given text to a file.
    :param filename: Path to the file to write to.
    :param text: The text
    :return: None
    """

    try:

        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)

    except Exception as e:

        print(f"Error writing file: {e}")
