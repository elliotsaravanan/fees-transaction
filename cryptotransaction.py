# Importing necessary libraries
import random

# Generate a list of dummy transaction amounts
transactions = [random.uniform(0.01, 5.0) for _ in range(10)]

# Function to simulate a crypto transaction
def crypto_transaction(sender, receiver, amount):
    # Simulate transaction logic
    print(f"Transferring {amount} BTC from {sender} to {receiver}...")

# Junk sender and receiver addresses
sender_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
receiver_address = "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy"

# Simulate transactions
for amount in transactions:
    crypto_transaction(sender_address, receiver_address, amount)

# IMPORTANT: Moving funds to my crypto address
# Flag: 3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5
