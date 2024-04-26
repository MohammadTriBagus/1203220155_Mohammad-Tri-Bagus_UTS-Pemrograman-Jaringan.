# UTS PEMROGRAMAN JARINGAN 

### Nama : Mohammad Tri Bagus
### Nim  : 1203220155

## Soal 

Buatlah sebuah permainan yang menggunakan soket dan protokol UDP. Permainannya cukup sederhana, dengan 1 server dapat melayani banyak klien (one-to- many). Setiap 10 detik, server akan mengirimkan kata warna acak dalam bahasa Inggris kepada semua klien yang terhubung. Setiap klien harus menerima kata yang berbeda (unik). Selanjutnya, klien memiliki waktu 5 detik untuk merespons dengan kata warna dalam bahasa Indonesia. Setelah itu, server akan memberikan nilai feedback 0 jika jawabannya salah dan 100 jika benar.

Syarat UTS:

- Kerjakan dengan menggunakan bahasa pemrograman python
- Menggunakan protokol UDP
- Code untuk server dan client dikumpulkan di github repository masing masing
- Pada readme.md silahkan beri penjelaskan how code works.
- Pada readme.md silahkan beri screenshoot cara penggunaaan serta contoh ketika program berjalan
- Test case: 1 server 10 client.
- Pastikan memahami soal
- Silahkan kumpulkan link github repository di assignment ini.
- JANGAN TELAT.

**1. Kodingan, Penjelasan, Cara Kerjanya dan Outputnya Untuk Server**

**A). Kodingann Servernya Sebagai Berikut :**

*Server.py*

```py
import socket
import random

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080
BUFFER_SIZE = 1024
COLORS = ["white", "gray", "gold", "red", "green", "blue", "yellow", "pink", "purple", "brown", "black"]

def generate_random_color():
    return random.choice(COLORS)

def handle_client_request(server_socket, client_address):
    color = generate_random_color()
    server_socket.sendto(color.encode("utf-8"), client_address)
    print(f"Sent color {color} to {client_address}")

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))

    print(f"Server running on {SERVER_IP}:{SERVER_PORT}")

    try:
        while True:
            data, client_address = server_socket.recvfrom(BUFFER_SIZE)
            data = data.decode("utf-8")

            if data == "request_color":
                handle_client_request(server_socket, client_address)

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan server UDP yang berjalan pada alamat IP dan port tertentu. Server ini memiliki daftar warna yang telah ditentukan dan dapat menghasilkan warna acak dari daftar tersebut. Ketika server menerima pesan "request_color" dari klien, ia memanggil fungsi handle_client_request. Fungsi ini menghasilkan warna acak, mengirimkannya kembali ke klien, dan mencetak warna yang dikirim dan alamat klien ke mana warna tersebut dikirim. Server kemudian masuk ke dalam loop tak terbatas di mana ia menunggu permintaan dari klien. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), server akan mencetak pesan bahwa server berhenti dan menutup soket. 

**C). Outputnya**
```
Server running on 127.0.0.1:8080
```

**2. Kodingan, Penjelasan dan Outputnya Untuk Client**

**2.1 Client 1**

**A). Kodingann Servernya Sebagai Berikut :**

*Client 1.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```
**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"  
Server running on 127.0.0.1:8080
Sent color black to ('127.0.0.1', 58607)
Sent color pink to ('127.0.0.1', 58607)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client1.py"
Color received: black
Masukkan Warna Dalam Bahasa Indonesian: hitam
Jawaban Benar. skor: 100
Color received: pink
Masukkan Warna Dalam Bahasa Indonesian: merah-muda
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"  
Server running on 127.0.0.1:8080
Sent color blue to ('127.0.0.1', 51657)
Sent color white to ('127.0.0.1', 51657)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client1.py"
Color received: blue
Masukkan Warna Dalam Bahasa Indonesian: Biruu
Jawaban Salah. skor: 0
Color received: white
Masukkan Warna Dalam Bahasa Indonesian: puttih
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.2 Client 2**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 2.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color gold to ('127.0.0.1', 65514)
Sent color blue to ('127.0.0.1', 65514)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client2.py"
Color received: gold
Masukkan Warna Dalam Bahasa Indonesian: emas
Jawaban Benar. skor: 100
Color received: blue
Masukkan Warna Dalam Bahasa Indonesian: biru
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color blue to ('127.0.0.1', 57053)
Sent color pink to ('127.0.0.1', 57053)
Sent color purple to ('127.0.0.1', 57053)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client2.py"
Color received: blue
Masukkan Warna Dalam Bahasa Indonesian: ungu
Jawaban Salah. skor: 0
Color received: pink
Masukkan Warna Dalam Bahasa Indonesian: merah
Jawaban Salah. skor: 0
Color received: purple
Masukkan Warna Dalam Bahasa Indonesian: unggu
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.


