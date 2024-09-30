import requests
import telebot
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

API_TOKEN = "7804271051:AAGGTqTy2ApgIb7zqdCnCFjATCyRFEkB0LQ"
API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

headers = {"Authorization": "Bearer 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"}
bot = telebot.TeleBot(API_TOKEN)

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

def read_excel_to_dict(file_path):
  df = pd.read_excel(file_path)
  df = df.drop(columns=['No'])
  data_dict = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
  return data_dict

file_path = 'Data/Data Informasi.xlsx'
data = read_excel_to_dict(file_path)
sentences = list(data.keys())

# Define a command handler
@bot.message_handler(commands=['start', 'mulai'])
def send_welcome(message):
	bot.reply_to(message, "Selamat datang di chatbot keputih, ada yang bisa saya bantu?")

# @bot.message_handler(commands=['info'])
# def send_info(message):
# 	bot.reply_to(message, "Ini adalah telegram bot untuk kebutuhan kepengurusan dokumen kelurahan keputih.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    kalimat = message.text
    output = query({
        "inputs": {"source_sentence": kalimat, "sentences": sentences},
    })

    if isinstance(output, list) and len(output) > 0:
        max_value = max(output)
        index = output.index(max_value)

        if index < len(sentences):
            jawaban = sentences[index]
            if jawaban in sentences:
                result = data[jawaban]
            print("Jawaban:", result)
            bot.reply_to(message, result)
    else:
        bot.reply_to(message, "Maaf, saya tidak dapat memproses permintaan Anda.")

bot.polling()