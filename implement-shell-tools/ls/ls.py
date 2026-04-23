import os
import sys
import argparse

def main():

    parser = argparse.ArgumentParser(prog="ls")
    parser.add_argument("-1", action="store_true", help="List one file per line")
    parser.add_argument("-a", "--all", action="store_true", help="Do not ignore entries starting with .")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to list")

    args = parser.parse_args()

    try:
        target_dir = args.directory
        files = os.listdir(target_dir)

        if args.all:
            files.extend([".", ".."])
        else:
            files = [f for f in files if not f.startswith('.')]
        files.sort()

        if args.__dict__['1']:
            for f in files:
                print(f) 
        else:
            print(" ".join(files))   
    
    except FileNotFoundError:
        print(f"ls: {args.directory}: No such file or directory", file=sys.stderr)

if __name__ == "__main__":
    main()
    