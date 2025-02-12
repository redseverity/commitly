import os

# Define ANSI escape codes for colored text
blue = "\033[34m"
yellow = "\033[33m"
red = "\033[31m"
white = "\033[37m"
bold = "\033[1m"
reset = "\033[0m"

# Global variable to store the selected commit type
chosenType = ""

# List of commit types following Conventional Commits format
Types = [
    "feat:      A new feature.",
    "fix:       A bug fix.",
    "docs:      Documentation changes.",
    "style:     Code style changes (e.g. formatting).",
    "refactor:  Code refactoring without changing functionality.",
    "perf:      Performance improvements.",
    "test:      Adding or modifying tests.",
    "chore:     Routine tasks (e.g. updating dependencies).",
    "build:     Build-related changes (e.g. Webpack configuration).",
    "ci:       Continuous integration configuration.",
    "revert:   Revert a previous commit.",
    "hotfix:   Urgent fix for production."
]

# Function to clear the terminal screen
def Clear():
    os.system('clear')

# Function to prompt the user to select a commit type
def SelectType():
    global chosenType  # Use the global variable to store the selected type

    Clear()
    print(f"{yellow + bold}Commitly lobby\n")
    print(f"{white}Select the type of commit (Conventional Commits):\n")
    
    while True:  # Keep asking until the user provides a valid choice

        # Display commit options with their corresponding numbers
        for idx, commit in enumerate(Types, 1):
            print(f"{blue}{idx}) {commit}")
        
        # Get user input
        choice = input(f"\n{white}Enter the number of your choice: ")
        
        try:
            choice = int(choice)  # Convert input to an integer
            
            # Check if the input is within the valid range
            if 1 <= choice <= len(commitType):
                CommitType = Types[choice - 1].split(":")[0]
                print(f"\nYou selected: {yellow}{Types}{reset}")
                break  # Exit the loop on valid input
            else:
                Clear()
                print(f"\n{red}...Invalid choice! Please select a number between 1 and 12.\n")
        
        except ValueError:  # Handle non-numeric input
            Clear()
            print(f"\n{red}...Invalid input! Please enter a valid number.\n")

# Main function to run the program
def main():
    try:
        SelectType()
    except KeyboardInterrupt:  # Handle interruption
        Clear()
        print(f'{red+bold}Stopped!{reset}')

# Run the program
main()
