import os
import requests

# Fungsi untuk mengirim teks ke ChatGPT API
def chat_with_gpt(api_key, text):
    endpoint = "https://platform.openai.com/docs/api-reference"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    data = {
        "model": "text-davinci-003",
        "prompt": text,
        "max_tokens": 50
    }
    response = requests.post(endpoint, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return "Error communicating with ChatGPT API"

# Fungsi untuk menambahkan file audio
def add_audio_file(file_path):
    # Lakukan apa yang diperlukan untuk menambahkan file audio
    print(f"File audio '{file_path}' berhasil ditambahkan.")

# Fungsi utama
def main():
    # Masukkan API key ChatGPT Anda di sini
    api_key = "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"

    # Mulai loop untuk menerima input dari pengguna
    while True:
        # Minta input dari pengguna
        user_input = input("RonzDev-Ofc: ")

        # Keluar dari loop jika pengguna memasukkan "exit"
        if user_input.lower() == "exit":
            break

        # Kirim input ke ChatGPT API untuk mendapatkan respons
        response = chat_with_gpt(api_key, user_input)

        # Tampilkan respons dari ChatGPT
        print("ChatGPT:", response)

        # Cek apakah respons mengandung kata "tambahkan audio"
        if "tambahkan audio" in response:
            # Ambil path file audio dari respons
            audio_file_path = response.split("tambahkan audio")[1].strip()
            # Tambahkan file audio
            add_audio_file(audio_file_path)

if __name__ == "__main__":
    main()
