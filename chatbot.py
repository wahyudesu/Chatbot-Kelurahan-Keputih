import os
from dotenv import load_dotenv
import requests
import telebot
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
HUGGINGFACE_API_URL = os.getenv('HUGGINGFACE_API_URL')

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def query(payload):
	response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
	return response.json()

def read_excel_to_dict(file_path):
  df = pd.read_excel(file_path)
  df = df.drop(columns=['No'])
  data_dict = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
  return data_dict

file_path = 'Data/Data Informasi.xlsx'
data = read_excel_to_dict(file_path)
sentences = list(data.keys())

# Command handler untuk memulai
@bot.message_handler(commands=['start', 'mulai'])
def send_welcome(message):
	bot.reply_to(message, "Selamat datang di chatbot keputih, ada yang bisa saya bantu?")

# Command handler untuk menghasilkan info
@bot.message_handler(commands=['info'])
def send_info(message):
	bot.reply_to(message, "Ini adalah telegram bot untuk kebutuhan kepengurusan dokumen kelurahan keputih.")

# Retrieval message
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    kalimat = message.text
    word_count = len(kalimat.split())
    # Logika untuk inputan yang hanya satu dan dua kata saja 
    if word_count < 2:
        bot.reply_to(message, "Terima kasih atas tanggapannya! Bisa tolong berikan sedikit lebih banyak informasi atau detail lagi.")
    # Logika untuk inputan yang kebanyakan kata
    if word_count > 10:
        bot.reply_to(message, "Mungkin kata-kata yang kamu berikan terlalu banyak, bisa diperingkas lagi")
    else:
        output = query({
            "inputs": {"source_sentence": kalimat, "sentences": sentences},
        })

        if isinstance(output, list) and len(output) > 0: #Threshold
            max_value = max(output)
            index = output.index(max_value)

            if index < len(sentences):
                jawaban = sentences[index]
                if jawaban in sentences:
                    result = data[jawaban]
                print("Jawaban:", result)
                bot.reply_to(message, result)
        
        # Logika jika permintaan kurang sesuai
        elif isinstance(output, list) and len(output) > 0 and 0.1 <= max(output) <= 0.5: #Threshold 0,1 hingga 0,5
            bot.reply_to(message, "Maaf, permintaan anda tidak ada di dalam database kami.")
        
        # Logika jika terjadi error
        else:
            bot.reply_to(message, "Maaf, saya tidak dapat memproses permintaan Anda.")

bot.polling()
