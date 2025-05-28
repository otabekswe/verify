"""
!!!Vektorlar

Kompyuterlar matnlar va shu kabi ma'lumotlarni tushunmaydi. Ular faqat raqamlarni tushunadi.
Shuning uchun ham biz ma'lumotlarimizni raqamlar ko'rinishida ifodalashimiz kerak.
Buning uchun esa bizga Vektorlar kerak bo'ladi.
Biz Vektor turini o'zimiz 0dan yaratamiz.
"""

import math

class Vector:
    def __init__(self, values: list[float] | tuple[float, ...] = [0.0]):
        self.values = values

    def scale(self, n: float) -> 'Vector':
        """
        Vektorni scalar n ga ko'paytirish. Bu asosan perceptron o'rganish jarayonida ishlatiladi.
        Example: v.scale(2)
        """
        return Vector([val * n for val in self.values])
    
    def product(self, other: 'Vector') -> float:
        """
        Vektorlar orasidagi skalar ko'paytma (dot product) hisoblash (ikki vektorning mos keluvchi elementlarini ko'paytirib, ularni yig'ish).
        Bu asosan perceptron net input'ini hisoblash uchun ishlatiladi.
        Example: v1.product(v2)
        """
        if len(self.values) != len(other.values):
            raise ValueError("Vektorlar uzunligi teng bo'lishi lozim.")
        return sum(a * b for a, b in zip(self.values, other.values))
    
    def length(self) -> float:
        """
        Vektor uzunligini hisoblash (Euclidean norm).
        Bu asosan vektorlarni normalizatsiya qilish uchun ishlatiladi.
        Example: v.length()
        """
        return math.sqrt(sum(val ** 2 for val in self.values))
    
    def normalize(self) -> 'Vector':
        """
        Vektorni normalizatsiya qilish (uzunligini 1 ga tenglashtirish).
        Bu asosan vektorlarni o'zaro solishtirishda ishlatiladi.
        Example: v.normalize()
        """
        vec_length = self.length()
        if vec_length == 0:
            raise ValueError("Vektor uzunligi nolga teng bo'lsa, normalizatsiya mumkin emas.")
        return Vector([val / vec_length for val in self.values])
    
    def copy(self) -> 'Vector':
        """
        Vektor nusxasini yaratish.
        Bu asosan vektorlarni o'zgartirmasdan ishlatish uchun kerak bo'ladi.
        Example: v.copy()
        """
        return Vector(self.values.copy())

    def __mul__(self, other: 'Vector') -> float:
        """
        Vektorlar orasidagi skalar ko'paytma (dot product) operatori.
        Example: v1 * v2
        """
        if isinstance(other, (float, int)):
            return self.scale(other)
        elif isinstance(other, Vector):
            return self.product(other)
        return NotImplemented
    
    def __add__(self, other: 'Vector') -> 'Vector':
        """
        Vektorlarni qo'shish operatori.
        Example: v1 + v2
        """
        if len(self.values) != len(other.values):
            raise ValueError("Vektorlar uzunligi teng bo'lishi lozim.")
        return Vector([a + b for a, b in zip(self.values, other.values)])
    
    def __repr__(self) -> str:
        """
        Vektorni matn ko'rinishida ifodalash.
        Example: str(v)
        """
        return f"Vector({self.values})"
