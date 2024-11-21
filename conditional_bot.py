from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Ganti dengan token bot Telegram Anda
TOKEN = "YOUR_BOT_TOKEN"

# Fungsi untuk memulai percakapan
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "🔹 *Silahkan Memilih kategori dokumen yang ingin anda cari:* 🔹\n"
        "1. 🧑‍🤝‍🧑 Dokumen Kependudukan\n"
        "2. 👶 Dokumen Kelahiran\n"
        "3. 💍 Dokumen Pernikahan\n"
        "4. ⚰️ Dokumen Kematian\n"
        "5. 📑 Lainnya"
    )

# Fungsi untuk menangani pilihan kategori dokumen
def handle_message(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text

    # Menangani pilihan kategori dokumen
    if user_input == "1":
        update.message.reply_text(
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Kependudukan:* 🔹\n"
            "1. 📝 Pemutahiran Biodata\n"
            "2. 📄 Pecah Kartu Keluarga\n"
            "3. 🆘 Cetak Kartu Keluarga Karena Hilang\n"
            "4. 🏠 Pelayanan Pindah Datang\n"
            "5. 🏡 Pemutahiran Biodata Keluarga"
        )
        # Simpan status pemilihan kategori
        context.user_data['category'] = 'Kependudukan'

    elif user_input == "2":
        update.message.reply_text(
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Kelahiran:* 🔹\n"
            "1. 📝 Permohonan Akta Kelahiran\n"
            "2. 👶 Akta Kelahiran Bayi Baru Lahir\n"
            "3. 📄 Akta Hilang atau Rusak\n"
            "4. ✍️ Perubahan Nama Akta Kelahiran\n"
            "5. 📑 Salinan Akta Kelahiran"
        )
        context.user_data['category'] = 'Kelahiran'

    elif user_input == "3":
        update.message.reply_text(
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Pernikahan:* 🔹\n"
            "1. 💍 Surat Pengantar Nikah\n"
            "2. 💌 Surat Pernyataan Belum Pernah Menikah\n"
            "3. 📝 Permohonan Akta Perkawinan\n"
            "4. 🌏 Pelaporan Peristiwa Perkawinan di Luar Negeri"
        )
        context.user_data['category'] = 'Pernikahan'

    elif user_input == "4":
        update.message.reply_text(
            "🔹 *Silahkan Pilih Layanan untuk Dokumen Kematian:* 🔹\n"
            "1. 📝 Permohonan Akta Kematian\n"
            "2. ⚰️ Akta Kematian Baru\n"
            "3. 📄 Akta Kematian Hilang atau Rusak\n"
            "4. 🧑‍⚖️ Surat Keterangan Ahli Waris"
        )
        context.user_data['category'] = 'Kematian'

    elif user_input == "5":
        update.message.reply_text("💬 *Silakan ketik pertanyaan Anda:*")
        context.user_data['category'] = 'Lainnya'

    else:
        update.message.reply_text("❌ *Pilihan tidak valid. Harap pilih angka 1-5.*")

# Fungsi untuk menangani layanan setelah kategori dipilih
def handle_service(update: Update, context: CallbackContext) -> None:
    category = context.user_data.get('category', None)

    if not category:
        update.message.reply_text("❌ *Harap pilih kategori dokumen terlebih dahulu.*")
        return

    user_input = update.message.text

    # Menangani layanan berdasarkan kategori yang dipilih
    if category == 'Kependudukan':
        if user_input == "1":
            update.message.reply_text("📄 *Kategori:* Dokumen Kependudukan - Pemutahiran Biodata")
        elif user_input == "2":
            update.message.reply_text("📄 *Kategori:* Dokumen Kependudukan - Pecah Kartu Keluarga")
        elif user_input == "3":
            update.message.reply_text("📄 *Kategori:* Dokumen Kependudukan - Cetak Kartu Keluarga Karena Hilang")
        elif user_input == "4":
            update.message.reply_text("📄 *Kategori:* Dokumen Kependudukan - Pelayanan Pindah Datang")
        elif user_input == "5":
            update.message.reply_text("📄 *Kategori:* Dokumen Kependudukan - Pemutahiran Biodata Keluarga")
        else:
            update.message.reply_text("❌ *Layanan tidak valid.*")

    elif category == 'Kelahiran':
        if user_input == "1":
            update.message.reply_text("📄 *Kategori:* Dokumen Kelahiran - Permohonan Akta Kelahiran")
        elif user_input == "2":
            update.message.reply_text("📄 *Kategori:* Dokumen Kelahiran - Akta Kelahiran Bayi Baru Lahir")
        elif user_input == "3":
            update.message.reply_text("📄 *Kategori:* Dokumen Kelahiran - Akta Hilang atau Rusak")
        elif user_input == "4":
            update.message.reply_text("📄 *Kategori:* Dokumen Kelahiran - Perubahan Nama Akta Kelahiran")
        elif user_input == "5":
            update.message.reply_text("📄 *Kategori:* Dokumen Kelahiran - Salinan Akta Kelahiran")
        else:
            update.message.reply_text("❌ *Layanan tidak valid.*")

    elif category == 'Pernikahan':
        if user_input == "1":
            update.message.reply_text("📄 *Kategori:* Dokumen Pernikahan - Surat Pengantar Nikah")
        elif user_input == "2":
            update.message.reply_text("📄 *Kategori:* Dokumen Pernikahan - Surat Pernyataan Belum Pernah Menikah")
        elif user_input == "3":
            update.message.reply_text("📄 *Kategori:* Dokumen Pernikahan - Permohonan Akta Perkawinan")
        elif user_input == "4":
            update.message.reply_text("📄 *Kategori:* Dokumen Pernikahan - Pelaporan Peristiwa Perkawinan di Luar Negeri")
        else:
            update.message.reply_text("❌ *Layanan tidak valid.*")

    elif category == 'Kematian':
        if user_input == "1":
            update.message.reply_text("📄 *Kategori:* Dokumen Kematian - Permohonan Akta Kematian")
        elif user_input == "2":
            update.message.reply_text("📄 *Kategori:* Dokumen Kematian - Akta Kematian Baru")
        elif user_input == "3":
            update.message.reply_text("📄 *Kategori:* Dokumen Kematian - Akta Kematian Hilang atau Rusak")
        elif user_input == "4":
            update.message.reply_text("📄 *Kategori:* Dokumen Kematian - Surat Keterangan Ahli Waris")
        else:
            update.message.reply_text("❌ *Layanan tidak valid.*")

    elif category == 'Lainnya':
        update.message.reply_text("💬 *Silakan ketik pertanyaan Anda:*")

    else:
        update.message.reply_text("❌ *Kategori tidak ditemukan.*")

# Fungsi utama untuk menjalankan bot
def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Menambahkan handler untuk perintah start
    dispatcher.add_handler(CommandHandler("start", start))

    # Menambahkan handler untuk pesan teks
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Menambahkan handler untuk menangani layanan berdasarkan kategori
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_service))

    # Memulai bot
    updater.start_polling()

    # Menjaga agar bot tetap berjalan
    updater.idle()

if __name__ == '__main__':
    main()
