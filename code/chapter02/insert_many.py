from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

hasil = produk.insert_many([
    { "nama": "USB Hub 4 Port", "harga": 120000, "stok": 40 },
    { "nama": "Webcam HD", "harga": 450000, "stok": 15 },
    { "nama": "Portable SSD 1TB", "harga": 1450000, "stok": 10 }
])

print("ID dokumen yang ditambahkan:")
for _id in hasil.inserted_ids:
    print("-", _id)