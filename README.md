# Smart-Trash-Bin-With-YOLOv8
The automatic waste sorter is a prototype project created to automatically classify types of waste.

# Waste Detection dengan YOLO (Python)

Repositori ini berisi program **deteksi objek (sampah)** menggunakan model **YOLO** yang dijalankan secara real-time melalui **webcam**. Program dibuat dengan Python dan dijalankan melalui **Visual Studio Code**.

File utama:

* `main.py` → program utama deteksi
* `best.pt` → model YOLO hasil training

Kalau kamu berharap ini bisa langsung jalan tanpa setup, sayangnya dunia tidak seindah itu. Ikuti langkah di bawah.

---

## 1. Persiapan Awal

### 1.1 Instalasi Software Wajib

Pastikan sudah terpasang:

* **Python 3.9 – 3.11** (disarankan 3.10)
* **Visual Studio Code**
* **Git** (opsional, tapi masuk akal kalau ini repo GitHub)

Cek Python:

```bash
python --version
```

---

## 2. Clone Repository (Opsional)

Jika repo ini berasal dari GitHub:

```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
```

Atau buka folder project langsung di VS Code.

---

## 3. Membuat Virtual Environment

Tujuannya sederhana: supaya library tidak bikin konflik dengan hidupmu yang lain.

### 3.1 Buat Virtual Environment

```bash
python -m venv env
```

### 3.2 Aktifkan Virtual Environment

**Windows:**

```bash
env\Scripts\activate
```

**Linux / macOS:**

```bash
source env/bin/activate
```

Kalau terminal sudah ada `(env)` di depannya, berarti kamu berada di jalur yang benar.

---

## 4. Instalasi Library yang Dibutuhkan

Program ini membutuhkan library berikut:

* `ultralytics` (YOLO)
* `opencv-python`
* `torch` (akan ikut terpasang otomatis)

### 4.1 Instal Manual

```bash
pip install ultralytics opencv-python
```

Kalau pip protes, update dulu:

```bash
python -m pip install --upgrade pip
```

### 4.2 Cek Instalasi

```bash
python -c "import cv2; from ultralytics import YOLO; print('OK')"
```

Kalau tidak error, lanjut. Kalau error, ya berarti belum OK.

---

## 5. Struktur File Project

Pastikan struktur folder seperti ini:

```
project-folder/
│
├── main.py
├── best.pt
└── env/
```

Catatan penting:

* File `best.pt` **HARUS** satu folder dengan `main.py`
* Nama file model harus persis `best.pt`

---

## 6. Menjalankan Program

Jalankan perintah berikut di terminal VS Code:

```bash
python main.py
```

Jika kamera aktif dan jendela muncul dengan judul:

```
Waste Detection
```

berarti program berjalan dengan benar.

---

## 7. Cara Penggunaan Program

* Program akan otomatis mengakses **webcam default (index 0)**
* Objek terdeteksi akan diberi:

  * Bounding box hijau
  * Label kelas
  * Confidence dalam persen
* Objek dengan confidence < **0.5** akan diabaikan

### Kontrol:

* Tekan **ESC** untuk keluar dari program

---

## 8. Pengujian (Testing)

Langkah pengujian yang disarankan:

1. Pastikan kamera tidak dipakai aplikasi lain
2. Arahkan objek sesuai kelas yang ada di model
3. Perhatikan:

   * Apakah bounding box muncul
   * Apakah label sesuai
   * Apakah confidence masuk akal

Jika tidak ada deteksi:

* Model tidak mengenali objek
* Pencahayaan buruk
* Kamera resolusi rendah

Bukan bug, tapi batas realita.

---

## 9. Troubleshooting Umum

### Kamera Tidak Aktif

* Pastikan webcam terdeteksi OS
* Ubah index kamera: 1= eksternal kamera
                     0= internal kamera (camera laptop)

```python
cv2.VideoCapture(1)
```

### Model Tidak Ditemukan

Error:

```
FileNotFoundError: best.pt
```

Solusi:

* Pastikan file `best.pt` ada
* Nama file tidak typo

---

## 10. Catatan Tambahan

* Program ini **real-time**, performa tergantung spesifikasi laptop
* Tidak menggunakan GPU secara eksplisit
* Bisa dikembangkan ke video file atau IP Camera

---

## Author

MIPRDCTN

Kalau kamu sampai baca README ini sampai habis, itu sudah nilai plus tersendiri.
