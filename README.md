# Password Strength Evaluator

Python script that analyzes whether a password entered by the user is **secure or weak**, based on standard security criteria, with the option to retry until a strong password is achieved.


---

## Purpose

Weak passwords are the most common entry point in computer attacks. This script aims to:

- **Educate on good practices**: show exactly what a password is missing to be secure
- **Prevent brute force attacks**: complex passwords are exponentially harder to crack
- **Security awareness**: understand why certain requirements matter
- **First step in password policies**: foundation for implementing validations in real systems

---

## Security criteria evaluated

| Criterion | Validation | Why it matters |
|---|---|---|
| **Minimum length** | ≥ 8 characters | More characters = more possible combinations |
| **Uppercase letters** | At least one `A-Z` | Expands the key space |
| **Lowercase letters** | At least one `a-z` | Expands the key space |
| **Numeric digits** | At least one `0-9` | Adds variation to the pattern |
| **Special characters** | `! @ # $ % ^ & *` etc. | The hardest to predict in brute force attacks |

---

## How does it work?

The script uses regular expressions to check each criterion individually. If all criteria are satisfied, the password is marked as **STRONG**; otherwise, it is **WEAK** and the missing requirements are shown. The user is then given the option to try again with a new password.

### Program flow

```
Start
  └─ Prompt user for a password
      └─ Validate each criterion using regex
          └─ All criteria met?
              ├─ YES → Display "STRONG" and exit
              └─ NO  → Display "WEAK" with missing requirements
                  └─ Ask user: try again? (y/n)
                      ├─ YES → Go back to prompt
                      └─ NO  → Exit
```

### Functions

| Function | What it does |
|---|---|
| `is_strong_password(password)` | Checks all criteria and returns a boolean and a list of missing rules |
| `display_result(is_strong, missing)` | Prints the evaluation result and recommendations |

---

## Sample output

```
=== Security Assessment Tool ===

Enter password to test: abc
[-] Status: Password is WEAK.
   Requirements: 8+ chars, upper & lower letters, digits, and special symbols.

Do you want to change it? (y/n): y

Enter password to test: Segura#2024!
[+] Status: Password is STRONG and secure!
```

---

## Technologies

| Library | Usage |
|---|---|
| `re` | Regular expressions for pattern validation |

> Uses only the **Python standard library** — no external dependencies required.

---

## How to run it

```bash
python pass_segura.py
```

---

## Applied security concepts

- **Password entropy**: complexity increases the number of possible combinations, making brute-force attacks impractical
- **Defense in depth**: strong passwords are one layer of a secure authentication system
- **User feedback**: providing clear error messages helps users understand and improve their choices
