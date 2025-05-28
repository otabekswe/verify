from selector import Selector
from perceptron import Perceptron, sigmoid, step_function
from trainer import Trainer
from reader import load_data, sanitize_text_to_word, text_to_vector, \
                   my_input, DIMENSIONS
from vector import Vector

# --- Configuration ---
LEARNING_RATE = 0.02
ITERATIONS = 50
ACTIVATION_FOR_TRAINING = sigmoid
ACTIVATION_FOR_SELECTION = sigmoid


if __name__ == '__main__':
    training_data_path = "data/train"
    training_data = load_data(training_data_path)
    if not training_data:
        print(f"Hech qanday o'qitish ma'lumotlari topilmadi {training_data_path}.")
        exit()

    test_data_path = "data/test"
    test_data = load_data(test_data_path)
    if not test_data:
        print(f"Hech qanday test ma'lumotlari topilmadi {test_data_path}. Iltimos, baholash uchun ba'zi ma'lumotlarni yarating.")

    default_initial_weight = Vector([0.01] * DIMENSIONS)

    perceptron_scam = Perceptron(
        label="scam",
        init_weight=default_initial_weight.copy()
    )
    perceptron_not_scam = Perceptron(
        label="notscam",
        init_weight=default_initial_weight.copy()
    )
    
    perceptrons = [perceptron_scam, perceptron_not_scam]

    print("Starting training...")
    trainer = Trainer(perceptrons, training_data)
    
    trainer.train_all(
        LEARNING_RATE,
        ITERATIONS,
        activation_func_for_train=ACTIVATION_FOR_TRAINING
    )
    print("Training finished successfully.\n")

    selector = Selector(perceptrons, activation_func_for_selection=ACTIVATION_FOR_SELECTION)

    if test_data:
        total_samples = 0
        correct_predictions = 0
        for expected_label, vector in test_data:
            prediction = selector.select(vector)
            if prediction == expected_label:
                correct_predictions += 1
            total_samples += 1
        
        if total_samples > 0:
            accuracy = (correct_predictions / total_samples) * 100
            print(f"Test Accuracy: {accuracy:.2f}% ({correct_predictions}/{total_samples})\n")
        else:
            print("Baholash uchun test ma'lumotlari mavjud emas.")
    else:
        print("\nHech qanday test topilmadi va baholash amalga oshirilmadi.")

    while True:
        user_text = my_input("Xabaringiz (To'xtatish uchun Ctrl + C bosing):")
        if not user_text.strip():
            print("Hech qanday kiritish amalga oshirilmadi.")
            continue

        sanitized_words = sanitize_text_to_word(user_text)
        input_vector = text_to_vector(sanitized_words).normalize()

        prediction = selector.select(input_vector)
        prediction = "scam" if prediction == "scam" else "scam emas"
        print(f"Siz kiritgan xabar {prediction.upper()}.")
        print("-" * 30)

