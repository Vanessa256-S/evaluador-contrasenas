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
