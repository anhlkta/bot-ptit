# pip install python-telegram-bot = 13.7
# pip install schedule
# pip install requests
# pip install beautifulsoup4
from telegram.ext import *
import News
import constants as keys
import time
import schedule
import requests
print('Starting up bot...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


# Lets us use the /custom command
def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')

def news_command(update, context):
    news = News.Getdata()
    if news == []:
        update.message.reply_text('Không có tin mới nào cả :<')
    else:
        for x in range(0, len(news)):
            message = news[x]
            update.message.reply_text(message[0] + "\n" 
                + message[1] + "\n" + 'from Hung dep trai')
        


def handle_response(text) -> str:
    if 'hello' in text:
        return 'Hey!'
    if 'how are you' in text:
        return 'I\'m good!'
    if 'news' in text:
        return 'news'
    return 'I don\'t understand'


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@toiyeuptit_bot' in text:
            new_text = text.replace('@toiyeuptit_bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')



class scheduleprint():

    def printprogress(self):
        print("Start of Processing")
        print("Processing Complete")

    def schedule_a_print_job(self, type="Secs", interval=5):

        if type == "Secs": # Fed from the function paramaters
            schedule.every(interval).seconds.do(self.printprogress())
            # Including the parentheses after printprogess will throw an error as you cant run that method directly from there you can only call it.

        if type == "Mins": # Fed from the function paramaters
            schedule.every(interval).minutes.do(self.printprogress)
            # Including the parentheses  after printprogess will throw an error as you cant run that method directly from there you can only call it.

        while True:
            schedule.run_pending()
            time.sleep(1) # The number of seconds the Python program should pause execution.



def Auto_send_message():
    Datas = News.Getdata()
    if Datas == []:
        print("Không có tin mới nào cả :<")
    else:
        for data in Datas:
            message = "Có tin mới: " + data[1] + "\n" + data[0] + "\n" + 'from Hung dep trai'
            send_message("-1001797670157", str(message))


def send_message(chat_id, text):
    # text = "hello"
    # chat_id = "939184869"
    token = keys.API_KEY
    url = "https://api.telegram.org/bot" + token + "/sendmessage" + "?chat_id=" + str(chat_id) + "&text=" + text
    results = requests.get(url)
    print(results.json())

def test():
    data = News.Getdata()
    print(str(data))
# Run the program
if __name__ == '__main__':
    # updater = Updater(keys.API_KEY, use_context=True)
    # dp = updater.dispatcher
    # for i in range(0, 10):
    #     send_message(939184869, "Hello")
    # # Commands
    # dp.add_handler(CommandHandler('start', start_command))
    # dp.add_handler(CommandHandler('help', help_command))
    # dp.add_handler(CommandHandler('custom', custom_command))
    # dp.add_handler(CommandHandler("news", news_command))
    
    # # Messages
    # dp.add_handler(MessageHandler(Filters.text, handle_message))

    # # Log all errors
    # dp.add_error_handler(error)

    # # Run the bot
    # updater.start_polling(1.0)
    # updater.idle()

    # # send message 
    schedule.every(10).seconds.do(Auto_send_message) # Thực hiện hàm send_message mỗi 10 giây
    while True:
        schedule.run_pending()
        time.sleep(1)
