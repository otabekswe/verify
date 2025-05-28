<h1 align=center>VeriFy</h1>

Ushbu loyiha matnlarni tahlil qilib, ularning "scam" (firibgarlik) yoki "notscam" (firibgarlik emas) ekanligini aniqlashga yordam beradigan oddiy sun'iy intellekt modelini namoyish etadi.

## Loyiha Tavsifi

**Umumiy Maqsad:**
Ushbu loyihaning asosiy maqsadi — matnli ma'lumotlarni (masalan, elektron xatlar, SMS xabarlar, onlayn sharhlar) tahlil qilib, ularning firibgarlikka aloqador yoki yo'qligini aniqlash uchun oddiy Perseptron modelini yaratish va o'rgatishdir. Bu foydalanuvchilarni potentsial onlayn xavflardan himoya qilishga yordam beradi. Aniqlikni oshirish uchun ko'proq ma'lumot kiritishni unutmang. Model qancha ko'p mashq qilsa shuncha yaxshilanib boraveradi.

**Asosiy Komponentlar va Ularning Vazifalari:**

1.  **vector.py (Vektorlar):**
    *   Kompyuterlar matnlarni to'g'ridan-to'g'ri "tushunmaydi"; ular raqamlar bilan ishlaydi. Ushbu modul matnlarni (aniqrog'i, matndagi so'zlarni) raqamli ko'rinishga, ya'ni matematik vektorlarga aylantirish uchun `Vector` klassini o'z ichiga oladi.
    *   Vektorlar ustida turli matematik amallar (masalan, qo'shish, skalyar songa ko'paytirish, normalizatsiya) bajarish imkonini beradi.

2.  **reader.py (Ma'lumotlarni O'qish va Tayyorlash):**
    *   Bu modul `.txt` formatidagi o'quv (train) va test (test) ma'lumotlarini fayllardan o'qish uchun mas'ul.
    *   Matnlarni dastlabki qayta ishlaydi: keraksiz belgilarni olib tashlaydi (`sanitize_text_to_word`), barcha harflarni kichik harfga o'tkazadi.
    *   Eng muhimi, `SCAM_KEYWORDS` nomli ro'yxatdagi kalit so'zlar asosida har bir matnni vektorga aylantiradi (`text_to_vector`). Agar matnda ro'yxatdagi kalit so'z uchrasa, vektorning tegishli komponentasi qiymat oladi (masalan, 1.0), aks holda 0.0.
    *   `DIMENSIONS` o'zgaruvchisi `SCAM_KEYWORDS` ro'yxatidagi so'zlar soniga teng bo'lib, hosil bo'ladigan vektorlarning o'lchamini belgilaydi.

