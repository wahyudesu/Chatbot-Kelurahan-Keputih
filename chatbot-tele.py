# library
import os
from dotenv import load_dotenv
import requests
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

load_dotenv()

# Load os
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
HUGGINGFACE_API_TOKEN = os.getenv('HUGGINGFACE_API_TOKEN')
HUGGINGFACE_API_URL = os.getenv('HUGGINGFACE_API_URL')

headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def query(payload):
    response = requests.post(HUGGINGFACE_API_URL, headers=headers, json=payload)
    return response.json()

# Read data
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

# Menampilkan menu
@bot.message_handler(func=lambda message: message.text.lower() == 'menu')
def send_menu(message):
    # Membuat custom keyboard
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = KeyboardButton("🧑‍🤝‍🧑 Dokumen Kependudukan")
    btn2 = KeyboardButton("👶 Dokumen Kelahiran")
    btn3 = KeyboardButton("💍 Dokumen Pernikahan")
    btn4 = KeyboardButton("⚰️ Dokumen Kematian")
    btn5 = KeyboardButton("📑 Lainnya")
    markup.add(btn1, btn2, btn3, btn4, btn5)

    bot.reply_to(
        message,
        "🔹 *Silahkan Memilih kategori dokumen yang ingin Anda cari:* 🔹",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# Fungsi untuk menangani pilihan kategori
@bot.message_handler(func=lambda message: message.text in [
    "🧑‍🤝‍🧑 Dokumen Kependudukan",
    "👶 Dokumen Kelahiran",
    "💍 Dokumen Pernikahan",
    "⚰️ Dokumen Kematian",
    "📑 Lainnya",
])
def handle_category(message):
    category = message.text
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    if category == "🧑‍🤝‍🧑 Dokumen Kependudukan":
        menu_text = (
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Kependudukan:* 🔹"
        )
        btn1 = KeyboardButton("📝 Pemutahiran Biodata")
        btn2 = KeyboardButton("📄 Pecah Kartu Keluarga")
        btn3 = KeyboardButton("🆘 Cetak Kartu Keluarga Karena Hilang")
        btn4 = KeyboardButton("🏠 Pelayanan Pindah Datang")
        btn5 = KeyboardButton("🏡 Pemutahiran Biodata Keluarga")
        markup.add(btn1, btn2, btn3, btn4, btn5)
    
    elif category == "👶 Dokumen Kelahiran":
        menu_text = (
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Kelahiran:* 🔹"
        )
        btn1 = KeyboardButton("📝 Permohonan Akta Kelahiran")
        btn2 = KeyboardButton("👶 Akta Kelahiran Bayi Baru Lahir")
        btn3 = KeyboardButton("📄 Akta Hilang atau Rusak")
        btn4 = KeyboardButton("✍️ Perubahan Nama Akta Kelahiran")
        btn5 = KeyboardButton("📑 Salinan Akta Kelahiran")
        markup.add(btn1, btn2, btn3, btn4, btn5)
    
    elif category == "💍 Dokumen Pernikahan":
        menu_text = (
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Pernikahan:* 🔹"
        )
        btn1 = KeyboardButton("💍 Surat Pengantar Nikah")
        btn2 = KeyboardButton("💌 Surat Pernyataan Belum Pernah Menikah")
        btn3 = KeyboardButton("📝 Permohonan Akta Perkawinan")
        btn4 = KeyboardButton("🌏 Pelaporan Peristiwa Perkawinan di Luar Negeri")
        markup.add(btn1, btn2, btn3, btn4)
    
    elif category == "⚰️ Dokumen Kematian":
        menu_text = (
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Kematian:* 🔹"
        )
        btn1 = KeyboardButton("📝 Permohonan Akta Kematian")
        btn2 = KeyboardButton("⚰️ Akta Kematian Baru")
        btn3 = KeyboardButton("📄 Akta Kematian Hilang atau Rusak")
        btn4 = KeyboardButton("🧑‍⚖️ Surat Keterangan Ahli Waris")
        markup.add(btn1, btn2, btn3, btn4)
    
    elif category == "📑 Lainnya":
        menu_text = "💬 *Silakan ketik pertanyaan Anda:*"
        markup = None  # Tidak memerlukan tombol untuk kategori ini
    
    else:
        menu_text = "❌ *Pilihan tidak valid.*"
        markup = None  # Tidak memerlukan tombol untuk kategori ini
    
    bot.reply_to(message, menu_text, reply_markup=markup, parse_mode="Markdown")

# Retrieval message
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    kalimat = message.text
    word_count = len(kalimat.split())
    # Logika untuk inputan yang hanya satu dan dua kata saja 
    if word_count < 2:
        bot.reply_to(message, "Terima kasih atas tanggapannya! Bisa tolong berikan sedikit lebih banyak informasi atau detail lagi.")
    # Logika untuk inputan yang kebanyakan kata
    elif word_count > 10:
        bot.reply_to(message, "Mungkin kata-kata yang kamu berikan terlalu banyak, bisa diperingkas lagi.")
    else:
        output = query({
            "inputs": {"source_sentence": kalimat, "sentences": sentences},
        })

        if isinstance(output, list) and len(output) > 0:  # Threshold
            max_value = max(output)
            index = output.index(max_value)

            if index < len(sentences):
                jawaban = sentences[index]
                if jawaban in sentences:
                    result = data[jawaban]
                print("Jawaban:", result)
                bot.reply_to(message, result)

        # Logika jika permintaan kurang sesuai
        elif isinstance(output, list) and len(output) > 0 and 0.1 <= max(output) <= 0.5:  # Threshold 0,1 hingga 0,5
            bot.reply_to(message, "Maaf, permintaan anda tidak ada di dalam database kami.")

        # Logika jika terjadi error
        else:
            bot.reply_to(message, "Maaf, saya tidak dapat memproses permintaan Anda.")

bot.polling()
