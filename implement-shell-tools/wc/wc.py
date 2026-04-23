import sys
import argparse

def main():
    parser = argparse.ArgumentParser(prog="wc")
    parser.add_argument("-l", action="store_true", help="count lines")
    parser.add_argument("-w", action="store_true", help="count words")
    parser.add_argument("-c", action="store_true", help="count bytes")
    parser.add_argument("files", nargs="*", help="files to process")

    args = parser.parse_args()

    show_all = not (args.l or args.w or args.c)
    total_l, total_w, total_c = 0, 0, 0

    for file_path in args.files:
        try:
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                text_data = raw_data.decode('utf-8', errors='ignore')

                l_count = text_data.count('\n')
                w_count = len(text_data.split())
                c_count = len(raw_data)

                total_l += l_count 
                total_w += w_count
                total_c += c_count

                results = []
                if args.l or show_all: results.append(f"{l_count:>7}")
                if args.w or show_all: results.append(f"{w_count:>7}")
                if args.c or show_all: results.append(f"{c_count:>7}")
                print(f"{' '.join(results)} {file_path}")
        
        except Exception as e:
            print(f"wc: {file_path}: {e}", file=sys.stderr)
    
    if len(args.files) > 1:
        results = []
        if args.l or show_all: results.append(f"{total_l:>7}")
        if args.w or show_all: results.append(f"{total_w:>7}")
        if args.c or show_all: results.append(f"{total_c:>7}")
        print(f"{' '.join(results)} total")

if __name__ == "__main__":
    main()
