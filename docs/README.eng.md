<h1 align=center>VeriFy</h1>

This project demonstrates a simple artificial intelligence model that helps analyze texts and determine if they are "scam" or "notscam".

## Project Description

**Overall Goal:**
The main goal of this project is to create and train a simple Perceptron model to analyze textual data (e.g., emails, SMS messages, online reviews) and determine if they are related to scams. This helps protect users from potential online threats. Remember to input more data to increase accuracy. The more the model trains, the better it will become.

**Main Components and Their Functions:**

1.  **vector.py (Vectors):**
    *   Computers don't directly "understand" text; they work with numbers. This module contains the `Vector` class to convert texts (specifically, words in the text) into numerical representations, i.e., mathematical vectors.
    *   It allows performing various mathematical operations on vectors (e.g., addition, scalar multiplication, normalization).

2.  **reader.py (Data Reading and Preparation):**
    *   This module is responsible for reading training and test data in `.txt` format from files.
    *   It preprocesses the texts: removes unnecessary characters (`sanitize_text_to_word`), converts all letters to lowercase.
    *   Most importantly, it converts each text into a vector based on a list of keywords called `SCAM_KEYWORDS` (`text_to_vector`). If a keyword from the list is found in the text, the corresponding component of the vector gets a value (e.g., 1.0), otherwise 0.0.
    *   The `DIMENSIONS` variable is equal to the number of words in the `SCAM_KEYWORDS` list and defines the dimension of the resulting vectors.

3.  **perceptron.py (Perceptron Model):**
    *   A Perceptron is the simplest type of artificial neural network, mainly used for binary classification tasks (i.e., assigning an object to one of two classes).
    *   In the project, each perceptron corresponds to a specific label (e.g., "scam" or "notscam").
    *   It processes an input vector using its "weights" and "bias" values.
    *   It converts the calculated result into a value (usually between 0 and 1) through an activation function (`sigmoid` or `step_function`). This value represents the perceptron's "confidence" level regarding the input vector.
    *   It "learns" by iteratively updating its weights and bias based on the training data using the `train` method.

4.  **trainer.py (Model Trainer):**
    *   This module manages the process of training one or more perceptrons (in our case, `perceptron_scam` and `perceptron_notscam`) using the training data (`training_data`).
    *   The training process is carried out based on hyperparameters defined in main.py, such as `learning_rate` and `iterations`.

5.  **selector.py (Selector):**
    *   Accepts a list of trained perceptrons (in our case, two perceptrons).
    *   When a new, unknown vector arrives, each perceptron calculates its "output" value for this vector.
    *   It selects the label of the perceptron that gave the highest output value (e.g., "scam" or "notscam") as the final prediction.

6.  **main.py (Main Program File):**
    *   This is the main entry point of the program and the central hub that connects all components.
    *   **Settings:** Defines global settings like `LEARNING_RATE`, `ITERATIONS`, `ACTIVATION_FOR_TRAINING`, `ACTIVATION_FOR_SELECTION`.
    *   **Data Loading:** Loads training and test data using reader.py.
    *   **Model Creation:** Creates two `Perceptron` objects (for "scam" and "notscam") with initial weights.
    *   **Training:** Creates a `Trainer` object and trains the perceptrons.
    *   **Evaluation:** Tests the trained model on test data using the `Selector` and calculates the accuracy.
    *   **Interactive Prediction:** Allows the user to input their text and see it classified by the model as "scam" or "not scam".

**How the Project Works (Step-by-step):**

1.  **Data Preparation:** The program reads `.txt` files from the train and test folders. Each file is considered a separate text sample. It is labeled based on the folder it's in ("scam" or "notscam").
2.  **Vectorization:** After each text is cleaned in reader.py, it is converted into a numerical vector based on the presence of words from the `SCAM_KEYWORDS` list.
3.  **Model Training:** The two perceptrons created in main.py (for `scam` and `notscam`) are trained using the `Trainer` based on the training data (vectors and their labels). During training, the perceptrons adjust their weights and biases according to errors, the specified `learning_rate`, and the number of `iterations`.
4.  **Model Testing:** After training is complete, the model's generalization ability is checked using previously "unseen" data from the test folder. The `Selector` makes a prediction for each test vector, and this prediction is compared with the true label to calculate the model's accuracy (the proportion of correctly identified samples).
5.  **User Text Prediction:** The program prompts the user to enter new text. The entered text is processed in the same way as in the steps above (cleaned, vectorized) and classified as "scam" or "not scam" using the `Selector`. The result is shown to the user.

**How to Use:**

1.  **Database:** Place text files in `.txt` format into the scam and notscam folders. Each file should contain one message or text sample. The more high-quality data, the better the model will learn.
2.  **Run the Program:** Run the program by typing the command
```
python main.py
```
in the terminal.
3.  The program will first train the models, then show the accuracy achieved on the test data, and then prompt you to enter new text.

**Project Settings and Improvement Paths:**

*   **`SCAM_KEYWORDS` (reader.py):** This list is like the "brain" of the model. Expanding, refining, or adapting it to the context can significantly improve model quality.
*   **Hyperparameters (main.py):** Experimenting with (tuning) values like `LEARNING_RATE` (learning speed) and `ITERATIONS` (number of training epochs) can lead to better results.
*   **Activation Functions (main.py):** `sigmoid` or `step_function` are selected for `ACTIVATION_FOR_TRAINING` and `ACTIVATION_FOR_SELECTION`. Trying other activation functions is also possible (but this might deviate from the classic Perceptron).
*   **Vectorization Methods:** Currently, vectors are created based on the presence (or count) of words. Using more complex vectorization methods like TF-IDF can improve model efficiency.
*   **More Complex Models:** The Perceptron is a simple model. If the accuracy is unsatisfactory, consider using more powerful models like Logistic Regression, Support Vector Machines (SVM), or even simple neural networks.

This project is a good starting point for getting acquainted with text classification and machine learning basics.
