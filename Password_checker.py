import sys
import re

def evaluate_password_strength(password):
    """
    Evaluates the strength of a password based on length, complexity, and common patterns.
    Returns a dictionary with score, strength level, and suggestions.
    """
    score = 0
    suggestions = []

    # Length check
    length = len(password)
    if length >= 8:
        score += 1
        if length >= 12:
            score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Complexity checks
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password))

    if has_lower:
        score += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    if has_upper:
        score += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    if has_digit:
        score += 1
    else:
        suggestions.append("Include at least one digit.")

    if has_symbol:
        score += 1
    else:
        suggestions.append("Include at least one special symbol.")

    # Common patterns check
    # Sequential characters (e.g., abc, 123)
    if re.search(r'(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz|012|123|234|345|456|567|678|789)', password.lower()):
        score -= 1
        suggestions.append("Avoid sequential characters like 'abc' or '123'.")

    # Repeated characters (e.g., aaa, 111)
    if re.search(r'(.)\1{2,}', password):
        score -= 1
        suggestions.append("Avoid repeated characters like 'aaa' or '111'.")

    # Common weak patterns (e.g., password, 123456)
    common_patterns = ['password', '123456', 'qwerty', 'admin', 'letmein']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 1
        suggestions.append("Avoid common words or sequences like 'password' or '123456'.")

    # Ensure score doesn't go below 0
    score = max(0, score)

    # Determine strength level
    if score >= 6:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return {
        'score': score,
        'strength': strength,
        'suggestions': suggestions
    }

def main():
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter a password to evaluate: ")

    result = evaluate_password_strength(password)

    print(f"Password Strength: {result['strength']} (Score: {result['score']}/8)")
    if result['suggestions']:
        print("Suggestions for improvement:")
        for suggestion in result['suggestions']:
            print(f"- {suggestion}")
    else:
        print("Your password is strong!")

if __name__ == "__main__":
    main()