3.  **perceptron.py (Perseptron Modeli):**
    *   Perseptron — bu sun'iy neyron tarmoqlarining eng sodda turi bo'lib, asosan ikkilik klassifikatsiya (binary classification) masalalarida qo'llaniladi (ya'ni, obyektni ikki sinfdan biriga ajratish).
    *   Loyihada har bir perseptron ma'lum bir yorliqqa (masalan, "scam" yoki "notscam") javob beradi.
    *   U kiruvchi vektorni o'zining "og'irliklari" (weights) va "bias" (siljish/erkin had) qiymatlari yordamida qayta ishlaydi.
    *   Hisoblangan natijani aktivatsiya funksiyasi (`sigmoid` yoki `step_function`) orqali (odatda 0 va 1 oralig'idagi) qiymatga aylantiradi. Bu qiymat perseptronning kiruvchi vektorga nisbatan "ishonch" darajasini bildiradi.
    *   `train` metodi yordamida o'z og'irliklarini va biasini o'quv ma'lumotlari asosida iterativ tarzda yangilab, "o'rganadi".

4.  **trainer.py (Modelni O'qituvchi):**
    *   Bu modul bir yoki bir nechta perseptronni (bizning holatda `perceptron_scam` va `perceptron_notscam`) o'quv ma'lumotlari (`training_data`) yordamida o'qitish jarayonini boshqaradi.
    *   O'qitish jarayoni main.py da belgilangan `learning_rate` (o'rganish tezligi) va `iterations` (takrorlashlar soni) kabi giperparametrlar asosida amalga oshiriladi.

5.  **selector.py (Tanlovchi):**
    *   O'qitilgan perseptronlar ro'yxatini (bizning holatda ikkita perseptron) qabul qiladi.
    *   Yangi, noma'lum vektor kelganda, har bir perseptron bu vektor uchun o'zining "javob" (output) qiymatini hisoblaydi.
    *   Eng yuqori javob qiymatini bergan perseptronning yorlig'ini (masalan, "scam" yoki "notscam") yakuniy bashorat sifatida tanlaydi.

6.  **main.py (Asosiy Dastur Fayli):**
    *   Bu dasturning asosiy ishga tushirish nuqtasi va barcha komponentlarni birlashtiruvchi markaz.
    *   **Sozlamalar:** `LEARNING_RATE`, `ITERATIONS`, `ACTIVATION_FOR_TRAINING`, `ACTIVATION_FOR_SELECTION` kabi global sozlamalarni belgilaydi.
    *   **Ma'lumotlarni Yuklash:** reader.py yordamida o'quv va test ma'lumotlarini yuklaydi.
    *   **Modellarni Yaratish:** Ikkita `Perceptron` obyektini ("scam" va "notscam" uchun) boshlang'ich og'irliklar bilan yaratadi.
    *   **O'qitish:** `Trainer` obyektini yaratib, perseptronlarni o'qitadi.
    *   **Baholash:** `Selector` yordamida o'qitilgan modelni test ma'lumotlarida sinab ko'radi va aniqlik (accuracy) darajasini hisoblab chiqaradi.
    *   **Interaktiv Bashorat:** Foydalanuvchiga o'z matnini kiritish va model tomonidan uning "scam" yoki "scam emas" deb tasniflanishini ko'rish imkonini beradi.

**Loyiha Qanday Ishlaydi (Bosqichma-bosqich):**

1.  **Ma'lumotlarni Tayyorlash:** Dastur train va test papkalaridagi `.txt` fayllarni o'qiydi. Har bir fayl alohida matn namunasi hisoblanadi. Faylning joylashgan papkasiga qarab ("scam" yoki "notscam") unga yorliq beriladi.
2.  **Vektorlashtirish:** Har bir matn reader.py da tozalangach, `SCAM_KEYWORDS` ro'yxatidagi so'zlarning mavjudligiga qarab raqamli vektorga aylantiriladi.
3.  **Modelni O'qitish:** main.py da yaratilgan ikkita perseptron (`scam` va `notscam` uchun) `Trainer` yordamida o'quv ma'lumotlari (vektorlar va ularning yorliqlari) asosida o'qitiladi. O'qitish jarayonida perseptronlar o'zlarining og'irliklarini va biaslarini xatoliklarga qarab, belgilangan `learning_rate` va `iterations` soniga muvofiq to'g'rilab boradi.
4.  **Modelni Sinovdan O'tkazish:** O'qitish tugagach, modelning umumlashtirish qobiliyati test papkasidagi avval "ko'rmagan" ma'lumotlar yordamida tekshiriladi. `Selector` har bir test vektori uchun bashorat qiladi va bu bashorat haqiqiy yorliq bilan solishtirilib, modelning aniqligi (to'g'ri topilgan namunalar ulushi) hisoblanadi.
5.  **Foydalanuvchi Matnini Bashorat Qilish:** Dastur foydalanuvchidan yangi matn kiritishni so'raydi. Kiritilgan matn ham xuddi yuqoridagi bosqichlardagidek qayta ishlanadi (tozalanadi, vektorlashtiriladi) va `Selector` yordamida "scam" yoki "scam emas" deb tasniflanadi. Natija foydalanuvchiga ko'rsatiladi.

**Qanday Foydalanish Mumkin:**

1.  **Ma'lumotlar Bazasi:** scam, notscam papkalariga `.txt` formatida matnli fayllarni joylashtiring. Har bir fayl bitta xabar yoki matn namunasini o'z ichiga olishi kerak. Qancha ko'p va sifatli ma'lumot bo'lsa, model shuncha yaxshi o'rganadi.
2.  **Dasturni Ishga Tushirish:** Terminal orqali
```
python main.py
``` 
buyrug'ini terish orqali dasturni ishga tushiring.
3.  Dastur avval modellarni o'qitadi, keyin test ma'lumotlarida erishilgan aniqlikni ko'rsatadi va so'ngra sizdan yangi matn kiritishingizni so'raydi.

**Loyiha Sozlamalari va Yaxshilash Yo'llari:**

*   **`SCAM_KEYWORDS` (reader.py):** Bu ro'yxat modelning "miya"si desak bo'ladi. Uni kengaytirish, aniqlashtirish yoki kontekstga moslashtirish orqali model sifatini sezilarli darajada oshirish mumkin.
*   **Giperparametrlar (main.py):** `LEARNING_RATE` (o'rganish tezligi) va `ITERATIONS` (o'qitish davrlari soni) kabi qiymatlarni o'zgartirib tajriba qilish (tuning) orqali yaxshiroq natijalarga erishish mumkin.
*   **Aktivatsiya Funksiyalari (main.py):** `ACTIVATION_FOR_TRAINING` va `ACTIVATION_FOR_SELECTION` uchun `sigmoid` yoki `step_function` tanlangan. Boshqa aktivatsiya funksiyalarini sinab ko'rish ham mumkin (lekin bu Perseptronning klassik variantidan chetga chiqishni anglatishi mumkin).
*   **Vektorlashtirish Usullari:** Hozirda so'zlarning mavjudligiga (yoki soniga) qarab vektor yasalmoqda. TF-IDF kabi murakkabroq vektorlashtirish usullarini qo'llash orqali model samaradorligini oshirish mumkin.
*   **Murakkabroq Modellar:** Perseptron oddiy model. Agar aniqlik qoniqarli bo'lmasa, Logistik Regressiya, Support Vector Machines (SVM) yoki hattoki oddiy neyron tarmoqlar kabi kuchliroq modellarni qo'llash haqida o'ylab ko'rish mumkin.

Ushbu loyiha matnlarni tasniflash va mashinali o'rganish asoslari bilan tanishish uchun yaxshi boshlang'ich nuqtadir.
