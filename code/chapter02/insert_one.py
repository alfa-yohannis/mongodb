from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

hasil = produk.insert_one({
    "nama": "Mouse Wireless",
    "harga": 250000,
    "kategori": "Aksesoris",
    "stok": 50
})

print("Dokumen berhasil ditambahkan dengan _id:", hasil.inserted_id)