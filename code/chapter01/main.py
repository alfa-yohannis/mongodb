from pymongo import MongoClient

# Membuat koneksi ke server MongoDB di localhost
client = MongoClient("mongodb://localhost:27017/")

# Memilih database
db = client["toko_online"]

# Memilih koleksi
produk = db["produk"]

# Menambahkan dokumen
insert_result = produk.insert_one({
    "nama": "Keyboard Mechanical",
    "harga": 750000,
    "stok": 20
})

print("ID dokumen yang ditambahkan:", insert_result.inserted_id)

# Membaca dokumen yang baru saja ditambahkan
hasil = produk.find_one({ "nama": "Keyboard Mechanical" })
print("Dokumen ditemukan:", hasil)