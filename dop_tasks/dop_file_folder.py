import os


def count_files_and_folders(path: str | None = None, recursive_count: bool = False) -> dict:
    """
    Подсчитывает количество файлов и папок в указанной директории.

    :param path: Путь до директории, для которой нужно выполнить подсчет (по умолчанию текущая директория).
    :param recursive_count: Флаг для включения рекурсивного подсчета файлов и папок (по умолчанию False).
    :return: Словарь с количеством файлов и папок в директории.
    """
    if not path:
        path = os.getcwd()

    files_count = 0
    folders_count = 0

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files_count += 1
            print(item_path)
        elif os.path.isdir(item_path):
            folders_count += 1
            print(item_path)
            if recursive_count:
                sub_count = count_files_and_folders(item_path, recursive_count=True)
                files_count += sub_count["files"]
                folders_count += sub_count["folders"]
    result = {"files": files_count, "folders": folders_count}
    return result


print(count_files_and_folders(recursive_count=True))
