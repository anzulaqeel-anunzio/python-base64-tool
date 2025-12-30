# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from base64_tool.core import Base64Tool

def main():
    parser = argparse.ArgumentParser(description="Base64 Encoder/Decoder Tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Encode command
    enc_parser = subparsers.add_parser("encode", help="Encode string or file to Base64")
    enc_parser.add_argument("input", help="Input string or file path")
    enc_parser.add_argument("--file", "-f", action="store_true", help="Treat input as file path")
    enc_parser.add_argument("--output", "-o", help="Save output to text file")

    # Decode command
    dec_parser = subparsers.add_parser("decode", help="Decode Base64 to string or file")
    dec_parser.add_argument("input", help="Base64 string or file path containing b64 data")
    dec_parser.add_argument("--input-file", action="store_true", help="Input is a path to a text file containing the b64 string")
    dec_parser.add_argument("--output", "-o", help="Save decoded result to file (binary/text)")

    args = parser.parse_args()

    if args.command == "encode":
        result = ""
        if args.file:
            if not os.path.exists(args.input):
                print(f"Error: File '{args.input}' not found.")
                sys.exit(1)
            result = Base64Tool.encode_file(args.input)
        else:
            result = Base64Tool.encode_string(args.input)

        if args.output:
            try:
                with open(args.output, "w") as f:
                    f.write(result)
                print(f"Encoded output saved to {args.output}")
            except Exception as e:
                print(f"Error saving output: {e}")
        else:
            print(result)

    elif args.command == "decode":
        b64_data = args.input
        if args.input_file:
             if not os.path.exists(args.input):
                print(f"Error: File '{args.input}' not found.")
                sys.exit(1)
             try:
                 with open(args.input, 'r') as f:
                     b64_data = f.read().strip()
             except Exception as e:
                 print(f"Error reading input file: {e}")
                 sys.exit(1)

        if args.output:
            success, msg = Base64Tool.decode_file(b64_data, args.output)
            if success:
                print(f"Decoded data saved to {args.output}")
            else:
                print(msg)
                sys.exit(1)
        else:
            print(Base64Tool.decode_string(b64_data))
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
