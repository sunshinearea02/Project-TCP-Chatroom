# Multi-Client Chat Room Simulation using TCP Socket

Nama: Athaya Khairani Adi <br>
NRP: 5024241007 <br>
Mata Kuliah : Jaringan Komputer

---
Project ini adalah aplikasi simulasi ruang obrolan (*chat room*) berbasis teks yang memungkinkan komunikasi *multi-client* secara *real-time* melalui satu server perantara. Program ini dibangun menggunakan bahasa **Python** dengan memanfaatkan protokol **TCP (Transmission Control Protocol)** dan teknik **Multithreading**.

---

## Fitur Utama
* **Arsitektur Client-Server:** Server bertindak sebagai broker/perantara sentral yang mengelola koneksi.
* **Protokol Resmi TCP:** Menjamin pengiriman pesan yang aman, andal (*reliable*), dan berurutan tanpa risiko kehilangan data.
* **Mendukung Multi-Client (Multithreading):** Server dapat menangani banyak client sekaligus secara asinkronus tanpa memblokir koneksi satu sama lain.
* **Mekanisme Broadcast:** Setiap pesan yang dikirim oleh salah satu client akan disebarkan secara otomatis oleh server ke seluruh client lain yang sedang terhubung.
* **Handling Disconnect:** Server secara otomatis mendeteksi jika ada client yang keluar atau terputus secara paksa, lalu membersihkan resource socket-nya.

---

## Prasyarat (Prerequisites)
* Python sudah terinstal di komputer Anda.
* Menggunakan minimal 3 jendela terminal/command prompt (1 untuk Server, 2 atau lebih untuk Client).

---

## Cara Menjalankan Simulasi

Ikuti langkah-langkah berikut untuk menjalankan simulasi dengan 1 Server dan 3 Client di komputer lokal (*localhost*):

### Langkah 1: Jalankan Server
Buka terminal pertama, masuk ke direktori tempat file disimpan, lalu jalankan script server:
```bash
python chat_server.py
```
### Langkah 2: Jalankan Server
Buka terminal kedua, arahkan ke direktori yang sama, lalu jalankan script client:
```Bash
python chat_client.py
```
Masukkan nama Anda (misal: taya). Terminal server akan mencatat log: taya joined the chat. <br>
Lakukan hal yang sama pada terminal ketiga dan keempat.

### Langkah 4: Mulai Chatting
Ketik pesan di terminal taya dan tekan Enter. Pesan tersebut akan otomatis muncul di terminal client 2, client 3 dan log Server secara real-time.

---
## Penjelasan Konsep Jaringan

### 1. Alokasi IP Address
* **Sisi Server (`0.0.0.0`):** Mengizinkan server untuk *bind* (mengikat diri) ke semua *interface* jaringan yang tersedia di komputer (Localhost, Wi-Fi, Ethernet).
* **Sisi Client (`127.0.0.1`):** Menggunakan *Loopback Address* (Localhost) untuk mengarahkan *traffic* data kembali ke komputer itu sendiri, karena simulasi dijalankan pada satu perangkat yang sama.

### 2. Alur Data TCP (Connection-Oriented)
Sebelum bertukar data, *client* dan *server* melakukan proses *handshake* melalui fungsi `.connect()` dan `.accept()`. Pesan string dikonversi menjadi biner menggunakan fungsi `.encode()` sebelum dialirkan ke dalam pipa TCP, dan diubah kembali menjadi teks di sisi penerima menggunakan fungsi `.decode()`.

### 3. Mengapa Menggunakan Multithreading?
Fungsi penerimaan data `recv()` dan fungsi input ketikan `input()` bersifat ***blocking*** (menghentikan eksekusi kode hingga ada aksi).

* **Di Server:** *Threading* digunakan agar server bisa membuatkan jalur khusus untuk setiap *client* yang masuk, sehingga *client* baru tidak perlu mengantre atau terblokir oleh *client* lama.
* **Di Client:** *Threading* digunakan untuk memisahkan fungsi membaca pesan masuk dengan fungsi mengetik pesan, sehingga *client* bisa menerima *chat* kapan saja meskipun sedang mengetik.

---

## Struktur File Project

```text
├── chat_server.py    
├── chat_client.py    
└── README.md         

