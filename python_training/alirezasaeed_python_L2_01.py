import string
from print_color import print
# welcome
# please pip install print-color


class PasswordValidator:
    _COMMON_PASSWORDS = [
        "123456",
        "password",
        "admin"
        "",
    ]
    _PASSWORD_SCORES = [
        (2, "very weak"),
        (4, "weak"),
        (6, "medium"),
        (8, "strong"),
    ]
    _letter_like_characters = {"a": ["@", "4"], "i": ["1", "!"], "s": ["$", "5"], "o": ["0"]}
    _password_score = 8

    def __init__(self, username: str, password: str):
        self.username = username.strip()
        self.password = password.strip()

    def validate(self)-> None:
        while True:
            score = self._password_score

            print("\nValidating password...", color="cyan")
            print("------------------------------------------------")
            if not (self.password and self.username):
                print("Username and password cannot be empty.", color="red")
                exit(1)

            if len(self.password) < 8:
                print("1. Password must be at least 8 characters long.", color="red")
                score -= 1

            if not any( char in string.ascii_letters for char in self.password):
                print("2. password must contain at least one a-z or A-Z character.", color="red")
                score -= 1

            if not any(char in string.punctuation for char in self.password):
                print("3. Password must contain at least one special character.", color="red")
                score -= 1

            if not any(char.isupper() for char in self.password):
                print("4. Password must contain at least one uppercase letter.", color="red")
                score -= 1

            if self.password.strip() == self.username.strip():
                print("5. Password must not be the same as the username.", color="red")
                score -= 1

            if self.username in self.password:
                print("6. Password must not contain the username.", color="red")
                score -= 1

            if self.leet_substitution():
                print("7. Password must not be the same as the username with leet substitutions.", color="red")
                score -= 1

            if self.password in self._COMMON_PASSWORDS:
                print("8. Password is too common.", color="red")
                score -= 1

            print("\n\npassword score for this password is:", self.score(score), color="magenta")
            print("------------------------------------------------")

            if score < 6:
                print("Password is not strong enough. Please try again.", color="yellow")
                self.password = input("Enter your password: ")

            else:
                print("Password is valid good by baby(:", color="green")
                break


    def score(self, score) -> int:
        for length, desc in sorted(self._PASSWORD_SCORES, key=lambda x: x[0], reverse=True):
            if score >= length:
                return desc

    def leet_substitution(self) -> bool:
        """
            Check and replace leet substitutions in the password.
            Returns True if any substitutions were made, False otherwise.
        """
        is_modified = False
        new_password = self.password

        for letter, substitutes in self._letter_like_characters.items():
            if is_modified:
                break

            for sub in substitutes:

                new_password = new_password.replace(sub, letter)
                if self.username == new_password:
                    is_modified = True
                    break

        return is_modified


if __name__ == "__main__":
    print("""
--- gol baray gol ---

   /\\_/\\
  ( o.o ) づ  @-->--
   > ^ <

--- sorry for delay(: ---
python_L2_01
by: alireza saeed
""", color="cyan")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    PasswordValidator(username, password).validate()
    