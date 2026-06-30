# 🎴 #52

**Strateji, Hafıza ve Blöf Oyunu!**

---

## 📋 İçindekiler

1. [Genel Bakış](#genel-bakış)
2. [Kurulum](#kurulum)
3. [Oyun Kuralları](#oyun-kurallari)
4. [Ozellikler](#ozellikler)
5. [Nasil Oynanir](#nasil-oynanir)
6. [AI Zorluk Seviyeleri](#ai-zorluk-seviyeleri)
7. [Oyun Stratejileri](#oyun-stratejileri)

---

## 🎮 Genel Bakış

#52 Kart Oyunu, iki oyunculu bir strateji ve blöf oyunudur. 52 kartlık standart bir deste ile oynanır ve amaç, elinizdeki kartları en aza indirerek en düşük puanı almaktır.

### Ana Özellikler
- 🤖 Gelişmiş AI rakip (3 zorluk seviyesi)
- 👥 İki oyunculu mod
- 🎨 Renkli konsol arayüzü
- 📊 Detaylı oyun istatistikleri
- 🎭 Blöf mekanizması
- 🧠 AI hafıza sistemi

---

## 💻 Kurulum

### Gereksinimler
- Python 3.6 veya üzeri
- Standart Python kütüphaneleri (random, time, collections)

### Kurulum Adımları

1. **Python kodunu kaydedin:**
   - Kodu `blof_oyunu.py` olarak kaydedin

2. **Oyunu çalıştırın:**
   ```bash
   python blof_oyunu.py
   ```

3. **Oyun başladı!** 🎉

---

## 📖 Oyun Kuralları

### 🎴 Hazırlık

1. **Deste:** 52 kartlık standart deste karıştırılır
2. **Zemin:** 12 kart zemine açık olarak dizilir
3. **Dağıtım:** Her oyuncuya 8'er kart dağıtılır

### 🎯 Zeminden Çekim

Oyuncular sırayla zeminden kart çeker:
- İlk tur: **1'er kart**
- İkinci tur: **2'şer kart**
- Üçüncü tur: **3'er kart**

Toplam her oyuncu 8 + 1 + 2 + 3 = **14 kart** ile oyuna başlar.

### 🃏 Eşleştirme Aşaması

- Oyuncular ellerindeki **aynı sayısal değerdeki kartları** eşleştirir
- Eşleşen kartlar (çift sayıda) oyundan çıkarılır
- Örnek: 2 adet 7♠ ve 7♥ varsa, her ikisi de atılır
- Eğer bir oyuncu tüm kartlarını eşleştirirse, **oyun hemen biter**

### 🎭 Blöf Turu

Blöf turu **5 tur** sürer. Her turda:

#### Oyuncu Sırası:
1. Oyuncu, elinde **tek kalan kartlardan** birini seçer
2. Rakipten o kartın eşini ister
3. Rakip 3 seçenek arasından birini yapar:
   - ✅ **Doğru kartı verir**
   - ❌ **Kartı vermez** (blöf - aslında varsa)
   - 🎭 **Yanlış kart verir** (blöf - farklı bir kart)

#### Önemli Notlar:
- Sadece **tek** olan kartların eşi istenebilir
- Kart aldıktan sonra eşleşme kontrolü yapılır
- Yeni eşler varsa otomatik atılır

### 💯 Puanlama

Oyun sonunda kalan kartların değerleri:

| Kart | Puan |
|------|------|
| 2-10 | Kendi değeri |
| Q (Kız) | 10 puan |
| K (Papaz) | 10 puan |
| A (As) | 10 puan |

### 🏆 Kazanma

- **En az puana** sahip oyuncu kazanır
- Beraberlik durumunda oyun berabere biter
- Kartları ilk bitiren otomatik kazanır (0 puan)

---

## ✨ Özellikler

### 🤖 Gelişmiş AI Sistemi

#### Hafıza:
- Oyuncunun istediği kartları hatırlar
- Verilen kartları kaydeder
- Blöf yapılan kartları not alır

#### Strateji:
- Elinde birden fazla olan kartlardan sorar
- Daha önce verilen kartları tekrar ister
- Yüksek puanlı kartları hedefler
- Akıllı blöf kararları verir

### 🎨 Görsel Özellikler

- ✅ Renkli kart sembolleri (♠♥♦♣)
- 📊 İlerleme çubukları
- 🎯 Animasyonlu mesajlar
- 💭 AI düşünce baloncukları
- 📈 Detaylı istatistikler

### 📊 İstatistikler

Oyun sonu istatistikleri:
- Toplam hamle sayısı
- Oyuncu blöf sayıları
- AI doğru söyleme/blöf oranı
- Kalan kart sayıları ve puanlar

---

## 🎮 Nasıl Oynanır

### Ana Menü

Oyun başladığında 4 seçenek sunulur:

```
1. Bilgisayara karşı (AI)
2. İki oyunculu
3. Nasıl Oynanır?
4. Çıkış
```

### 1️⃣ Bilgisayara Karşı (AI Modu)

#### Zorluk Seçimi:
- **Kolay:** AI rastgele oynuyor, %75 dürüst
- **Orta:** Stratejik düşünüyor, bazen blöf yapıyor
- **Zor:** Hafızalı, çok stratejik ve sık blöf yapıyor

#### Oyun Akışı:
1. Kartlar dağıtılır
2. Eşler otomatik atılır
3. Sizin turunuz:
   - Elinizdeki kartlar gösterilir
   - Tek kalan kartlardan birini seçersiniz
   - AI karar verir (ver/verme/blöf)
4. AI'nın turu:
   - AI düşünür ve kart sorar
   - Siz karar verirsiniz:
     - `1`: Kartı ver (doğru)
     - `2`: Kartı verme (blöf)
     - `3`: Yanlış kart ver (blöf)
5. 5 tur veya kartlar bitene kadar devam eder

### 2️⃣ İki Oyunculu Mod

- Her oyuncu sırayla oynuyor
- Kartlar karşı oyuncuya gösterilmiyor
- Oyuncular kendi kararlarını veriyor
- Blöf mekanizması aynı şekilde çalışıyor

### 3️⃣ Nasıl Oynanır?

Detaylı oyun kurallarını gösterir ve ana menüye döner.

---

## 🎯 AI Zorluk Seviyeleri

### 🟢 Kolay Seviye

**Karakteristikler:**
- Rastgele kart seçimi
- %75 ihtimalle doğru söyler
- %25 ihtimalle blöf yapar
- Strateji yok

**Mesajlar:**
```
💭 "Hmm, 7 istesem mi acaba?"
💭 "Şansımı Q ile deneyeyim"
😊 "Evet, 2 adet A vereceğim"
```

### 🟡 Orta Seviye

**Karakteristikler:**
- Hafıza kullanır
- Daha önce verilen kartları hatırlar
- %50 doğru söyler, %50 blöf yapar
- Yüksek puanlı kartları tercih eder

**Mesajlar:**
```
💭 "Daha önce K vermişti, belki hala var..."
😏 "Yok bende 5, başka karttan iste!"
🎭 "Al sana kart!" (Yanlış kart veriyor)
```

### 🔴 Zor Seviye

**Karakteristikler:**
- Gelişmiş hafıza
- Blöf geçmişini takip eder
- Tek kart varsa %70 blöf yapar
- Çok kart varsa %60 doğru söyler
- Stratejik kart seçimi

**Mesajlar:**
```
💭 "Ona blöf yaptığı kartlardan uzak durayım"
😈 "Bende 3 yok!" (Aslında var, saklıyor)
🤔 "Peki, 3 adet Q veriyorum"
```

---

## 💡 Oyun Stratejileri

### 🎯 Genel Stratejiler

1. **Yüksek Puanlı Kartlardan Kurtulun:**
   - J (11), A/K/Q (10) puanlık kartlar öncelikli
   - Düşük puanlı kartları tutun

2. **Blöf Yapın:**
   - Tek kartınızı saklamak için blöf yapın
   - Rakibin yüksek puanlı kartını vermemek için reddedin

3. **Hafızanızı Kullanın:**
   - Rakibin istediği kartları not alın
   - Daha önce verdiği kartları tekrar isteyin

4. **Eş Yapma Şansı:**
   - Elinde olan kartların eşini isteyin
   - Hemen eşleşir ve puanınız düşer

### 🤖 AI'ya Karşı Stratejiler

#### Kolay AI'ya Karşı:
- ✅ Doğru söyler çoğunlukla
- 📝 Rastgele sorar, takip gerekmez
- 🎯 Basit blöf yapın

#### Orta AI'ya Karşı:
- ⚠️ Bazen blöf yapar
- 🧠 Verdiğiniz kartları hatırlar
- 🎭 Stratejik blöf gerekir

#### Zor AI'ya Karşı:
- 🔥 Çok blöf yapar!
- 🧠 Her şeyi hatırlar
- 🎯 Çok dikkatli olun
- 🎭 Karmaşık blöf stratejisi kullanın

### 📊 İpuçları

**✅ Yapılması Gerekenler:**
- Her hamlenizi düşünün
- AI'nın önceki hamlelerini hatırlayın
- Yüksek puanlı kartlardan kurtulun
- Stratejik blöf yapın

**❌ Yapılmaması Gerekenler:**
- Rastgele kart istemeyin
- Her zaman doğru söylemeyin
- Düşük puanlı kartları saklamayın
- AI'nın hafızasını unutmayın

---

## 🎲 Örnek Oyun

### Başlangıç:
```
Oyuncu 1 eli: 7♠, 7♥, K♣, 3♦, 5♠, 5♥, Q♦, A♠, 2♣, 9♥, J♣, 4♦, 8♠, 10♥
```

### Eşleştirme Sonrası:
```
Atılan kartlar: 7♠, 7♥, 5♠, 5♥ (2 çift)
Kalan kartlar: K♣, 3♦, Q♦, A♠, 2♣, 9♥, J♣, 4♦, 8♠, 10♥
```

### Blöf Turu - Tur 1:

**Oyuncu 1:** "Q istiyorum"
**AI:** 😊 "Evet, 1 adet Q veriyorum"
**Sonuç:** Oyuncu 1, Q♦ ve Q♥ eşleştirdi, attı

**AI:** 💭 "Şansımı K ile deneyeyim"
**Oyuncu 1:** Seçim: `1` (Kartı ver)
**Sonuç:** AI, K aldı ve eşleştirdi

### Oyun Sonu:
```
Oyuncu 1: 3♦, 2♣ (5 puan)
AI: J♣, 4♦ (15 puan)

🎉 OYUNCU 1 KAZANDI! 🎉
```

---

## 🐛 Sorun Giderme

### Renkler Görünmüyorsa:
- Windows'ta: `colorama` kütüphanesini yükleyin
- Linux/Mac: Terminal ANSI renklerini desteklemelidir

### Oyun Donuyorsa:
- Ctrl+C ile çıkın
- Python sürümünü kontrol edin (3.6+)

---

## 📝 Notlar

- Oyun tamamen konsolda çalışır
- AI kartları asla gösterilmez
- Her oyun sonunda istatistikler gösterilir
- Tekrar oynamak için menüden seçim yapabilirsiniz

---

## 👨‍💻 Geliştirici Notları

### Kod Yapısı:
```python
class RenkliCikti:  # ANSI renk kodları
class AI:           # Gelişmiş AI sistemi
class KartOyunu:    # Ana oyun mantığı
```

### Önemli Metodlar:
- `deste_olustur()`: 52 kart oluşturur
- `es_ayir()`: Eşleşen kartları bulur
- `kart_sec()`: AI kart seçimi
- `karar_ver()`: AI blöf kararı

---

## 🎉 İyi Oyunlar!

**Bol şans ve başarılar!** 🍀

Oyunu beğendiyseniz arkadaşlarınızla paylaşın! 🎴

---

*Son güncelleme: 2025*
*Sürüm: 1.0*

-----------------------------------------
# 🎴 #52

**AI:** 💭 “I’ll try my luck with the K”
**Player 1:** Choice: `1` (Play the card)
**Result:** The AI took the K and matched it

### End of Game:
```
Player 1: 3♦, 2♣ (5 points)
AI: J♣, 4♦ (15 points)

🎉 PLAYER 1 WON! 🎉
```

---

## 🐛 Troubleshooting

### If Colours Are Not Displayed:
- On Windows: Install the `colorama` library
- On Linux/Mac: Your terminal must support ANSI colours

### If the Game Freezes:
- Exit using Ctrl+C
- Check your Python version (3.6+)

---

## 📝 Notes

- The game runs entirely in the console
- AI cards are never displayed
- Statistics are shown at the end of each game
- You can select to play again from the menu

---

## 👨‍💻 Developer Notes

### Code Structure:
```python
class ColouredOutput:  # ANSI colour codes
class AI:           # Advanced AI system
class CardGame:    # Main game logic
```

### Important Methods:
- `shuffle_deck()`: Shuffles the 52-card deck
- `find_pairs()`: Finds matching cards
- `select_card()`: AI card selection
- `decide()`: AI bluff decision

---

## 🎉 Enjoy the game!

**Good luck and all the best!** 🍀

If you enjoyed the game, share it with your friends! 🎴

---

*Last updated: 2025*
*Version: 1.0*

