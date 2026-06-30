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

**A Game of Strategy, Memory and Bluffing!**

---

## 📋 Contents

1. [Overview](#overview)
2. [Set-up](#set-up)
3. [Game Rules](#game-rules)
4. [Features](#features)
5. [How to Play](#how-to-play)
6. [AI Difficulty Levels](#ai-difficulty-levels)
7. [Game Strategies](#game-strategies)

---

## 🎮 Overview

#52 Card Game is a two-player strategy and bluffing game. It is played with a standard 52-card deck, and the aim is to minimise the number of cards in your hand to achieve the lowest score.

### Key Features
- 🤖 Advanced AI opponent (3 difficulty levels)
- 👥 Two-player mode
- 🎨 Colourful console interface
- 📊 Detailed game statistics
- 🎭 Bluffing mechanism
- 🧠 AI memory system

---

## 💻 Installation

### Requirements
- Python 3.6 or later
- Standard Python libraries (random, time, collections)

### Installation Steps

1. **Save the Python code:**
   - Save the code as `blof_oyunu.py`

2. **Run the game:**
   ```bash
   python blof_oyunu.py
   ```

3. **The game has started!** 🎉

---

## 📖 Game Rules

### 🎴 Preparation

1. **Deck:** A standard 52-card deck is shuffled
2. **Table:** 12 cards are laid face-up on the table
3. **Deal:** Each player is dealt 8 cards

### 🎯 Drawing from the Table

Players take turns drawing cards from the table:
- First round: **1 card each**
- Second round: **2 cards each**
- Third round: **3 cards each**

In total, each player starts the game with 8 + 1 + 2 + 3 = **14 cards**.

### 🃏 Matching Phase

- Players match **cards of the same numerical value** from their hands
- Matched cards (in pairs) are removed from the game
- Example: If there are 2 sevens (7♠ and 7♥), both are discarded
- If a player matches all their cards, **the game ends immediately**

### 🎭 Bluffing Round

The bluffing round lasts for **5 rounds**. In each round:

#### Player Turn:
1. The player selects one of the **remaining single cards** in their hand
2. They ask their opponent for the matching card
*Version: 1.0*
