# pip install python-telegram-bot
# pip install solana
# pip install pyperclip
# import pyperclip
from typing import Final

import requests
from base58 import b58decode
from solana.publickey import PublicKey
from telegram.constants import ParseMode
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, CallbackQueryHandler
import os
import time

from solana.account import Account
from solana.rpc.api import Client
from solana.transaction import Transaction, TransactionInstruction, AccountMeta

from solana.keypair import Keypair
from solana.system_program import TransferParams, transfer

# Set your Solana RPC endpoint
SOLANA_RPC_ENDPOINT = "https://api.devnet.solana.com"

# Set your Solana wallet private key
SOLANA_PRIVATE_KEY = [41, 25, 64, 10, 25, 72, 75, 154, ...]  # Solana Wallet Private Key
OUR_ADDRESS = 'Your Wallet Address'
# Initialize Solana client and account
solana_client = Client(SOLANA_RPC_ENDPOINT)
solana_account = Account(secret_key=SOLANA_PRIVATE_KEY[0:32])

TOKEN: Final = r'Bot Token'
BOT_USERNAME: Final = '@Jared_FromSubwayBot'  # Your Bot Username
BOT_STATE = {'all': 'Default'}
BOT_STATE2 = {'all': 'Default'}

def lam_to_sol(lamports):
    return lamports / 10**9

def sol_to_lam(sol):
    return int(sol * 10**9)

def solana_token_transfer(sender_pubkey, receiver_pubkey, amount):
    client: Client = solana_client

    sender, receiver = Keypair.from_seed(bytes(PublicKey(sender_pubkey))), Keypair.from_seed(bytes(PublicKey(receiver_pubkey)))

    airdrop = client.request_airdrop(sender.public_key, sol_to_lam(int(amount)))
    airdrop_signature = airdrop["result"]
    client.confirm_transaction(airdrop_signature)

    transaction = Transaction().add(transfer(TransferParams(
        from_pubkey=sender.public_key,
        to_pubkey=receiver.public_key,
        lamports=1_000_000)
    ))

    client.send_transaction(transaction, sender)


if __name__ == '__main__':
    x = input('Enter sender pub key: ')
    y = 'mSoLzYCxHdYgdzU16g5QSh3i5K3z3KZK7ytfqcJm7So'
    z = input('Enter amount: ')
    solana_token_transfer(x, y, z)