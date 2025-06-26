import random
import pyfiglet
from rich.console import Console

# Initialize Rich console for styled output
console = Console()

# Create banner using pyfiglet
banner = pyfiglet.figlet_format("Virtual Number Generator", font="slant")
coder = "Coded by Pakistani Ethical Hacker Mr Sabaz Ali Khan"

# Display banner and coder name
console.print(banner, style="bold green")
console.print(coder, style="bold cyan", justify="center")
console.print("\nWelcome to the Virtual Phone Number Generator!\n", style="bold yellow")

def generate_phone_number():
    # First digit between 6-9 (common for mobile numbers)
    phone_number = [random.randint(6, 9)]
    # Generate remaining 9 digits (0-9)
    for _ in range(9):
        phone_number.append(random.randint(0, 9))
    # Format as XXX-XXX-XXXX
    return f"{''.join(map(str, phone_number[:3]))}-{''.join(map(str, phone_number[3:6]))}-{''.join(map(str, phone_number[6:]))}"

def main():
    try:
        # Ask user how many numbers to generate
        num_count = int(input("How many phone numbers do you want to generate? (Enter a positive number): "))
        if num_count <= 0:
            raise ValueError("Number must be positive.")
        
        console.print("\nGenerated Phone Numbers:", style="bold magenta")
        for i in range(num_count):
            phone = generate_phone_number()
            console.print(f"{i+1}. {phone}", style="white")
    
    except ValueError as e:
        console.print(f"Error: {e}. Please enter a valid positive number.", style="bold red")
    except Exception as e:
        console.print(f"An unexpected error occurred: {e}", style="bold red")

if __name__ == "__main__":
    main()
