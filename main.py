#Importing Libraries
from telegram.ext import *
from io import BytesIO
import cv2
import numpy as np
import tensorflow as tf


#Token
with open('file.txt','r') as f:
    file = f.read()

TOKEN = file.split('\n')[2].split(':')[-2] + ':' + file.split('\n')[2].split(':')[-1]


#Custom Function
def start(update, context):
    update.message.reply_text("Hello! Welcome to Diptam's Bot")

def help(update, context):
    update.message.reply_text("""
    The following commands are available : 

    /start  -> Welcome message
    /help  -> To list out all the commands
    /train  -> To train the neural network
    """)


#-------------------------------------------------------Image Detection -----------------------------------------------


def handle_message(update, context):
    update.message.reply_text("Please train the model and send a picture")

def handle_photo(update, context):
    #Loading image
    photo = context.bot.get_file(update.message.photo[-1].file_id)
    photo.download('test.jpg')
    f = BytesIO(photo.download_as_bytearray())
    file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
    #Loading image done
    pass
    # img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # img = cv2.resize(img, (32,32), interpolation=cv2.INTER_AREA)

    # prediction = model.predict(np.array([img / 255]))
    # print(prediction)
    # update.message.reply_text(f"In this image I see a {class_names[np.argmax(prediction)]}")



#-------------------------------------------------------Face Recognize and mark attendance-----------------------------------------------
# Face Recognition  

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    disp = updater.dispatcher


    disp.add_handler(CommandHandler("start", start))
    disp.add_handler(CommandHandler("help", help))
    disp.add_handler(MessageHandler(Filters.text, handle_message))
    disp.add_handler(MessageHandler(Filters.photo, handle_photo))


    updater.start_polling()
    updater.idle()