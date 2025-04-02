import os
import random
import string
import argparse
from getpass import getpass
from zxcvbn import zxcvbn
from colorama import init, Fore

# Initialize colorama (needed for Windows)
init(autoreset=True)

# Define colors (works on both Windows & Linux)
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
RESET = Fore.RESET

# ASCII Banner
BANNER = f"""
   {YELLOW}_____           ____{RESET}
  {YELLOW}/ ___/___  _____/ __ \\____ ___________{RESET}
  {YELLOW}\\__ \\/ _ \\/ ___/ /_/ / __ `/ ___/ ___/{RESET}
 {YELLOW}___/ /  __/ /__/ ____/ /_/ (__  |__  ){RESET}
{YELLOW}/____/\\___/\\___/_/    \\__,_/____/____/{RESET}

          {GREEN}Password Strength Tool{RESET}
"""

# Function to generate stronger password suggestions
def generate_suggestion(password):
    suggestion = list(password)

    while len(suggestion) < 12:
        suggestion.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    if not any(c.isupper() for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        while not suggestion[idx].islower():
            idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = suggestion[idx].upper()

    if not any(c.islower() for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        while not suggestion[idx].isupper():
            idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = suggestion[idx].lower()

    if not any(c.isdigit() for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = random.choice(string.digits)

    if not any(c in string.punctuation for c in suggestion):
        idx = random.randint(0, len(suggestion) - 1)
        suggestion[idx] = random.choice(string.punctuation)

    substitutions = {'a': '@', 's': '$', 'o': '0', 'i': '1', 'e': '3'}
    for i, c in enumerate(suggestion):
        if c.lower() in substitutions and random.random() < 0.5:
            suggestion[i] = substitutions[c.lower()]
            if c.isupper():
                suggestion[i] = suggestion[i].upper()

    return ''.join(suggestion)

# Function to analyze password strength and return with color
def analyze_strength(password):
    result = zxcvbn(password)
    score = result['score']
    feedback = result['feedback']['suggestions']
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_text = strength_levels[score]

    # Apply color based on strength
    if score <= 1:
        colored_strength = f"{RED}{strength_text}{RESET}"
    elif score == 2:
        colored_strength = f"{YELLOW}{strength_text}{RESET}"
    else:
        colored_strength = f"{GREEN}{strength_text}{RESET}"

    return colored_strength, feedback

# Main function
def main():
    parser = argparse.ArgumentParser(description="SecPass: A CLI tool to analyze password strength and suggest improvements.")
    parser.add_argument("-p", "--password", help="Password to analyze (if not provided, you'll be prompted securely)")

    args = parser.parse_args()

    # Display banner
    print(BANNER)

    # Get password from argument or prompt
    if args.password:
        password = args.password
    else:
        password = getpass("Enter your password: ")

    # Analyze the password strength
    strength, feedback = analyze_strength(password)
    print(f"Password strength: {strength}")

    if feedback:
        print("Feedback:")
        for f in feedback:
            print(f"- {f}")

    # Generate and display 2-3 unique suggestions
    print("\nSuggestions to improve your password:")
    suggestions = set()
    while len(suggestions) < 3:
        suggestion = generate_suggestion(password)
        if suggestion not in suggestions:
            suggestions.add(suggestion)
            print(f"- {suggestion}")

# Ensure script runs properly when executed directly
if __name__ == "__main__":
    main()
