from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Menampilkan hanya 'nama' dan 'harga'
cursor = produk.find(
    {"kategori": "Elektronik"},
    {"nama": 1, "harga": 1}
)

for p in cursor:
    print(p)

# Menyembunyikan _id
cursor = produk.find(
    {"kategori": "Elektronik"},
    {"_id": 0, "nama": 1, "harga": 1}
)

for p in cursor:
    print(p)