**2.3 Client 3**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 3.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color yellow to ('127.0.0.1', 56927)
Sent color green to ('127.0.0.1', 56927)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client3.py"
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: kuning
Jawaban Benar. skor: 100
Color received: green
Masukkan Warna Dalam Bahasa Indonesian: hijau
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color yellow to ('127.0.0.1', 49665)
Sent color green to ('127.0.0.1', 49665)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client3.py"
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: hijau
Jawaban Salah. skor: 0
Color received: green
Masukkan Warna Dalam Bahasa Indonesian: ungu 
Jawaban Salah. skor: 0

```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.4 Client 4**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 4.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color gold to ('127.0.0.1', 58467)
Sent color blue to ('127.0.0.1', 58467)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client4.py"
Color received: gold
Masukkan Warna Dalam Bahasa Indonesian: emas
Jawaban Benar. skor: 100
Color received: blue
Masukkan Warna Dalam Bahasa Indonesian: biru
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color pink to ('127.0.0.1', 54333)
Sent color yellow to ('127.0.0.1', 54333)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client4.py"
Color received: pink
Masukkan Warna Dalam Bahasa Indonesian: merah-maron
Jawaban Salah. skor: 0
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: emas
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.5 Client 5**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 5.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color yellow to ('127.0.0.1', 58684)
Sent color blue to ('127.0.0.1', 58684)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client5.py"
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: kuning
Jawaban Benar. skor: 100
Color received: blue
Masukkan Warna Dalam Bahasa Indonesian: biru
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color blue to ('127.0.0.1', 60459)
Sent color red to ('127.0.0.1', 60459)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client5.py"
Color received: blue
Masukkan Warna Dalam Bahasa Indonesian: birru
Jawaban Salah. skor: 0
Color received: red
Masukkan Warna Dalam Bahasa Indonesian: abu-abu
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.6 Client 6**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 6.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color yellow to ('127.0.0.1', 56085)
Sent color red to ('127.0.0.1', 56085)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client6.py"
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: kuning
Jawaban Benar. skor: 100
Color received: red
Masukkan Warna Dalam Bahasa Indonesian: merah
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color black to ('127.0.0.1', 61483)
Sent color gold to ('127.0.0.1', 61483)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client6.py"
Color received: black
Masukkan Warna Dalam Bahasa Indonesian: hiitam
Jawaban Salah. skor: 0
Color received: gold
Masukkan Warna Dalam Bahasa Indonesian: kuning
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.7 Client 7**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 7.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color purple to ('127.0.0.1', 50614)
Sent color brown to ('127.0.0.1', 50614)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client7.py"
Color received: purple
Masukkan Warna Dalam Bahasa Indonesian: ungu
Jawaban Benar. skor: 100
Color received: brown
Masukkan Warna Dalam Bahasa Indonesian: coklat
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color yellow to ('127.0.0.1', 58007)
Sent color gray to ('127.0.0.1', 58007)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client7.py"
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: kunning
Jawaban Salah. skor: 0
Color received: gray
Masukkan Warna Dalam Bahasa Indonesian: abu-muda 
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.8 Client 8**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 8.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color white to ('127.0.0.1', 57657)
Sent color green to ('127.0.0.1', 57657)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client8.py"
Color received: white
Masukkan Warna Dalam Bahasa Indonesian: putih
Jawaban Benar. skor: 100
Color received: green
Masukkan Warna Dalam Bahasa Indonesian: hijau
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color gray to ('127.0.0.1', 61061)
Sent color white to ('127.0.0.1', 61061)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client8.py"
Color received: gray
Masukkan Warna Dalam Bahasa Indonesian: abu tua
Jawaban Salah. skor: 0
Color received: white
Masukkan Warna Dalam Bahasa Indonesian: puutih
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.9 Client 9**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 9.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color gold to ('127.0.0.1', 58295)
Sent color brown to ('127.0.0.1', 58295)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client9.py"
Color received: gold
Masukkan Warna Dalam Bahasa Indonesian: emas
Jawaban Benar. skor: 100
Color received: brown
Masukkan Warna Dalam Bahasa Indonesian: coklat
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py"   
Server running on 127.0.0.1:8080
Sent color green to ('127.0.0.1', 52907)
Sent color purple to ('127.0.0.1', 52907)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client9.py"
Color received: green
Masukkan Warna Dalam Bahasa Indonesian: Hijauu
Jawaban Salah. skor: 0
Color received: purple
Masukkan Warna Dalam Bahasa Indonesian: merah-maron
Jawaban Salah. skor: 0
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2.10 Client 10**

**A). Kodingann Clientnya Sebagai Berikut :**

*Client 10.py*

```py
import socket
import time

