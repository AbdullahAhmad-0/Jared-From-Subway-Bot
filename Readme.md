# Jared From Subway Bot

Jared From Subway Bot is a Telegram bot that enables fast and efficient trading of SPL tokens on the Solana blockchain. It allows users to generate wallets, check balances, buy or sell tokens, and track wallets—all through an intuitive Telegram interface.

---

## Features

- Generate new Solana wallets.
- Get the balance of any Solana wallet.
- Buy or sell SPL tokens.
- Track a wallet's balance and transactions.
- Manage trading orders (coming soon).
- Built with Python, utilizing the python-telegram-bot library and Solana's blockchain API.

---

## Installation

1. Clone the repository:
   git clone https://github.com/AbdullahAhmad-0/Jared-From-Subway-Bot.git
   cd Jared-From-Subway-Bot

2. Install required dependencies:
   pip install python-telegram-bot
   pip install solana
   pip install pyperclip

3. Update the following variables in the script:
   - `TOKEN`: Your bot's Telegram token.
   - `BOT_USERNAME`: Your bot's username on Telegram.
   - `SOLANA_RPC_ENDPOINT`: Your Solana RPC endpoint (e.g., Devnet or Mainnet).
   - `SOLANA_PRIVATE_KEY`: Private key for your Solana wallet.

---

## Usage

1. Start the bot:
   python main.py

2. Interact with the bot in Telegram using these commands:
   - /start - Welcome message and main menu.
   - /help - Display a list of available commands.
   - /generate_wallet - Generate a new Solana wallet.
   - /get_balance - Check the balance of a wallet.
   - /buy_token - Buy SPL tokens.
   - /sell_token - Sell SPL tokens.
   - /track_wallet - Track a specific wallet.

---

## Code Highlights

- **Wallet Generation**:
  The bot generates new Solana wallets using the `Account` class:
  new_wallet = Account()
  print(f"New Wallet Address: {new_wallet.public_key()}")

- **Balance Retrieval**:
  Fetch wallet balance using Solana's RPC client:
  balance = solana_client.get_balance(PublicKey(wallet_address))
  print(f"Balance: {lam_to_sol(balance['result']['value'])} SOL")

- **Token Transfers**:
  Transfer tokens securely with the Solana API:
  transaction = Transaction().add(transfer(TransferParams(
      from_pubkey=sender.public_key,
      to_pubkey=receiver.public_key,
      lamports=sol_to_lam(amount)
  )))

---

## Contributing

Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed explanation of changes.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgments

- python-telegram-bot for the bot's core functionality.
- Solana blockchain for enabling fast and secure transactions.

---

## Disclaimer

The safety of user funds is a priority. Ensure private keys are not exposed to maintain wallet security. Use at your own risk.
