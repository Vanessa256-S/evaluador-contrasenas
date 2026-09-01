import re


def check_password_strength(password: str) -> bool:
    """Validate if a password meets minimum security criteria.

    Criteria:
    - At least 8 characters long
    - Contains uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character
    """
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    return not (
        length_error
        or digit_error
        or uppercase_error
        or lowercase_error
        or symbol_error
    )


def main() -> None:
    """Prompt user for password evaluation and dynamic updates."""
    print("=== Security Assessment Tool ===")

    while True:
        user_password = input("\nEnter password to test: ").strip()
        is_secure = check_password_strength(user_password)

        if is_secure:
            print("[+] Status: Password is STRONG and secure!")
            break

        print("[-] Status: Password is WEAK.")
        print(
            "   Requirements: 8+ chars, upper & lower letters, digits, and special symbols."
        )

        retry = input("\nDo you want to change it? (y/n): ").strip().lower()
        if retry != "y":
            print("[!] Exiting program without password modification.")
            break


if __name__ == "__main__":
    main()
