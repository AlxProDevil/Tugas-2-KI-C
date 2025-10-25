import socket
from des import des_encrypt_ecb

HOST = '127.0.0.1'
PORT = 65432

key = input("Enter 8-character key for encryption: ").encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to server {HOST}:{PORT}")

    while True:
        message = input("\nEnter message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        plaintext = message.encode('utf-8')
        ciphertext = des_encrypt_ecb(plaintext, key)
        print("Encrypted message (hex):", ciphertext.hex())

        s.sendall(ciphertext)