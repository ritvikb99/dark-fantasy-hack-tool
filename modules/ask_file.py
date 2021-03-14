from pathlib import Path


def ask_file():
    while 1:
        path = Path(input(
            f"Enter the file name (eg: pass.txt, wordlist.txt)\n>"))
        if not path.is_file():
            print('[!] No such file!')
            continue
        return path
