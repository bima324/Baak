import os
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from datetime import datetime
import json

# Fungsi untuk mengambil kalender akademik
def get_akademik_calendar():
    KALENDER_URL = "http://baak.gunadarma.ac.id/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    # Cek apakah ada cache sebelumnya (file cache)
    if os.path.exists("akademik_cache.json"):
        with open("akademik_cache.json", "r") as file:
            cached_data = json.load(file)
        print("Menggunakan data cache...")
        return cached_data

    try:
        response = requests.get(KALENDER_URL, headers=headers, timeout=10)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            table = soup.find("tbody")

            if table:
                events = []
                rows = table.find_all("tr")
                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) > 1:
                        event = cols[0].text.strip()
                        date = cols[1].text.strip()
                        events.append({"event": event, "date": date})
                
                # Simpan data ke cache untuk penggunaan selanjutnya
                with open("akademik_cache.json", "w") as file:
                    json.dump(events, file)
                
                return events
            else:
                print("❌ Data akademik tidak dapat ditemukan.")
                return None
        else:
            print(f"❌ Gagal mengakses halaman BAAK. Status Code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Terjadi kesalahan saat mengakses server: {e}")
        return None

# Daftar mahasiswa yang pindah kelas
mahasiswa_pindah = [
    (1, "50423048", "ADINDA AULIA PUTRI", "1IA24", "2IA24"),
    (2, "50423055", "ADITYA PERMANA PUTRA", "1IA22", "2IA24"),
    (3, "50423075", "AGUSTINO WIJAYA HURSEPUNY", "1IA19", "2IA24"),
    (4, "50423079", "AHMAD DEEDAT DINATA", "1IA11", "2IA24"),
    (5, "50423091", "AHMAD YAZID ILMI", "1IA22", "2IA24"),
    (6, "50423102", "ALAN NABABAN", "1IA23", "2IA24"),
    (7, "50423122", "ALI MUKODASSAIT", "1IA21", "2IA24"),
    (8, "50423181", "ANGGA RIZKI NUGRAHA", "1IA21", "2IA24"),
    (9, "50423199", "ARDI LOWES FERNANDA", "1IA23", "2IA24"),
    (10, "50423210", "ARKAN ODESSAMAHENDRA", "1IA24", "2IA24"),
    (11, "50423237", "AXL REGAN YOHANDE", "1IA21", "2IA24"),
    (12, "50423276", "BIMA GUNAWAN", "1IA21", "2IA24"),
    (13, "50423423", "FADHIIL WIBYSONO", "1IA20", "2IA24"),
    (14, "50423463", "FARREL AKMAL AKHSANUDIN", "1IA20", "2IA24"),
    (15, "50423551", "HAFIZ SURYA NUGRAHA", "1IA22", "2IA24"),
    (16, "50423560", "HAIKAL RAFFIDIANSYAH", "1IA24", "2IA24"),
    (17, "50423620", "INDRA RAMADHAN", "1IA21", "2IA24"),
    (18, "50423647", "JAUZA PRASTA RAFADIO", "1IA23", "2IA24"),
    (19, "50423669", "JULIAN FADZLI", "1IA24", "2IA24"),
    (20, "50423678", "KATARINA SUSI WULANDARI", "1IA19", "2IA24"),
    (21, "50423714", "LUBENTIYO KRISDANI", "1IA20", "2IA24"),
    (22, "50423741", "MAHER SAHAB", "1IA21", "2IA24"),
    (23, "50423746", "MARCHEL IMANUEL PANGRURUK", "1IA23", "2IA24"),
    (24, "50423748", "MARIO CRISTIAN SIMATUPANG", "1IA22", "2IA24"),
    (25, "50423842", "MUHAMMAD ABDUL WAHID", "1IA23", "2IA24"),
    (26, "50423879", "MUHAMMAD DAFFA ALGHIFARI", "1IA20", "2IA24"),
    (27, "50423893", "MUHAMMAD FADHLAN IKHSANI", "1IA24", "2IA24"),
    (28, "50423908", "MUHAMMAD FATIH MAULANA", "1IA21", "2IA24"),
    (29, "50423925", "MUHAMMAD HAEKAL", "1IA23", "2IA24"),
    (30, "50423930", "MUHAMMAD HARY PRASETIYO", "1IA23", "2IA24"),
    (31, "51423050", "MYCHELE G PONAMON", "1IA19", "2IA24"),
    (32, "51423081", "NAUFAL HAFIZH AHNAF", "1IA20", "2IA24"),
    (33, "51423097", "NAZWA AMANDA SYIFA", "1IA23", "2IA24"),
    (34, "51423176", "RAFAEL RAMDANI", "1IA20", "2IA24"),
    (35, "51423218", "RAKA PRATAMA PUTRA SODIQ", "1IA24", "2IA24"),
    (36, "51423268", "RENDI PRANOTO", "1IA22", "2IA24"),
    (37, "51423316", "RIVAN ARDI NUGROHO", "1IA23", "2IA24"),
    (38, "51423454", "VIQRI RAMADHAN WALUYA", "1IA21", "2IA24"),
    (39, "51423505", "ZIDAN PUTRA WIKANDANA", "1IA22", "2IA24"),
]

