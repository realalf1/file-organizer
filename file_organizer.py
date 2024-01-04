import os
import shutil

def rapih(src, dst):
    # perintah untuk mendapatkan semua files termasuk direktori di simpan di <files>
    files = os.listdir(src)

    # ambil setiap file termasuk direktori
    for file in files:
        path = os.path.join(src, file) # jalur file & direktori

        # perkondisian jika terdeteksi file atau bukan direktori
        if os.path.isfile(path): 
            name, ext = os.path.splitext(path)      # (nama file, ekstensi file) (tuple)
            file_path = f"{dst}/{ext[1:]}"          # jalur direktori file per ekstensi
          
            os.makedirs(file_path, exist_ok= True)  # perintah untuk membuat direktori + jika sudah ada
            
            final_file_path = f"{file_path}/{file}" # jalur file terakhir disimpan

            shutil.move(path, final_file_path)      # perintah pindahin file berantakan
            
        else: # kondisi jika bukan file / adalah direktori
            print(f"Bukan file --> {path}")

if __name__ == "__main__":
    src = "C:/Users/Administrator/Downloads"
    dst = f"{src}/rapih"

    rapih(src, dst)
