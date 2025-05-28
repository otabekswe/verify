"""
Ushbu modul modelni o'qitish uchun kerakli funksiya va classlarni taqdim etadi.

"""
from typing import List, Tuple, Callable # type hinting uchun
from threading import Thread

from perceptron import Perceptron, step_function
from vector import Vector

class Trainer:
    def __init__(
            self,
            perceptrons: List[Perceptron],
            training_data: List[Tuple[str, Vector]],
    ):
        self.perceptrons = perceptrons
        self.training_data = training_data

    def train_all(
        self,
        learning_rate: float,
        iterations: int,
        activation_func_for_train: Callable = None
    ):
        """
        Barcha perceptronlarni berilgan ma'lumotlar bilan o'qitadi. Oddiy o'qitish jarayoni.
        """
        activation_func = activation_func_for_train or step_function

        for perceptron in self.perceptrons:
            perceptron.train(
                self.training_data,
                learning_rate,
                iterations,
                activation_func_for_train=activation_func
            )

    def train_parallel(self, learning_rate: float, iterations: int, activation_func_for_train: Callable = None):
        """
        Barcha perceptronlarni parallel ravishda o'qitadi. Bu o'qitish jarayonini tezlashtiradi.
        """
        threads = []
        activation_func = activation_func_for_train or step_function
        for perceptron in self.perceptrons:
            args_tuple = (self.training_data, learning_rate, iterations, activation_func)
            thread = Thread(target=perceptron.train, args=args_tuple, name=perceptron.label)
            threads.append(thread)
            thread.start()
    
        for thread in threads:
            thread.join()