# Daftar Kuliah
daftar_kuliah = [
    ("2IA24", "Rabu", "Matematika Informatika 4 *", "1/2/3", "J1216B", "SRAVA CHRISDES ANTORO"),
    ("2IA24", "Rabu", "Pemrograman Berorientasi Objek **", "5/6/7", "J1216B", "INDAH TRI HANDAYANI"),
    ("2IA24", "Rabu", "Statistika 2 **", "8/9/10", "J1216B", "INTI MULYO ARTI"),
    ("2IA24", "Kamis", "Sistem Operasi */**", "1/2/3", "J1116", "NATALLIOS PETER SIPASULTA"),
    ("2IA24", "Kamis", "Sistem Berkas *", "5/6", "J1116", "YENI SETIANI"),
    ("2IA24", "Kamis", "Matematika Lanjut 2", "8/9/10", "J1216A", "NURMA NUGRAHA"),
    ("2IA24", "Sabtu", "Arsitektur Komputer *", "1/2", "J1211", "NELLY SOFI"),
    ("2IA24", "Sabtu", "Bisnis Informatika", "3/4", "J1211", "ADAM HUDA NUGRAHA"),
    ("2IA24", "Sabtu", "Riset Operasional", "5/6", "J1211", "DESTI DIRNAENI"),
]

# Fungsi untuk menampilkan daftar kuliah dalam tabel
def display_course_schedule():
    course_table = PrettyTable()
    course_table.field_names = ["KELAS", "HARI", "MATA KULIAH", "WAKTU", "RUANG", "DOSEN"]
    course_table.align["MATA KULIAH"] = "l"  # Menyesuaikan kolom Mata Kuliah
    course_table.align["DOSEN"] = "l"
    course_table.max_width["MATA KULIAH"] = 40
    course_table.max_width["DOSEN"] = 30

    for kuliah in daftar_kuliah:
        course_table.add_row([kuliah[0], kuliah[1], kuliah[2], kuliah[3], kuliah[4], kuliah[5]])

    print("\n✨ Daftar Jadwal Kuliah 2IA24:")
    print(course_table)

# Fungsi untuk menampilkan data mahasiswa dalam tabel
def display_student_data():
    student_table = PrettyTable()
    student_table.field_names = ["No", "NPM", "Nama", "Kelas Lama", "Kelas Baru"]
    student_table.align["Nama"] = "l"  # Menyesuaikan kolom Nama
    student_table.align["Kelas Lama"] = "l"
    student_table.align["Kelas Baru"] = "l"
    student_table.max_width["Nama"] = 40

    for mahasiswa in mahasiswa_pindah:
        student_table.add_row([mahasiswa[0], mahasiswa[1], mahasiswa[2], mahasiswa[3], mahasiswa[4]])

    print("\n✨ Data Mahasiswa yang Pindah Kelas:")
    print(student_table)

# Fungsi untuk menandai event yang sesuai dengan tanggal saat ini
def mark_current_date(events, current_date):
    for event in events:
        if event["date"]:
            try:
                event_date = None
                date_formats = ["%d %B %Y", "%d-%m-%Y", "%Y-%m-%d"]
                for date_format in date_formats:
                    try:
                        event_date = datetime.strptime(event["date"], date_format).date()
                        break
                    except ValueError:
                        continue
                if event_date and event_date == current_date:
                    event["date"] = f"📍 {event['date']}"
            except Exception as e:
                print(f"Error while marking current date: {e}")
    return events

# Fungsi untuk menampilkan kalender akademik
def display_academic_calendar(events):
    if events:
        today = datetime.today().date()
        events = mark_current_date(events, today)

        academic_calendar_table = PrettyTable()
        academic_calendar_table.field_names = ["Event", "Date"]
        academic_calendar_table.align["Event"] = "l"  # Rata kiri untuk kolom Event
        academic_calendar_table.align["Date"] = "r"  # Rata kanan untuk kolom Date
        academic_calendar_table.max_width["Event"] = 40  # Menyesuaikan lebar kolom Event
        academic_calendar_table.max_width["Date"] = 20   # Menyesuaikan lebar kolom Date

        for event in events:
            academic_calendar_table.add_row([event["event"], event["date"]])

        print("\n✨ Kalender Akademik:")
        print(academic_calendar_table)

        # Menampilkan ukuran tabel (jumlah baris)
        print(f"\nJumlah event dalam kalender akademik: {len(events)}")

# Menu utama
def main_menu():
    while True:
        print("\nPilih opsi:")
        print("1. Tampilkan Jadwal Kalender Akademik")
        print("2. Tampilkan Daftar Mahasiswa yang Pindah Kelas")
        print("3. Tampilkan Daftar Jadwal Kuliah")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == '1':
            calendar_data = get_akademik_calendar()
            display_academic_calendar(calendar_data)
        elif pilihan == '2':
            display_student_data()
        elif pilihan == '3':
            display_course_schedule()
        elif pilihan == '4':
            print("Selamat tinggal! Sampai jumpa.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan menu utama
if __name__ == "__main__":
    main_menu()
