# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

def get_valid_number(prompt, is_integer=False):
    """Prompts the user until a valid number is entered.

    Args:
        prompt (str): The input prompt for the user.
        is_integer (bool): Whether to validate the input as an integer.

    Returns:
        float or int: The validated number entered by the user.
    """
    while True:
        user_input = input(prompt)
        try:
            # Convert to int or float based on the flag
            return int(user_input) if is_integer else float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = get_valid_number("Enter savings balance: ")
    savings_interest = get_valid_number("Enter savings interest rate: ")
    savings_maturity = get_valid_number("Enter savings maturity (in months): ", is_integer=True)

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_maturity
    )

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"Your Updated Savings Balance is: ${updated_savings_balance:.2f}")
    print(f"Savings Interest Earned is: ${interest_earned:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = get_valid_number("Enter CD account balance: ")
    cd_interest = get_valid_number("Enter CD interest rate: ")
    cd_months = get_valid_number("Enter CD maturity (in months): ", is_integer=True)

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"Your Updated CD Balance is: ${updated_cd_balance:.2f}")
    print(f"CD Interest Earned is: ${cd_interest_earned:.2f}")

# if __name__ == "__main__":
#     main()
main()