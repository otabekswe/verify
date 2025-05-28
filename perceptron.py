"""
!!!Perceptron

Perceptron bu neural network modelini eng sodda shakli hisoblanadi. U input sifatida vektor qabul qiladi va bu vektorlarni weights (og'irliklar) bilan ko'paytirib, output'ni `activation function` orqali qaytaradi (odatda 0 yoki 1).
Perceptronlar asosan og'irliklarni o'zgarishi orqali o'rganadi (learning) va shu orqali ma'lum bir vazifani bajarishga qodir bo'ladi.
Perceptronlar asosan binary classification (ikki sinfli tasniflash) vazifalarida ishlatiladi.

"""
import math
from typing import Callable, Iterable, Tuple # type hint uchun kerak bo'ladi
from vector import Vector # Vector klassimizni import qilamiz


def sigmoid(net_input: float) -> float:
    """
    Sigmoid aktivatsiya funksiyasi xisoblanadi. Bu funksiya net input'ni 0 va 1 orasida qiymatga aylantiradi.
    Bu asosan ehtimoliy tasniflash vazifalarida ishlatiladi.
    """
    try:
        return 1 / (1 + math.exp(-net_input))
    except OverflowError: # Agar net_input juda katta yoki juda kichik bo'lsa
        return 0.0 if net_input < 0 else 1.0


def step_function(net_input: float) -> int:
    """
    Step function aktivatsiya funksiyasi xisoblanadi.
    Agar net input 0 dan katta bo'lsa, 1 qaytaradi, qolgan hollarda 0 qaytaradi.
    Asosan binary classification vazifalarida ishlatiladi.
    """
    return 1 if net_input >= 0 else 0


class Perceptron:
    def __init__(self, label: str, init_weight: Vector, init_bias: float = 0.0):
        """
        Perceptron klassi yaratiladi.
        - label: Perceptronning nomi yoki identifikatori. (Bizni holatda "scam" yoki "scam emas")
        - init_weight: Perceptronning boshlang'ich og'irliklari (weights) vektori.
        - init_bias: Perceptronning boshlang'ich bias (og'irliksiz qo'shimcha) qiymati.
        """
        self.label = label
        self.weights = init_weight
        self.bias = init_bias
    
    def output_value(self, x: Vector, activation_func: Callable = step_function) -> float:
        """
        Berilgan x vektori uchun Perceptronning output qiymatini hisoblaydi.
        """
        activation_func = activation_func
        net_input = (self.weights * x) + self.bias # dot product va bias qo'shiladi
        return activation_func(net_input)

    def train(self, training_data: Iterable[Tuple[Vector, Vector]], learning_rate: float, iterations: int, activation_func_for_train: Callable = step_function):
        """
        Berilgan ma'lumotlari bilan Perceptronni o'rgatadi. Va o'rgatish jarayonida wieghts va bias'ni yangilab boradi. 
        Bu ishni qilishga sabab, Perceptron o'zini o'rgatish jarayonida xatolarni kamaytirishga harakat qiladi.
        """
        for i in range(iterations):
            # Har bir iteratsiyada xatolarni hisoblaymiz
            errors_in_iteration = 0
            for expected_label, x_vector in training_data:
                # Perceptronning hozirgi output qiymatini berilgan x vektori uchun hisoblaymiz
                y_output = self.output_value(x_vector, activation_func_for_train)

                # 'd' qiymatini hisoblaymiz (xato)
                d_output = 1 if expected_label == self.label else 0

                # Xatolarni hisoblaymiz
                error = d_output - y_output

                if error != 0:
                    errors_in_iteration += 1

                    # Weights'ni yangilaymiz: weight = old_weight + learning_rate * error * x
                    self.weights += (x_vector * (learning_rate * error))

                    # Bias'ni yangilaymiz: bias = old_bias + learning_rate * error
                    self.bias += learning_rate * error

