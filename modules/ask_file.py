from pathlib import Path


def ask_file():
    while 1:
        path = Path(input(
            f"Enter the file name (eg: pass.txt, wordlist.txt)\n>"))
        try:
            path.is_file()
        except:
            raise FileNotFoundError('[!] No such file!')
        else:
            return path
