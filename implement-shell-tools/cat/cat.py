import sys
import argparse

def main():

    parser = argparse.ArgumentParser(prog="cat")
    parser.add_argument("-n", "--number", action="store_true", help="number all output lines")
    parser.add_argument("-b", "--number-nonblank", action="store_true", help="number nonempty output lines")
    parser.add_argument("files", nargs="*", help="files to read")

    args = parser.parse_args()
    
    show_all_numbers = args.number and not args.number_nonblank
    show_nonblank_numbers = args.number_nonblank

    line_count = 1

    for file_path in args.files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if show_nonblank_numbers:
                        if line.strip():
                            print(f"{line_count:>6}\t{line}", end='')
                            line_count += 1
                        else:
                            print(line, end='')
                    elif show_all_numbers:
                        print(f"{line_count:>6}\t{line}", end='')
                        line_count += 1
                    else:
                        print(line, end='')
        except FileNotFoundError:
            print(f"cat: {file_path}: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    main()