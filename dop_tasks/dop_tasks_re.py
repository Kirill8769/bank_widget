import re
from collections import Counter


def is_valid_email(email: str) -> bool:
    pattern = re.compile(r"\b[\w.-]+@[\w.-]+\.\w+\b")
    result = pattern.search(email)
    return bool(result)


print(is_valid_email("example@gmail.com"))  # True
print(is_valid_email("example.gmail.com"))  # False


def format_dates(text: str) -> str:
    result = re.sub(pattern=r"/", repl=".", string=text)
    return result


text = "Встреча назначена на 05/20/2022. Подтвердите свое участие 05/10/2022."
formatted_text = format_dates(text)
print(formatted_text)  # Встреча назначена на 05.20.2022. Подтвердите свое участие 05.10.2022.


def most_common_letter(string: str) -> list:
    result = Counter(string)
    return list(result.most_common(1)[0][0])


string = "Это последний урок модуля, позади много прорешенных задач, и я ооочень горжусь собой"
print(most_common_letter(string))  # ['о']
