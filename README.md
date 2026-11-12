*This project has been created as part of the 42 curriculum by samalves.*

# ft_otp

## Description

ft_otp is a project from the 42 Cybersecurity Piscine. It stores a hexadecimal secret encrypted and generates six-digit, time-based one-time passwords.

The program implements the HOTP calculation with HMAC-SHA1 and dynamic truncation. It derives the moving counter from the current time in 30-second intervals, following the TOTP approach.

## Instructions

### Requirements

- Python 3
- `cryptography`

Install `cryptography` if it is not already available in your Python environment:

```bash
python3 -m pip install cryptography
```

No compilation is required.

### Store a secret

Create a text file containing a hexadecimal key of at least 64 characters. From the project directory, run:

```bash
python3 ./ft_otp.py -g key.hex
```

The program validates the key and creates:

- `ft_otp.key` — the encrypted OTP secret
- `.fernet` — the Fernet key used to decrypt the secret

### Generate an OTP

Run the following command from the directory containing `ft_otp.key` and `.fernet`:

```bash
python3 ./ft_otp.py -k ft_otp.key
```

The program prints a six-digit OTP for the current 30-second time interval.

Keep both generated files private. Anyone with access to `ft_otp.key` and `.fernet` can recover the original secret.

## Resources

- [RFC 4226](https://datatracker.ietf.org/doc/html/rfc4226) — HOTP algorithm.
- [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238) — TOTP, the time-based variant built on HOTP.
- [Python `argparse`](https://docs.python.org/3/library/argparse.html) — command-line argument parsing.
- [Python `pathlib`](https://docs.python.org/3/library/pathlib.html) — filesystem paths.
- [Python `hmac`](https://docs.python.org/3/library/hmac.html) — HMAC computation.
- [Python `hashlib`](https://docs.python.org/3/library/hashlib.html) — hash algorithms, including SHA-1.
- [Fernet documentation](https://cryptography.io/en/latest/fernet/) — authenticated symmetric encryption.

### Use of AI

AI assistance was used to explain Python concepts, discuss implementation approaches, help reason about debugging output, and draft this README. The student implemented and tested the program and is responsible for reviewing and understanding the submitted code.

## Project Structure and Technical Choices

The repository contains the `ft_otp.py` command-line program and this README. The program uses Fernet to encrypt and decrypt the stored secret, and implements the HOTP calculation with HMAC-SHA1 and dynamic truncation. For time-based OTP generation, it derives the counter from the current time in 30-second intervals.