# This file is used for Git practice.
# It will be constantly updated, changed, and deleted as I learn.

def greet_user(name: str):
    print(f"Hello, {name}! Welcome to Git practice.")

def main():
    user_name = "Developer"
    greet_user(user_name)
    
    tasks = ["Learn Git status", "Make a commit", "Create a branch"]
    
    print("My current tasks:")
    for task in tasks:
        print(f"- {task}")

if __name__ == "__main__":
    main()