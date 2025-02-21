"""
Search and Replace text across Markdown files
"""

import re
from pathlib import Path


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def replace_text_in_content(content, search_text, replacement_text):
    return re.sub(search_text, replacement_text, content)


def process_directory(directory_path, search_text, replacement_text):
    pathlist = Path(directory_path).glob('**/*.md')
    for path in pathlist:
        path_in_str = str(path)
        print(f'Processing file: {path_in_str}')

        content = read_file(path_in_str)
        new_content = replace_text_in_content(content, search_text, replacement_text)
        write_file(path_in_str, new_content)


def main():
    """
    Runs all the functions for collection and deployment
    :rtype: None
    """
    directory_path = input("Enter the directory path: ")
    search_text = input("Enter the text to search for: ")
    replacement_text = input("Enter the text to replace with: ")

    process_directory(directory_path, search_text, replacement_text)
    print("Text replacement completed.")


if __name__ == '__main__':
    main()
