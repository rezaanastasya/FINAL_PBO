# workshop_oop_v2.py - Contoh PBO Unik Tema Bengkel Cowok
# Menggunakan ABC, Properties, dan Multi-level Inheritance

from abc import ABC, abstractmethod

# 1. Kelas (Class) dan 4. Inheritance (Pewarisan) - Kelas Abstrak
class Vehicle(ABC):
    """Kelas Abstrak dasar untuk semua kendaraan."""
    def __init__(self, brand, model, engine_code):
        self.brand = brand
        self.model = model
        self._engine_code = engine_code # Atribut protected

    # 5. Polymorphism (Polimorfisme) - Metode Abstrak
    @abstractmethod
    def perform_diagnostic(self):
        """Melakukan diagnostik spesifik kendaraan."""
        pass

    @abstractmethod
    def get_service_cost(self):
        """Menghitung biaya servis dasar."""
        pass

# 3. Enkapsulasi (Encapsulation) - Menggunakan Property
class Car(Vehicle):
    """Kelas untuk Mobil, mewarisi dari Vehicle."""
    def __init__(self, brand, model, engine_code, base_price):
        super().__init__(brand, model, engine_code)
        self._base_price = base_price # Atribut privat/protected

    @property
    def engine_code(self):
        """Getter untuk engine_code."""
        return self._engine_code

    @engine_code.setter
    def engine_code(self, new_code):
        """Setter untuk engine_code dengan validasi."""
        if len(new_code) == 6:
            self._engine_code = new_code
        else:
            print("Kode mesin harus 6 karakter!")

    # Implementasi metode abstrak
    def perform_diagnostic(self):
        return f"Diagnostik Mobil {self.brand} {self.model} (Kode Mesin: {self.engine_code}) selesai. Cek ECU."

    def get_service_cost(self):
        return self._base_price * 0.15 # Biaya servis 15% dari harga dasar

# 4. Inheritance (Pewarisan) - Multi-level Inheritance
class SportCar(Car):
    """Kelas untuk Mobil Sport, mewarisi dari Car."""
    def __init__(self, brand, model, engine_code, base_price, turbo_boost):
        super().__init__(brand, model, engine_code, base_price)
        self.turbo_boost = turbo_boost

    # 5. Polymorphism (Polimorfisme) - Override
    def perform_diagnostic(self):
        # Memanggil metode kelas induk
        base_diag = super().perform_diagnostic()
        return f"{base_diag} Tambahan: Cek tekanan turbo ({self.turbo_boost} psi)."

    def get_service_cost(self):
        # Biaya servis mobil sport lebih mahal
        return self._base_price * 0.25

# Kelas lain untuk menunjukkan Polymorphism
class ServiceBay:
    """Kelas yang menangani berbagai jenis kendaraan."""
    def __init__(self, bay_id):
        self.bay_id = bay_id

    # 5. Polymorphism (Polimorfisme) - Metode yang menerima objek Vehicle
    def process_service(self, vehicle):
        print(f"\n--- Bay {self.bay_id} Memproses Kendaraan ---")
        print(f"Kendaraan: {vehicle.brand} {vehicle.model}")
        print(vehicle.perform_diagnostic()) # Polimorfisme: memanggil metode yang berbeda
        cost = vehicle.get_service_cost()
        print(f"Total Biaya Servis Estimasi: Rp{cost:,.0f}")
        print("-----------------------------------------")


# --- Penggunaan Objek (Object) ---

# 2. Objek (Object): Membuat instance dari kelas
sedan = Car("Toyota", "Vios", "1NZ-FE", 250000000)
gtr = SportCar("Nissan", "GT-R", "VR38DETT", 1500000000, 14.7)
bay_A = ServiceBay("A")

# Demonstrasi Enkapsulasi
print("--- Demonstrasi Enkapsulasi dan Property ---")
print(f"Kode Mesin Sedan Awal: {sedan.engine_code}")
sedan.engine_code = "2NZ-FE" # Menggunakan setter yang valid
print(f"Kode Mesin Sedan Baru: {sedan.engine_code}")
sedan.engine_code = "ABC" # Menggunakan setter yang tidak valid
print(f"Kode Mesin Sedan Setelah Gagal Set: {sedan.engine_code}")

# Demonstrasi Inheritance dan Polymorphism
print("\n--- Demonstrasi Inheritance dan Polymorphism ---")
bay_A.process_service(sedan) # Polimorfisme dengan objek Car
bay_A.process_service(gtr)   # Polimorfisme dengan objek SportCar (Multi-level Inheritance)

# Contoh lain Polimorfisme
vehicles = [sedan, gtr]
print("\n--- Contoh Polimorfisme dalam List ---")
for v in vehicles:
    print(f"{v.brand} {v.model} - Diagnostik: {v.perform_diagnostic()}")
    print(f"Biaya Servis: Rp{v.get_service_cost():,.0f}")
