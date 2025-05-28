"""
Perceptronlar mashq qilingandan ya'ni o'rgatilgandan so'ng, Selector klassi yordamida berilgan vektor uchun 
eng mos keladigan labelni tanlash mumkin. Selector klassi, o'rgatilgan Perceptronlar ro'yxatini oladi va berilgan 
vektor uchun eng yuqori output qiymatiga ega bo'lgan Perceptronning labelini qaytaradi.
Berilgan vektor inputga qarab, har bir Perceptron output qiymatini hisoblaydi va eng yuqori qiymatga ega
Perceptronning labelini tanlaydi va qaytaradi.
"""

from typing import List, Callable

from perceptron import Perceptron, sigmoid
from vector import Vector

class Selector:
    def __init__(self, perceptrons: List[Perceptron], activation_func_for_selection: Callable):
        self.perceptrons = perceptrons
        self.activation_func = activation_func_for_selection

    def select(self, vector: Vector) -> str:
        """
        Berilgan vektor uchun eng mos keladigan Perceptron labelini tanlaydi.
        Barcha Perceptronlarni iteratsiya qilib, har birining output qiymatini oladi,
        va eng yuqori qiymatga ega bo'lgan Perceptronning labelini qaytaradi.
        """
        if not self.perceptrons:
            return "Hech qanday perceptron mavjud emas"

        max_output = -float('inf') # Boshlang'ich qiymat sifatida minimal qiymat
        selected_label = self.perceptrons[0].label # Boshlang'ich label sifatida birinchi perceptronning labeli

        for perceptron in self.perceptrons:
            output = perceptron.output_value(vector, activation_func=self.activation_func)
            if output > max_output:
                max_output = output
                selected_label = perceptron.label

        # Ikki klassli "scam" va "not_scam" uchun, agar sizda faqat bitta perceptron bo'lsa (masalan, "scam" uchun)
        # siz uning outputini to'g'ridan-to'g'ri talqin qilishingiz mumkin (masalan, > 0.5 - agar sigmoiddan foydalansangiz, scam)
        # Ammo bu tuzilma asl loyihadagi kabi bir nechta klasslarni qo'llab-quvvatlaydi.
        return selected_label