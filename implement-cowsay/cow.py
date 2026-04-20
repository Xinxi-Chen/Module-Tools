
import argparse
import cowsay

def main():
    supported_animals = sorted(cowsay.char_names)
    parser = argparse.ArgumentParser(prog="cowsay", description="Make animals say things")
    parser.add_argument("message", nargs="+", help="The message to say.")
    parser.add_argument("--animal", default="cow", choices=supported_animals,help="The animal to be saying things.")

    args = parser.parse_args()

    message_text = " ".join(args.message)
    func = getattr(cowsay, args.animal)
    func(message_text)

if __name__ == "__main__":
    main()