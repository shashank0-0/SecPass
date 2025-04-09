import os
import random
import string
import argparse
from getpass import getpass
from zxcvbn import zxcvbn
from colorama import init, Fore

# Initialize colorama (needed for Windows)
init(autoreset=True)

# Define colors
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RESET = Fore.RESET

# ASCII Banner (unchanged)
BANNER = f"""
{YELLOW}      ######   ########   ######   ########      ###      ######    ######  {RESET}
{YELLOW}     ##    ##  ##        ##    ##  ##     ##    ## ##    ##    ##  ##    ## {RESET}
{YELLOW}     ##        ##        ##        ##     ##   ##   ##   ##        ##       {RESET}
{YELLOW}      ######   ######    ##        ########   ##     ##   ######    ######  {RESET}
{YELLOW}           ##  ##        ##        ##         #########        ##        ## {RESET}
{YELLOW}     ##    ##  ##        ##    ##  ##         ##     ##  ##    ##  ##    ## {RESET}
{YELLOW}      ######   ########   ######   ##         ##     ##   ######    ######  {RESET}
          {GREEN}Password Strength Tool{RESET}
"""

def generate_suggestion(password):
    suggestion = list(password)

    while len(suggestion) < 12:
        suggestion.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    if not any(c.isupper() for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = random.choice(string.ascii_uppercase)

    if not any(c.islower() for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = random.choice(string.ascii_lowercase)

    if not any(c.isdigit() for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = random.choice(string.digits)

    if not any(c in string.punctuation for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = random.choice(string.punctuation)

    substitutions = {'a': '@', 's': '$', 'o': '0', 'i': '1', 'e': '3'}
    for i, c in enumerate(suggestion):
        if c.lower() in substitutions and random.random() < 0.5:
            suggestion[i] = substitutions[c.lower()].upper() if c.isupper() else substitutions[c.lower()]

    return ''.join(suggestion)

def analyze_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']
    levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_text = levels[score]

    if score <= 1:
        color = RED
    elif score == 2:
        color = YELLOW
    else:
        color = GREEN

    return f"{color}{strength_text}{RESET}", feedback

def main():
    parser = argparse.ArgumentParser(description="SecPass: Analyze password strength and suggest improvements.")
    args = parser.parse_args()

    print(BANNER)

    # Prompt for password without exposing it or storing in shell history
    password = getpass("Enter your password: ")

    strength, feedback = analyze_strength(password)
    print(f"\nPassword strength: {strength}")

    if feedback:
        print("Feedback:")
        for line in feedback:
            print(f"- {line}")

    print("\nSuggestions to improve your password:")
    suggestions = set()
    while len(suggestions) < 3:
        new_suggestion = generate_suggestion(password)
        if new_suggestion not in suggestions:
            suggestions.add(new_suggestion)
            print(f"- {new_suggestion}")

if __name__ == "__main__":
    main()
