import os

def setup_api_key(api_key):
    home_dir = os.path.expanduser("~")
    gpt_dir = os.path.join(home_dir, ".gpt")
    
    # Membuat direktori .gpt jika belum ada
    if not os.path.exists(gpt_dir):
        os.makedirs(gpt_dir)
    
    # Menyimpan API key ke dalam file
    api_key_file = os.path.join(gpt_dir, "api_key.txt")
    with open(api_key_file, "w") as f:
        f.write(api_key)
    print("API key berhasil disimpan.")

if __name__ == "__main__":
    api_key = input("Masukkan API key ChatGPT Anda: ")
    setup_api_key(api_key)
