from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["toko_online"]
produk = db["produk"]

# Menghapus seluruh produk dalam kategori Aksesoris
hasil = produk.delete_many({"kategori": "Aksesoris"})
print("Total dokumen terhapus:", hasil.deleted_count)

# Menghapus produk dengan stok <= 0
hasil2 = produk.delete_many({"stok": {"$lte": 0}})
print("Total dokumen terhapus:", hasil2.deleted_count)