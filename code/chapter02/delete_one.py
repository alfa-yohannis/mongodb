from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Menghapus produk berdasarkan nama
hasil = produk.delete_one({"nama": "Mouse Wireless"})
print("Jumlah dokumen terhapus:", hasil.deleted_count)

# Menghapus sebuah produk dengan stok 0
hasil2 = produk.delete_one({"stok": 0})
print("Jumlah dokumen terhapus:", hasil2.deleted_count)