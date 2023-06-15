import telebot

TOKEN = '6102789034:AAE7S9whz67Z6HOoq1iLXCE1PkrqSzqlnTw'
bot = telebot.TeleBot(TOKEN)

def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + 13) % 26 + 65)  # Encrypt using ROT13 for uppercase letters
            else:
                encrypted_char = chr((ord(char) - 97 + 13) % 26 + 97)  # Encrypt using ROT13 for lowercase letters
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt_message(message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - 13) % 26 + 65)  # Decrypt using ROT13 for uppercase letters
            else:
                decrypted_char = chr((ord(char) - 97 - 13) % 26 + 97)  # Decrypt using ROT13 for lowercase letters
        else:
            decrypted_char = char
        decrypted_message += decrypted_char
    return decrypted_message

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Welcome to the encryption/decryption bot!")
    bot.send_message(message.chat.id, "How to use this bot: /encrypt (your message) or /decrypt (your message)")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.startswith('/encrypt'):
        text_to_encrypt = message.text[9:]  # Extract the text to encrypt (remove '/encrypt ')
        encrypted_message = encrypt_message(text_to_encrypt)
        bot.send_message(message.chat.id, f"Encrypted message: {encrypted_message}")
    elif message.text.startswith('/decrypt'):
        text_to_decrypt = message.text[9:]  # Extract the text to decrypt (remove '/decrypt ')
        decrypted_message = decrypt_message(text_to_decrypt)
        bot.send_message(message.chat.id, f"Decrypted message: {decrypted_message}")
    else:
        bot.send_message(message.chat.id, "Invalid command. Please use /encrypt or /decrypt.")

bot.polling()
