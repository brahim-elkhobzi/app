class User:
    def __init__(self, name, email, password, balance=0):
        self.name = name
        self.email = email
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Balance: {self.balance}"


class BankingSystem:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open('users.txt', 'r') as file:
                for line in file:
                    email, name, password, balance = line.strip().split(',')
                    self.users[email] = User(name, email, password, float(balance))
        except FileNotFoundError:
            pass

    def save_users(self):
        with open('users.txt', 'w') as file:
            for user in self.users.values():
                file.write(f"{user.email},{user.name},{user.password},{user.balance}\n")

    def register(self, name, email, password):
        if email in self.users:
            print("Email already registered.")
            return False
        self.users[email] = User(name, email, password)
        self.save_users()
        print("Registration successful.")
        return True

    def login(self, email, password):
        if email in self.users and self.users[email].password == password:
            print("Login successful.")
            return self.users[email]
        print("Invalid email or password.")
        return None

    def __str__(self):
        return "\n".join([str(user) for user in self.users.values()])


def main():
    banking_system = BankingSystem()

    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            banking_system.register(name, email, password)
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = banking_system.login(email, password)
            if user:
                while True:
                    print("\nUser Menu:")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Logout")

                    user_choice = input("Enter your choice: ")

                    if user_choice == '1':
                        amount = float(input("Enter amount to deposit: "))
                        if user.deposit(amount):
                            print("Deposit successful.")
                        else:
                            print("Invalid amount.")
                    elif user_choice == '2':
                        amount = float(input("Enter amount to withdraw: "))
                        if user.withdraw(amount):
                            print("Withdrawal successful.")
                        else:
                            print("Insufficient balance or invalid amount.")
                    elif user_choice == '3':
                        print(f"Your balance is: {user.balance}")
                    elif user_choice == '4':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    banking_system.save_users()


if __name__ == "__main__":
    main()
