import socket
from des import des_decrypt_ecb

HOST = '127.0.0.1'  # localhost
PORT = 65432        # arbitrary port

key = input("Enter 8-character key for decryption: ").encode("utf-8")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on {HOST}:{PORT}...")

    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("\nEncrypted message (hex):", data.hex())
            try:
                decrypted = des_decrypt_ecb(data, key)
                print("Decrypted message:", decrypted.decode('utf-8', errors='ignore'))
            except Exception as e:
                print("Error decrypting:", e)