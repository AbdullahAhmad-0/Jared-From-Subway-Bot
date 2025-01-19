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


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(
        f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    buttons = [
        [InlineKeyboardButton("Generate Wallet", callback_data="/generate_wallet"),
         InlineKeyboardButton("Get Balance", callback_data="/get_balance")],

        [InlineKeyboardButton("Buy Token", callback_data="/buy_token"),
         InlineKeyboardButton("Sell Token", callback_data="/sell_token")],

        [InlineKeyboardButton("Track Wallet", callback_data="/track_wallet"),
         InlineKeyboardButton("Set Order", callback_data="/set_order")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(f"Welcome to Jared From Subway Bot!\n"
                                    "Solana's fastest bot to trade any coin (SPL token), and the official Telegram trading bot.\n\n"
                                    # "You currently have no SOL balance. To get started with trading, send some SOL to your Jared From Subway Bot wallet address:\n"
                                    # f"9ZfdCP772E3rrcE3tv4 (tap to copy)\n\n"
                                    # "Once done, tap refresh, and your balance will appear here.\n\n"
                                    # "To buy a token, just enter a token address or post the birdeye link of the coin.\n\n"
                                    "For more info on your wallet and to retrieve your private key, tap the wallet button below. "
                                    "We guarantee the safety of user funds on Jared From Subway Bot, but if you expose your private key, your funds will not be safe..", reply_markup=reply_markup)

    BOT_STATE[update.message.chat.id] = 'Default'


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    buttons = [
        [InlineKeyboardButton("Generate Wallet", callback_data="/generate_wallet"),
         InlineKeyboardButton("Get Balance", callback_data="/get_balance")],

        [InlineKeyboardButton("Buy Token", callback_data="/buy_token"),
         InlineKeyboardButton("Sell Token", callback_data="/sell_token")],

        [InlineKeyboardButton("Track Wallet", callback_data="/track_wallet"),
         InlineKeyboardButton("Set Order", callback_data="/set_order")]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text("Public Commands:\n"
                                    # " /cleartrades - Clears all of your current trades (both active and disabled)\n"
                                    "/help - Prints this help message\n"
                                    "/generate_wallet - Generate Wallet\n"
                                    "/get_balance - Get Balance\n"
                                    "/buy_token - Buy Token\n"
                                    "/sell_token - Sell Token\n"
                                    "/track_wallet - Track Wallet\n"
                                    "/set_order - Set Order\n",
                                    reply_markup=reply_markup)
    # " /import - Imports a wallet from one chain to the other\n"
    # " /monitor - Spawns the trade monitor panel in case the user deletes it by accident\n"
    # " /partner - Spawn the quick buy menu for our current partner\n"
    # " /premium - Spawns the premium menu to upgrade subscription\n"
    # " /quick - Summons the sniperbot quick panel\n"
    # " /referral - Pops up the referral menu\n"
    # " /sniper - Summons the sniperbot main panel\n"
    # " /srgwallets - Reveals all of your connected Surge wallets\n"
    # " /start - Let's get this party started! 🎉\n"
    # " /trending - Gets top trending hits\n"
    # " /tutorial - Print the sniper manual link\n"
    # " /wallets - Reveals all of your connected wallets\n")

    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(
        f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    BOT_STATE[update.message.chat.id] = 'Default'


async def generate_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    new_wallet = Account()
    message_text = (
        f"New Solana wallet generated:\n"
        f"Address: ```{new_wallet.public_key()}```\(tap to copy\)\n"
        f"Private Key: ```{new_wallet.secret_key()}```\(tap to copy\)"
    )
    BOT_STATE2[update.message.chat.id] = [Update, context]
    await update.message.reply_text(message_text, parse_mode=ParseMode.MARKDOWN_V2)


def lam_to_sol(lamports):
    return lamports / 10 ** 9


def sol_to_lam(sol):
    return int(sol * 10 ** 9)


async def get_balance(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # balance = solana_client.get_balance(solana_account.public_key())
    # await update.message.reply_text(f"Your Solana wallet balance: {lam_to_sol(balance['result']['value'])} sol")
    await update.message.reply_text("Please Enter Your Wallet Address")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'GET'


async def buy_token(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please Enter Your Wallet Address, Amount To Buy")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'BUY'


async def sell_token(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please Enter Your Wallet Address, Amount To Sell")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'SELL'


async def track_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Please Enter Your Wallet Address")
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')
    BOT_STATE[update.message.chat.id] = 'TRACK'


async def set_order(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Implement setting buy/sell orders logic here
    await update.message.reply_text("Setting buy/sell orders is not implemented yet.")


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    print(
        f'{update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: Update {update} caused error {context.error}')
    await update.message.reply_text(str(context.error))


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global BOT_STATE
    message_type: str = update.message.chat.type
    text: str = update.message.text

    text: str = update.message.text

    if BOT_STATE[update.message.chat.id] == 'TRACK':
        BOT_STATE[update.message.chat.id] = 'Default'
        print('TRACK WALLET')
        msg = update.message.text
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{msg}"')
        balance = solana_client.get_balance(msg)
        await update.message.reply_text(f"Balance of {msg}: {balance['result']['value']} lamports")
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    elif BOT_STATE[update.message.chat.id] == 'GET':
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}" ')
        BOT_STATE[update.message.chat.id] = 'Default'
        print('BUY TOKEN')
        msg = update.message.text
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{msg}"')

        balance = solana_client.get_balance(PublicKey(msg))
        await update.message.reply_text(f"Your Solana wallet balance: {lam_to_sol(balance['result']['value'])} sol")

        text2 = f"Your Solana wallet balance: {lam_to_sol(balance['result']['value'])} sol"
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text2}" ')

    elif BOT_STATE[update.message.chat.id] == 'BUY':
        BOT_STATE[update.message.chat.id] = 'Default'
        print('BUY TOKEN')
        msg = update.message.text
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{msg}"')

        target_wallet, amount_to_buy = msg.split(',')

        solana_token_transfer(target_wallet, OUR_ADDRESS, amount_to_buy)
        await update.message.reply_text(f"Bought {amount_to_buy} lamports of the token.")
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    elif BOT_STATE[update.message.chat.id] == 'SELL':
        BOT_STATE[update.message.chat.id] = 'Default'
        print('SELL TOKEN')
        msg = update.message.text
        print(f'User {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{msg}"')

        target_wallet, amount_to_sell = msg.split(',')

        solana_token_transfer(OUR_ADDRESS, target_wallet, amount_to_sell)

        await update.message.reply_text(f"Sold {amount_to_sell} lamports of the token.")
        print(f'Bot To {update.message.chat.first_name} {update.message.chat.last_name} ({update.message.chat.id}) in {message_type}: "{text}"')

    else:
        await update.message.reply_text(f"{message_type}: I don't understand that command. {text}")


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global app
    query = update.callback_query
    await query.answer()
    command = query.data
    # arg = BOT_STATE2[query.message.chat.id]
    await app.bot.send_message(chat_id=query.message.chat.id, text=command)

    # Handle all commands
    # if command == "/generate_wallet":
    # await query.edit_message_text(text=f"You pressed the button with the command {command}")
    # await app.bot.send_message(chat_id=query.message.chat.id, text=command)
    # await generate_wallet(arg[0], arg[1])
    #     try:
    #         await generate_wallet(update, context)
    #     except Exception as e:
    #         print('\n', str(e), '\n')
    # elif command == "/get_balance":
    #     # await query.edit_message_text(text=f"You pressed the button with the command {command}")
    #     await get_balance(update, context)
    # elif command == "/buy_token":
    #     # await query.edit_message_text(text=f"You pressed the button with the command {command}")
    #     await buy_token(update, context)
    # elif command == "/sell_token":
    #     # await query.edit_message_text(text=f"You pressed the button with the command {command}")
    #     await sell_token(update, context)
    # elif command == "/track_wallet":
    #     # await query.edit_message_text(text=f"You pressed the button with the command {command}")
    #     await track_wallet(update, context)
    # elif command == "/set_order":
    #     # await query.edit_message_text(text=f"You pressed the button with the command {command}")
    #     await set_order(update, context)


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
    print('STARTING BOT...')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(CommandHandler("generate_wallet", generate_wallet))
    app.add_handler(CommandHandler("get_balance", get_balance))
    app.add_handler(CommandHandler("buy_token", buy_token))
    app.add_handler(CommandHandler("sell_token", sell_token))
    app.add_handler(CommandHandler("track_wallet", track_wallet))
    app.add_handler(CommandHandler("set_order", set_order))

    # MESSAGES
    app.add_handler(MessageHandler(filters.ALL, handle_message))

    # ERRORS
    app.add_error_handler(error)
    app.add_handler(CallbackQueryHandler(button_callback))

    print('POLLING...')
    app.run_polling(poll_interval=1)
