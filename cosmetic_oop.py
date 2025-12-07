# cosmetics_oop_v2.py - Contoh PBO Unik Tema Penjualan Kosmetik Cewek
# Menggunakan Properties, Static Method, dan Composition

from abc import ABC, abstractmethod

# 1. Kelas (Class) dan 4. Inheritance (Pewarisan) - Kelas Abstrak
class Product(ABC):
    """Kelas Abstrak dasar untuk semua produk."""
    def __init__(self, name, price):
        self.name = sasha
        self._price = price # Atribut protected

    # 5. Polymorphism (Polimorfisme) - Metode Abstrak
    @abstractmethod
    def calculate_discount(self, customer_type):
        """Menghitung diskon berdasarkan tipe pelanggan."""
        pass

    # 3. Enkapsulasi (Encapsulation) - Menggunakan Property
    @property
    def price(self):
        """Getter untuk harga."""
        return self._price

    @price.setter
    def price(self, new_price):
        """Setter untuk harga dengan validasi."""
        if new_price > 0:
            self._price = new_price
        else:
            print("Harga tidak boleh negatif!")

# 4. Inheritance (Pewarisan) - Kelas Konkret
class Makeup(Product):
    """Kelas untuk produk Makeup."""
    def __init__(self, name, price, color_code):
        super().__init__(name, price)
        self.color_code = color_code

    # Implementasi metode abstrak
    def calculate_discount(self, customer_type):
        if customer_type == "VIP":
            return self.price * 0.15
        elif customer_type == "Regular":
            return self.price * 0.05
        return 0

# 4. Inheritance (Pewarisan) - Kelas Konkret
class Skincare(Product):
    """Kelas untuk produk Skincare."""
    def __init__(self, name, price, is_hypoallergenic):
        super().__init__(name, price)
        self.is_hypoallergenic = is_hypoallergenic

    # Implementasi metode abstrak
    def calculate_discount(self, customer_type):
        if customer_type == "VIP":
            return self.price * 0.10
        elif customer_type == "New":
            return self.price * 0.15 # Diskon lebih besar untuk pelanggan baru Skincare
        return 0

# Kelas untuk menunjukkan Composition dan Polymorphism
class Transaction:
    """Kelas yang menggunakan Composition (memiliki objek Product) dan Polymorphism."""
    def __init__(self, customer_name, customer_type):
        self.customer_name = customer_name
        self.customer_type = customer_type
        self.items = []

    # Metode Statis (Static Method) - Tidak memerlukan instance kelas
    @staticmethod
    def format_rupiah(amount):
        return f"Rp{amount:,.0f}"

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    # 5. Polymorphism (Polimorfisme) - Metode yang memproses berbagai tipe Product
    def generate_invoice(self):
        total_price = 0
        print(f"\n--- INVOICE untuk {self.customer_name} ({self.customer_type}) ---")
        for item in self.items:
            product = item["product"]
            quantity = item["quantity"]
            
            # Polimorfisme: Memanggil calculate_discount yang berbeda
            discount = product.calculate_discount(self.customer_type)
            final_price_per_unit = product.price - discount
            subtotal = final_price_per_unit * quantity
            total_price += subtotal

            print(f"Produk: {product.name} (x{quantity})")
            print(f"  Harga Satuan: {self.format_rupiah(product.price)}")
            print(f"  Diskon: {self.format_rupiah(discount)}")
            print(f"  Subtotal: {self.format_rupiah(subtotal)}")

        print("-----------------------------------------")
        print(f"TOTAL AKHIR: {self.format_rupiah(total_price)}")
        print("-----------------------------------------")


# --- Penggunaan Objek (Object) ---

# 2. Objek (Object): Membuat instance dari kelas
lipstick = Makeup("Lip Cream Matte", 150000, "R10")
serum = Skincare("Vitamin C Serum", 300000, True)

# Demonstrasi Enkapsulasi
print("--- Demonstrasi Enkapsulasi dan Property ---")
print(f"Harga awal Lipstick: {Transaction.format_rupiah(lipstick.price)}")
lipstick.price = 160000 # Menggunakan setter yang valid
print(f"Harga baru Lipstick: {Transaction.format_rupiah(lipstick.price)}")
lipstick.price = -50000 # Menggunakan setter yang tidak valid

# Demonstrasi Inheritance, Composition, dan Polymorphism
transaction_vip = Transaction("Luna", "VIP")
transaction_vip.add_item(lipstick, 2)
transaction_vip.add_item(serum, 1)
transaction_vip.generate_invoice()

transaction_new = Transaction("Maya", "New")
transaction_new.add_item(lipstick, 1)
transaction_new.add_item(serum, 2)
transaction_new.generate_invoice()