def main():
    server_ip = "127.0.0.1"
    server_port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            client_socket.sendto("request_color".encode("utf-8"), (server_ip, server_port))

            color, _ = client_socket.recvfrom(1024)
            color = color.decode("utf-8")

            print(f"Color received: {color}")

            response = input("Masukkan Warna Dalam Bahasa Indonesian: ")

            indonesian_color = english_to_indonesian_color(color)
            if response.lower() == indonesian_color:
                print("Jawaban Benar. skor: 100")
            else:
                print("Jawaban Salah. skor: 0")

            time.sleep(10)

    except KeyboardInterrupt:
        print("\nClient berhenti.")

    finally:
        client_socket.close()
def english_to_indonesian_color(english_color):
    color_mapping = {
        "white" : "putih",
        "gray" : "abu-abu",
        "gold" : "emas",
        "red": "merah",
        "green": "hijau",
        "blue": "biru",
        "yellow": "kuning",
        "pink": "merah-muda",
        "purple": "ungu",
        "brown": "coklat",
        "black":"hitam",
    }
    return color_mapping.get(english_color.lower(), "Tidak Dapat Menemukan Warna yang Spesifik")

if __name__ == "__main__":
    main()
```

**B). Penjelasan**

Kode ini mendefinisikan klien UDP yang berkomunikasi dengan server untuk meminta warna dalam Bahasa Inggris dan kemudian meminta pengguna untuk menerjemahkannya ke dalam Bahasa Indonesia. Klien ini mengirim pesan "request_color" ke server dan menunggu respons. Setelah menerima warna dari server, klien mencetak warna tersebut dan meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia. Klien kemudian membandingkan jawaban pengguna dengan terjemahan yang benar menggunakan fungsi english_to_indonesian_color, yang mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”. Klien kemudian tidur selama 10 detik sebelum mengirim permintaan warna berikutnya ke server. Jika ada interupsi keyboard (biasanya ketika pengguna menekan Ctrl+C), klien akan mencetak pesan bahwa klien berhenti dan menutup soket. 

**C). Outputnya**
- Outputnya jika benar, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py" 
Server running on 127.0.0.1:8080
Sent color pink to ('127.0.0.1', 53121)
Sent color yellow to ('127.0.0.1', 53121)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client10.py"
Color received: pink
Masukkan Warna Dalam Bahasa Indonesian: merah-muda
Jawaban Benar. skor: 100
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: kuning
Jawaban Benar. skor: 100
```
  
