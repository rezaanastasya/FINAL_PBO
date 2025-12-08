# Final Pemrograman Berorientasi Objek (PBO) - Contoh Implementasi OOP Unik

Repositori ini berisi dua contoh implementasi **Pemrograman Berorientasi Objek (PBO)** dalam bahasa Python. Setiap contoh dirancang secara unik untuk mendemonstrasikan lima konsep dasar PBO: **Kelas**, **Objek**, **Enkapsulasi**, **Inheritance**, dan **Polimorfisme** dengan tema yang berbeda.

## Struktur Proyek

| File | Tema | Deskripsi Singkat |
| :--- | :--- | :--- |
| `workshop_oop_v2.py` | Bengkel Cowok | Implementasi PBO dengan fokus pada sistem diagnostik dan biaya servis kendaraan, menggunakan **Kelas Abstrak** dan **Inheritance Multi-level**. |
| `cosmetics_oop_v2.py` | Penjualan Kosmetik Cewek | Implementasi PBO dengan fokus pada sistem transaksi dan diskon produk, menggunakan **Properti** untuk enkapsulasi dan **Composition** untuk transaksi. |

## Konsep PBO yang Didemonstrasikan

Setiap file kode secara eksplisit menunjukkan kelima pilar PBO:

### 1. Kelas (Class)

*   **`workshop_oop_v2.py`**: Kelas seperti `Vehicle` (Abstrak), `Car`, `SportCar`, dan `ServiceBay`.
*   **`cosmetics_oop_v2.py`**: Kelas seperti `Product` (Abstrak), `Makeup`, `Skincare`, dan `Transaction`.

### 2. Objek (Object)

*   **`workshop_oop_v2.py`**: Pembuatan instance seperti `sedan = Car(...)`, `gtr = SportCar(...)`, dan `bay_A = ServiceBay(...)`.
*   **`cosmetics_oop_v2.py`**: Pembuatan instance seperti `lipstick = Makeup(...)`, `serum = Skincare(...)`, dan `transaction_vip = Transaction(...)`.

### 3. Enkapsulasi (Encapsulation)

*   **`workshop_oop_v2.py`**: Menggunakan atribut *protected* (`_engine_code`) dan mengontrol akses serta modifikasi melalui dekorator `@property` dan `@setter` pada kelas `Car`.
*   **`cosmetics_oop_v2.py`**: Menggunakan atribut *protected* (`_price`) dan mengontrol akses serta validasi melalui dekorator `@property` dan `@setter` pada kelas `Product`.

### 4. Inheritance (Pewarisan)

*   **`workshop_oop_v2.py`**: Menggunakan **Inheritance Multi-level** (`Vehicle` -> `Car` -> `SportCar`) untuk mewarisi sifat dan metode dari kelas induk.
*   **`cosmetics_oop_v2.py`**: Menggunakan **Inheritance** sederhana (`Product` -> `Makeup` dan `Product` -> `Skincare`) untuk mengkhususkan jenis produk.

### 5. Polimorfisme (Polymorphism)

*   **`workshop_oop_v2.py`**:
    *   **Metode Abstrak**: Metode `perform_diagnostic()` dan `get_service_cost()` didefinisikan di kelas abstrak `Vehicle` dan diimplementasikan secara berbeda di `Car` dan `SportCar`.
    *   **Overriding**: Metode `perform_diagnostic()` di kelas `SportCar` menimpa (override) metode dari kelas `Car`.
*   **`cosmetics_oop_v2.py`**:
    *   **Metode Abstrak**: Metode `calculate_discount()` diimplementasikan secara berbeda di `Makeup` dan `Skincare` untuk menghitung diskon berdasarkan tipe pelanggan dan jenis produk.
    *   **Composition**: Kelas `Transaction` menggunakan objek `Product` dan memanggil metode polimorfik (`calculate_discount`) tanpa perlu mengetahui tipe produk spesifik.

## Cara Menjalankan Kode

Pastikan Anda memiliki Python 3 terinstal.

1.  **Kloning Repositori** (jika Anda mengunggahnya ke GitHub):
    ```bash
    git clone [URL_REPOSITORI_ANDA]
    cd [NAMA_REPOSITORI]
    ```

2.  **Jalankan File Contoh:**
    ```bash
    python3 workshop_oop_v2.py
    python3 cosmetics_oop_v2.py
    ```

Output dari setiap file akan menunjukkan demonstrasi dari setiap konsep PBO secara berurutan.
