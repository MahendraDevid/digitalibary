# context_processors.py

from kategoribuku.views import total_data_kategori
from buku.views import total_data_buku
from koleksipribadi.views import total_data_koleksi, total_koleksi_per_user
from peminjaman.views import total_data_peminjaman, total_peminjaman_per_user
from ulasanbuku.views import total_data_ulasan, total_ulasan_per_user
from user.views import total_data_user

def total_semua_data(request):
    total_kategori = total_data_kategori(request)
    total_buku = total_data_buku(request)
    total_koleksi = total_data_koleksi()
    total_koleksi_peminjam = total_koleksi_per_user(request)
    total_peminjaman_admin = total_data_peminjaman()
    total_peminjaman = total_peminjaman_per_user(request)
    total_ulasan = total_data_ulasan()
    total_ulasan_peminjam = total_ulasan_per_user(request)
    total_user = total_data_user()
    
    return {
        'total_kategori': total_kategori,
        'total_buku': total_buku,
        'total_koleksi': total_koleksi,
        'total_koleksi_peminjam': total_koleksi_peminjam,
        'total_peminjaman_admin': total_peminjaman_admin,
        'total_peminjaman': total_peminjaman,
        'total_ulasan': total_ulasan,
        'total_ulasan_peminjam': total_ulasan_peminjam,
        'total_user': total_user
    }