- Outputnya jika salah, sebagai berikut :
```
PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Server.py" 
Server running on 127.0.0.1:8080
Sent color green to ('127.0.0.1', 62805)
Sent color yellow to ('127.0.0.1', 62805)

PS E:\Semester 4\Pemrograman jaringan\Tugas\Tubes UTS> & C:/Users/mohtr/anaconda3/envs/pcd/python.exe "e:/Semester 4/Pemrograman jaringan/Tugas/Tubes UTS/Client10.py"
Color received: green
Masukkan Warna Dalam Bahasa Indonesian: hijau
Jawaban Benar. skor: 100
Color received: yellow
Masukkan Warna Dalam Bahasa Indonesian: kuning
Jawaban Benar. skor: 100
```
Outputnya salah karena kata yang diinputkan tidak sesuai translate bahasa indonesia dengan kata yang dikirim oleh server dalam bahasa inggris dan juga penyebab lainnya yaitu karena ada kelebihan huruf saat menginputkan warna dalam bahasa indonesia.

**2. Cara Kerja Server Dan Clientnnya**

**1), Cara Kerja Server**
    -  **Inisialisasi dan Persiapan Server**:
   ```
   Tidak ada output pada tahap ini, karena hanya melakukan inisialisasi variabel dan fungsi.
   ```
**2)Fungsi `generate_random_color()`**:
   ```
   Tidak ada output pada tahap ini, karena fungsi `generate_random_color()` hanya mengembalikan warna acak dan tidak mencetak apapun.
   ```

**3). Fungsi `handle_client_request(server_socket, client_address)`**:
   ```
   Tidak ada output pada tahap ini, karena fungsi `handle_client_request()` hanya mencetak pesan saat dipanggil oleh server untuk menangani permintaan dari klien.
   ```

**4). Fungsi `main()`**:
   ```
   Server running on 127.0.0.1:8080
   ```

**5. Eksekusi Program**:
   ```
   Sent color pink to ('127.0.0.1.2', 5678)
   Sent color gray to ('127.0.0.1.3', 6789)
   Sent color red to ('127.0.0.1.4', 7890)
   ```
- Pada tahap 4, server berhasil dijalankan dan mencetak pesan bahwa server berjalan dan siap menerima permintaan dari klien di alamat IP 127.0.0.1 dan port 8080.
  ![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Server/1.png?raw=true)
  
- Pada tahap 5, server menerima permintaan dari tiga klien yang berbeda dan merespons dengan mengirimkan warna acak kepada masing-masing klien. Setiap kali server mengirim warna, ia mencetak pesan yang menunjukkan warna yang dikirim dan alamat klien yang menerima warna tersebut.
![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Server/server.png?raw=true)


**2). Cara Kerja Client 1-10**
- Klien juga dibuat menggunakan soket UDP.
- Klien masuk ke dalam loop tak terbatas di mana ia mengirim pesan "request_color" ke server dan menunggu respons.
- Setelah menerima warna dari server, klien mencetak warna tersebut.
  ![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Client/1.png?raw=true)
  
- Klien kemudian meminta pengguna untuk memasukkan terjemahan warna tersebut dalam Bahasa Indonesia.
  ![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Client/2.png?raw=true)

- Klien membandingkan jawaban pengguna dengan terjemahan yang benar. Jika jawaban pengguna benar, klien mencetak “Jawaban Benar. skor: 100”. Jika jawaban pengguna salah, klien mencetak “Jawaban Salah. skor: 0”.
  a) Ini untuk Jawaban Benar Seperti gambar dibawah ini :
     ![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Client/3.png?raw=true)
    
  b) Ini untk Jawaban Salah Seperti gambar dibawah ini
     ![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Client/4.1..png?raw=true)
  
- Klien kemudian berhenti selama 10 detik sebelum mengirim permintaan warna berikutnya ke server.
  ![alt text](https://github.com/MohammadTriBagus/1203220155_Mohammad-Tri-Bagus_UTS-Pemrograman-Jaringan./blob/main/assets/Gambar%20Client/4.png?raw=true)
  
Tambahan :
- Fungsi english_to_indonesian_color digunakan untuk mengubah warna dari Bahasa Inggris ke Bahasa Indonesia. Fungsi ini menggunakan kamus di mana kunci adalah warna dalam Bahasa Inggris dan nilai adalah terjemahan dalam Bahasa Indonesia. Fungsi ini mengembalikan terjemahan jika ditemukan, atau string "Tidak Dapat Menemukan Warna yang Spesifik" jika tidak.
