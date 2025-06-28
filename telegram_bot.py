"""
Runs the search agent as a Telegram bot.
"""
import asyncio
import os
import logging

from dotenv import load_dotenv

from agents import Runner
from reagentic.interfaces import TelegramMessagingInterface, Message

from agent import create_search_agent

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from .env file
load_dotenv()

# Create the search agent
agent, _ = create_search_agent()
logging.info("🤖 Search agent created.")

async def message_handler(message: Message):
    """Handles incoming messages and uses the agent to respond."""
    logging.info(f"📬 Received message from {message.user_name} in chat {message.chat_id}: '{message.text}'")
    
    if not message.text or message.text.startswith('/'):
        # You can add command handling here, e.g., /start
        if message.text == '/start':
            await telegram_interface.send_message(
                message.chat_id, 
                "Hello! I am a web search assistant. Send me a query and I'll find information for you."
            )
        return

    max_retries = 3
    retry_delay_seconds = 2

    for attempt in range(max_retries):
        try:
            # Run the agent with the user's message
            logging.info(f"🧠 Processing message (Attempt {attempt + 1}/{max_retries})...")
            result = await Runner.run(agent, message.text)
            
            # Send the agent's response back to the user
            await telegram_interface.send_message(message.chat_id, result.final_output)
            logging.info(f"📩 Sent response to {message.chat_id}")
            return  # Exit after success

        except Exception as e:
            logging.warning(f"⚠️ Attempt {attempt + 1} of {max_retries} failed: {e}")
            if attempt < max_retries - 1:
                await asyncio.sleep(retry_delay_seconds)
            else:
                logging.error(f"❌ All {max_retries} attempts failed for chat {message.chat_id}.")
                await telegram_interface.send_message(
                    message.chat_id, 
                    "Sorry, I was unable to process your request after multiple attempts. Please try again later."
                )

async def main():
    """Initializes and runs the Telegram bot."""
    token = os.getenv("TELEGRAM_BOT_TOKEN", "YOUR_TELEGRAM_BOT_TOKEN")

    if token == "YOUR_TELEGRAM_BOT_TOKEN":
        logging.warning("⚠️ Telegram token not found. Please set the TELEGRAM_BOT_TOKEN environment variable.")
        return

    global telegram_interface
    telegram_interface = TelegramMessagingInterface(config={'token': token})
    telegram_interface.set_message_handler(message_handler)

    try:
        await telegram_interface.start()
        logging.info("🚀 Telegram bot is running. Press Ctrl+C to stop.")
        
        # Keep the bot running
        while True:
            await asyncio.sleep(3600)
            
    except Exception as e:
        logging.error(f"💥 Failed to start or run the bot: {e}")
    finally:
        if 'telegram_interface' in globals() and telegram_interface.is_running:
            await telegram_interface.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("👋 Bot stopped manually.") 