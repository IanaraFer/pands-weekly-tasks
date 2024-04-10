# Week task 3. Create a code that don't show the first 6 digit of the client Bank Account.
# Autor - Ianara Fernandes

def mask_bank_account(account_number):
    # Assuming account_number is a string
    masked_account =  '*' * (len(account_number) -6) + account_number[6:]
    return masked_account

# Example usage:
bank_account = "1234567890"
masked_result = mask_bank_account(bank_account)
print(f"Masked bank account: {masked_result}")