# imports
import argparse
from pathlib import Path
import string

# -k: counter 30s

# -k: unix hour manager

# -k: SHA1 print 6 digits

# -g: hex.key validation (for -g and -k) if needed

# -k:check file existence

# -k: start the process: checkers and generator

# -g: validation, encryptation and file creation
def is_valid_hex_key(text):
    return (
        len(text) >= 64
        and len(text) % 2 == 0
        and all(char in string.hexdigits for char in text)
    )

# -g: hex settings: checkers and start the process
def generate_key(files):
    try:
        hex_text = Path(files).read_text(encoding="ascii").strip()
    except (OSError, UnicodeError) as error:
        raise ValueError(f"Could not read key file: {error}") from error
    if not is_valid_hex_key(hex_text):
        raise ValueError("key must contain at least 64 hexadecimal characters")
    
# parsing arguments
def parse_args():
    parser = argparse.ArgumentParser(prog="ft_otp")
    operation = parser.add_mutually_exclusive_group(required=True)
    operation.add_argument(
        "-g",
        action="store_true",
        help="Encrypt and store .hex key",
    )
    operation.add_argument(
        "-k",
        action="store_true",
        help="Generate a temporary password",
    )
    parser.add_argument(
        "files",
        help=".hex file for -g, or .key file for -k",
    )
    return parser.parse_args()

# main function
def otp_router(args):
    if args.g:
        generate_key(args.files)
    elif args.k:
        generate_otp(args.files)

def main():
    args = parse_args()
    otp_router(args)

if __name__ == "__main__":
    main()