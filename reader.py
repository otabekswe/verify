"""
Ushbu modul fayllarni o'qish va yozish uchun kerakli funksiyalarni taqdim etadi.
"""

import os
import re # Murakkab matnlarni tozalash va tokenizatsiya qilish uchun kerak

from pathlib import Path
from typing import Iterator, Tuple, List
from collections import Counter

from vector import Vector


# Xabarni scamligni bilish uchun ba'zi so'zlarni aniqlash kifoya qiladi. 
# Biz o'sha so'zlar ro'yxatini tuzishimiz kerak bo'ladi. Buni kengayritish mumkin albatta.
SCAM_KEYWORDS = [
    "winner", "congratulations", "claim", "prize", "urgent", "verify",
    "account", "password", "ssn", "bank", "irs", "tax", "refund",
    "free", "money", "cash", "offer", "limited", "click", "link",
    "unsubscribe", "lottery", "inheritance", "guaranteed", "risk-free",
    "invoice", "payment", "due", "overdue", "suspended"
]

DIMENSIONS = len(SCAM_KEYWORDS)  # Vektor o'lchami


def sanitize_text_to_word(text: str) -> List[str]:
    """
    Matnni tozalash va lower case so'zlarga ajratish uchun.
    Murakkab matnlarni tozalash uchun regex ishlatiladi.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Belgilar va raqamlarni olib tashlaymiz
    words = text.split()
    return words


def text_to_vector(words: List[str]) -> Vector:
    """
    Berilgan matnni SCAM_KEYWORDS asosida vektorga aylantiradi.
    Har bir so'z SCAM_KEYWORDS ro'yxatida mavjud bo'lsa, vektor qiymati 1, aks holda 0 bo'ladi.
    """
    word_counts = Counter(words)  
    feature_values = [float(word_counts[keyword]) for keyword in SCAM_KEYWORDS]
    return Vector(feature_values)


def load_datapoint(dir_path: str, filename: str, label: str) -> Tuple[str, Vector]:
    """
    Fayldan matnni o'qib, vektorga aylantiradi va label bilan birga qaytaradi.
    """
    file_path = Path(dir_path) / filename
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            text_content = file.read()
    except Exception as e:
        print(f"Faylni o'qishda xatolik yuz berdi: {e}")
        return label, Vector([0] * DIMENSIONS)  # Xatolik yuz bersa, nol vektor qaytaramiz
    
    words = sanitize_text_to_word(text_content)
    vector = text_to_vector(words)
    return label, vector.normalize()  # Vektorni normalizatsiya qilamiz


def load_data(base_path: str) -> List[Tuple[str, Vector]]:
    """
    Berilgan katalogdagi fayllarni o'qib, har bir fayl uchun label va vektorlarni qaytaradi.
    Fayl nomi asosida label aniqlanadi: "scam" yoki "notscam".
    """
    dataset = []
    for label_type in ["scam", "notscam"]:
        dir_path = Path(base_path) / label_type
        if not dir_path.is_dir():
            print(f"Warning: Directory {dir_path} topilmadi, ammo davom etamiz.")
            continue
        for file_name in os.listdir(dir_path):
            if file_name.endswith(".txt"):
                label, vector = load_datapoint(str(dir_path), file_name, label_type)
                dataset.append((label, vector))
    return dataset


def my_input(message: str) -> str:
    """
    Foydalanuvchidan matn kiritishni so'raydi va kiritilgan matnni qaytaradi.
    Multi line matn kiritish uchun EOFError yordamida tugatish mumkin.
    """
    print(message)
    content = []
    while True:
        try:
            line = input()
            if line.strip().upper() == "EOF":
                break
            content.append(line)
        except EOFError:
            break
    return "\n".join(content)