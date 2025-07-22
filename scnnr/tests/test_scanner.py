from scnnr.file_scanner import scan_files, count_files
from pprint import pprint

if __name__ == "__main__":
    path = "."
    files = scan_files(path, extensions=[".py", ".js"])
    pprint(count_files(files))
