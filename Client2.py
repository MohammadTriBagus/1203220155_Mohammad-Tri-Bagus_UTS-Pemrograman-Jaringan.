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