import random
import time
from collections import Counter, defaultdict

class RenkliCikti:
    """Renkli konsol çıktıları için ANSI kodları"""
    KIRMIZI = '\033[91m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    MAVI = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    BEYAZ = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

class AI:
    """Gelişmiş AI sistemi - Hafıza ve strateji ile"""
    def __init__(self, zorluk='orta'):
        self.zorluk = zorluk
        self.hafiza_istenen = []
        self.hafiza_verilen = {}
        self.hafiza_blof = []
        self.blof_sayisi = 0
        self.dogru_sayisi = 0
        
    def dusunuyor_animasyon(self):
        """AI düşünüyor animasyonu"""
        mesajlar = [
            "🤔 Stratejimi planlıyorum",
            "🧠 Hafızamı tarayorum",
            "🎯 En iyi hamleyi arıyorum",
            "💭 Düşünüyorum"
        ]
        mesaj = random.choice(mesajlar)
        print(f"{RenkliCikti.CYAN}{mesaj}", end="", flush=True)
        for _ in range(3):
            time.sleep(0.25)
            print(".", end="", flush=True)
        print(f"{RenkliCikti.RESET}")
        time.sleep(0.2)
    
    def oyuncu_kart_istedi(self, deger):
        """Oyuncunun istediği kartı hafızaya kaydet"""
        self.hafiza_istenen.append(deger)
    
    def oyuncu_kart_verdi(self, deger, adet):
        """Oyuncunun verdiği kartları hafızaya kaydet"""
        if deger in self.hafiza_verilen:
            self.hafiza_verilen[deger] += adet
        else:
            self.hafiza_verilen[deger] = adet
    
    def oyuncu_blof_yapti(self, deger):
        """Oyuncunun blöf yaptığını kaydet"""
        self.hafiza_blof.append(deger)
    
    def kart_sec(self, el):
        """AI hangi kartı soracağına karar verir"""
        if not el:
            return None
        
        self.dusunuyor_animasyon()
        
        # Tek olan kartları bul
        deger_sayilari = Counter([k['deger'] for k in el])
        tekler = [d for d, say in deger_sayilari.items() if say == 1]
        
        if not tekler:
            print(f"{RenkliCikti.SARI}💭 \"Tek kart kalmadı...\"{RenkliCikti.RESET}")
            return None
        
        # Zorluk: Kolay - Rastgele seçim
        if self.zorluk == 'kolay':
            secilen = random.choice(tekler)
            print(f"{RenkliCikti.SARI}💭 \"Hmm, {secilen} istesem mi acaba?\"{RenkliCikti.RESET}")
            return secilen
        
        # Orta/Zor: Oyuncunun daha önce verdiği kartlardan sor
        if self.hafiza_verilen and random.random() < (0.7 if self.zorluk == 'zor' else 0.4):
            potansiyel = [d for d in self.hafiza_verilen.keys() if d in tekler]
            if potansiyel:
                secilen = random.choice(potansiyel)
                print(f"{RenkliCikti.SARI}💭 \"Daha önce {secilen} vermişti, belki hala var...\"{RenkliCikti.RESET}")
                return secilen
        
        # Yüksek puanlı kartları tercih et
        if random.random() < 0.3:
            yuksek_puanli = [d for d in tekler if d in ['A', 'K', 'Q', 'J', '10']]
            if yuksek_puanli:
                secilen = random.choice(yuksek_puanli)
                print(f"{RenkliCikti.SARI}💭 \"Yüksek puanlı {secilen} isteyeyim\"{RenkliCikti.RESET}")
                return secilen
        
        # Varsayılan: Rastgele tek karttan
        secilen = random.choice(tekler)
        print(f"{RenkliCikti.SARI}💭 \"Şansımı {secilen} ile deneyeyim\"{RenkliCikti.RESET}")
        return secilen
    
    def karar_ver_verme(self, istenen_deger, oyuncu_eli):
        """AI oyuncudan kart istediğinde, oyuncunun verme/vermeme/blöf kararı"""
        kartlar = [k for k in oyuncu_eli if k['deger'] == istenen_deger]
        
        if not kartlar:
            print(f"{RenkliCikti.CYAN}ℹ️  Elinizde {istenen_deger} yok{RenkliCikti.RESET}")
            return None, 'yok'
        
        print(f"{RenkliCikti.YESIL}Elinizde {len(kartlar)} adet {istenen_deger} var{RenkliCikti.RESET}")
        print(f"1. Kartı ver (doğru)")
        print(f"2. Kartı verme (blöf)")
        print(f"3. Yanlış kart ver (blöf)")
        
        while True:
            secim = input(f"{RenkliCikti.SARI}Seçiminiz (1/2/3): {RenkliCikti.RESET}")
            if secim in ['1', '2', '3']:
                break
            print(f"{RenkliCikti.KIRMIZI}❌ Geçersiz seçim!{RenkliCikti.RESET}")
        
        if secim == '1':
            # Doğru kartı ver
            return kartlar, 'dogru'
        elif secim == '2':
            # Verme
            return None, 'verme'
        else:
            # Yanlış kart ver (blöf)
            yanlis_kartlar = [k for k in oyuncu_eli if k['deger'] != istenen_deger]
            if not yanlis_kartlar:
                print(f"{RenkliCikti.KIRMIZI}Blöf yapacak başka kart yok, vermediniz{RenkliCikti.RESET}")
                return None, 'verme'
            return yanlis_kartlar, 'blof'
    
    def karar_ver(self, istenen_deger, ai_eli):
        """AI kartı verip vermeme kararı verir"""
        kartlar = [k for k in ai_eli if k['deger'] == istenen_deger]
        
        if not kartlar:
            print(f"{RenkliCikti.CYAN}ℹ️  \"Bende {istenen_deger} yok!\"{RenkliCikti.RESET}")
            return None, 'yok'
        
        # Zorluk: Kolay - Çoğunlukla doğru söyler
        if self.zorluk == 'kolay':
            if random.random() < 0.75:
                self.dogru_sayisi += 1
                print(f"{RenkliCikti.YESIL}😊 \"Evet, {len(kartlar)} adet {istenen_deger} vereceğim\"{RenkliCikti.RESET}")
                return kartlar, 'dogru'
            else:
                self.blof_sayisi += 1
                # Bazen yanlış kart verir, bazen vermez
                if random.random() < 0.5:
                    yanlis_kartlar = [k for k in ai_eli if k['deger'] != istenen_deger]
                    if yanlis_kartlar:
                        print(f"{RenkliCikti.KIRMIZI}😏 \"İşte kart!\" (Ama yanlış kart veriyor){RenkliCikti.RESET}")
                        return [random.choice(yanlis_kartlar)], 'blof'
                print(f"{RenkliCikti.KIRMIZI}🤷 \"Maalesef {istenen_deger} yok\"{RenkliCikti.RESET}")
                return None, 'verme'
        
        # Zorluk: Orta - Stratejik blöf
        if self.zorluk == 'orta':
            rand = random.random()
            if rand < 0.5:
                self.dogru_sayisi += 1
                print(f"{RenkliCikti.YESIL}😊 \"Tamam, {len(kartlar)} adet {istenen_deger} veriyorum\"{RenkliCikti.RESET}")
                return kartlar, 'dogru'
            elif rand < 0.75:
                self.blof_sayisi += 1
                print(f"{RenkliCikti.KIRMIZI}😏 \"Yok bende {istenen_deger}!\"{RenkliCikti.RESET}")
                return None, 'verme'
            else:
                self.blof_sayisi += 1
                yanlis_kartlar = [k for k in ai_eli if k['deger'] != istenen_deger]
                if yanlis_kartlar:
                    print(f"{RenkliCikti.KIRMIZI}🎭 \"Al sana kart!\" (Yanlış kart veriyor){RenkliCikti.RESET}")
                    return [random.choice(yanlis_kartlar)], 'blof'
                print(f"{RenkliCikti.KIRMIZI}😏 \"Yok bende!\"{RenkliCikti.RESET}")
                return None, 'verme'
        
        # Zorluk: Zor - Çok stratejik
        if self.zorluk == 'zor':
            rand = random.random()
            if len(kartlar) == 1:
                if rand < 0.7:
                    self.blof_sayisi += 1
                    if random.random() < 0.6:
                        yanlis_kartlar = [k for k in ai_eli if k['deger'] != istenen_deger]
                        if yanlis_kartlar:
                            print(f"{RenkliCikti.KIRMIZI}😈 \"İşte {istenen_deger}!\" (Ama aslında farklı kart){RenkliCikti.RESET}")
                            return [random.choice(yanlis_kartlar)], 'blof'
                    print(f"{RenkliCikti.KIRMIZI}😈 \"Bende {istenen_deger} yok!\"{RenkliCikti.RESET}")
                    return None, 'verme'
                else:
                    self.dogru_sayisi += 1
                    print(f"{RenkliCikti.YESIL}😊 \"Tamam veriyorum ama tek var!\"{RenkliCikti.RESET}")
                    return kartlar, 'dogru'
            else:
                if rand < 0.4:
                    self.blof_sayisi += 1
                    print(f"{RenkliCikti.KIRMIZI}🎭 \"Hiç {istenen_deger} yok elimde!\"{RenkliCikti.RESET}")
                    return None, 'verme'
                else:
                    self.dogru_sayisi += 1
                    print(f"{RenkliCikti.YESIL}🤔 \"Peki, {len(kartlar)} adet {istenen_deger} veriyorum\"{RenkliCikti.RESET}")
                    return kartlar, 'dogru'
        
        return kartlar, 'dogru'

class KartOyunu:
    def __init__(self):
        self.deste = []
        self.zemin = []
        self.oyuncu1_el = []
        self.oyuncu2_el = []
        self.oyuncu1_atilan = []
        self.oyuncu2_atilan = []
        self.oyun_modu = None
        self.ai = None
        self.istatistik = {
            'oyuncu1_kazanma': 0,
            'oyuncu2_kazanma': 0,
            'oyuncu1_blof': 0,
            'oyuncu2_blof': 0,
            'toplam_hamle': 0
        }
        
    def ascii_banner(self):
        """Oyun başlangıç banner'ı"""
        banner = f"""
{RenkliCikti.MAGENTA}{RenkliCikti.BOLD}
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║        🎴        #52        🎴                        ║
║                                                       ║
║        Strateji, Hafıza ve Blöf Oyunu!                ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
{RenkliCikti.RESET}
"""
        print(banner)
        time.sleep(1)
    
    def nasil_oynanir(self):
        """Oyun kurallarını göster"""
        print(f"\n{RenkliCikti.BOLD}{RenkliCikti.CYAN}{'='*70}{RenkliCikti.RESET}")
        print(f"{RenkliCikti.BOLD}{RenkliCikti.CYAN}📖 OYUN KURALLARI{RenkliCikti.RESET}")
        print(f"{RenkliCikti.CYAN}{'='*70}{RenkliCikti.RESET}\n")
        
        kurallar = """
🎴 HAZIRLIK:
   • 52 kartlık deste karıştırılır
   • Zemine 12 kart dizilir
   • İki oyuncuya geri kalan desteden sekizer kart dağıtılır
   
🎯 ZEMINDEN ÇEKİM:
   • Zeminde dizili olan kartlar sırasıyla birer, ikişer ve üçer olarak çekilir
   
🃏 EŞLEŞTİRME:
   • Oyuncular ellerindeki aynı sayısal değerdeki kartları eşleştirip 
     oyundan çıkarır
   • Eğer bir oyuncu tüm kartlarının eşini bulduysa oyun blöf turuna 
     geçmeden biter
   
🎭 BLÖF TURU:
   • Oyuncular karşı tarafın ellerindeki eşleri tahmin ederek kart 
     almaya çalışır
   • Rakip kartı verir, blöf yapar ya da kart yok der
   • Oyun 5 tur sürer
   
💯 PUANLAMA:
   • Tur sonunda ellerindeki kartların puanları hesaplanır
   • Sayısal kartlar: Kendi değeri (2-10)
   • Özel kartlar (Q, K, A): 10 puan
   • J kartı: 11 puan
   
🏆 KAZANMA:
   • En az puana sahip oyuncu kazanır
   • Oyun blöf ve strateji içerir
   • Amaç kartları azaltmaktır
"""
        print(f"{RenkliCikti.YESIL}{kurallar}{RenkliCikti.RESET}")
        print(f"{RenkliCikti.CYAN}{'='*70}{RenkliCikti.RESET}\n")
        input(f"{RenkliCikti.SARI}Ana menüye dönmek için Enter'a basın...{RenkliCikti.RESET}")
    
    def ilerleme_cubugu(self, oran, genislik=30):
        """İlerleme çubuğu göster"""
        dolu = int(genislik * oran)
        bos = genislik - dolu
        bar = "█" * dolu + "░" * bos
        yuzde = int(oran * 100)
        return f"[{RenkliCikti.YESIL}{bar}{RenkliCikti.RESET}] {yuzde}%"
    
    def deste_olustur(self):
        """52'lik iskambil destesi oluşturur"""
        semboller = ['♠', '♥', '♦', '♣']
        degerler = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deste = [{'deger': d, 'sembol': s} for s in semboller for d in degerler]
        random.shuffle(self.deste)
    
    def kart_puani(self, kart):
        """Kartın puan değerini döndürür"""
        if kart['deger'] in ['A', 'K', 'Q']:
            return 10
        elif kart['deger'] == 'J':
            return 11
        return int(kart['deger'])
    
    def kart_goster(self, kart):
        """Kartı renkli gösterir"""
        sembol = kart['sembol']
        deger = kart['deger']
        if sembol in ['♥', '♦']:
            return f"{RenkliCikti.KIRMIZI}{deger}{sembol}{RenkliCikti.RESET}"
        else:
            return f"{RenkliCikti.BEYAZ}{deger}{sembol}{RenkliCikti.RESET}"
    
    def el_goster(self, kartlar):
        """El kartlarını renkli gösterir"""
        return ', '.join([self.kart_goster(k) for k in kartlar])
    
    def zemin_dagit(self):
        """Zemine 12 kart dizer"""
        print(f"\n{RenkliCikti.CYAN}📋 Zemine 12 kart diziliyor...{RenkliCikti.RESET}")
        self.zemin = [self.deste.pop() for _ in range(12)]
        print(f"{RenkliCikti.MAVI}Zemin: {self.el_goster(self.zemin)}{RenkliCikti.RESET}")
        time.sleep(1)
    
    def ilk_dagitim(self):
        """Her oyuncuya 8'er kart dağıtır"""
        print(f"\n{RenkliCikti.CYAN}🎴 Her oyuncuya 8'er kart dağıtılıyor...{RenkliCikti.RESET}")
        time.sleep(0.5)
        self.oyuncu1_el = [self.deste.pop() for _ in range(8)]
        self.oyuncu2_el = [self.deste.pop() for _ in range(8)]
        print(f"{RenkliCikti.YESIL}✓ Dağıtım tamamlandı!{RenkliCikti.RESET}")
        time.sleep(0.5)
    
    def zeminden_cek(self):
        """Oyuncular sırayla zeminden 1'er, 2'şer, 3'er kart çeker"""
        print(f"\n{RenkliCikti.CYAN}🎯 Oyuncular zeminden kart çekiyor...{RenkliCikti.RESET}")
        
        # 1'er kart
        print(f"{RenkliCikti.SARI}  → Oyuncular 1'er kart çekti{RenkliCikti.RESET}")
        if self.zemin:
            self.oyuncu1_el.append(self.zemin.pop(0))
        if self.zemin:
            self.oyuncu2_el.append(self.zemin.pop(0))
        time.sleep(0.3)
        
        # 2'şer kart
        print(f"{RenkliCikti.SARI}  → Oyuncular 2'şer kart çekti{RenkliCikti.RESET}")
        for _ in range(2):
            if self.zemin:
                self.oyuncu1_el.append(self.zemin.pop(0))
        for _ in range(2):
            if self.zemin:
                self.oyuncu2_el.append(self.zemin.pop(0))
        time.sleep(0.3)
        
        # 3'er kart
        print(f"{RenkliCikti.SARI}  → Oyuncular 3'er kart çekti{RenkliCikti.RESET}")
        for _ in range(3):
            if self.zemin:
                self.oyuncu1_el.append(self.zemin.pop(0))
        for _ in range(3):
            if self.zemin:
                self.oyuncu2_el.append(self.zemin.pop(0))
        time.sleep(0.3)
        
        print(f"{RenkliCikti.YESIL}✓ Çekim tamamlandı!{RenkliCikti.RESET}")
        time.sleep(0.5)
    
    def es_ayir(self, el):
        """Eldeki eş kartları bulur ve ayırır (tüm eşler çıkarılır)"""
        deger_sayilari = Counter([k['deger'] for k in el])
        atilacaklar = []
        yeni_el = []
        
        for kart in el:
            if deger_sayilari[kart['deger']] >= 2 and kart['deger'] not in [k['deger'] for k in atilacaklar]:
                ayni_deger = [k for k in el if k['deger'] == kart['deger']]
                # Çift sayıda kartı at (2, 4, 6...)
                cift_sayi = (len(ayni_deger) // 2) * 2
                atilacaklar.extend(ayni_deger[:cift_sayi])
            elif kart not in atilacaklar:
                yeni_el.append(kart)
        
        return yeni_el, atilacaklar
    
    def es_kontrol_ve_ayir(self, oyuncu):
        """Belirtilen oyuncunun elindeki eşleri kontrol eder ve ayırır"""
        if oyuncu == 1:
            self.oyuncu1_el, atilan = self.es_ayir(self.oyuncu1_el)
            self.oyuncu1_atilan.extend(atilan)
            return atilan
        else:
            self.oyuncu2_el, atilan = self.es_ayir(self.oyuncu2_el)
            self.oyuncu2_atilan.extend(atilan)
            return atilan
    
    def durum_goster(self, tur):
        """Oyun durumunu güzel bir şekilde göster"""
        print(f"\n{RenkliCikti.BOLD}{RenkliCikti.CYAN}{'='*60}{RenkliCikti.RESET}")
        print(f"{RenkliCikti.BOLD}{RenkliCikti.CYAN}TUR {tur}/5 - OYUN DURUMU{RenkliCikti.RESET}")
        print(f"{RenkliCikti.CYAN}{'='*60}{RenkliCikti.RESET}")
        
        # Oyuncu 1
        puan1 = self.toplam_puan(self.oyuncu1_el)
        kart_sayisi1 = len(self.oyuncu1_el)
        oran1 = kart_sayisi1 / 14 if kart_sayisi1 <= 14 else 1
        print(f"\n{RenkliCikti.YESIL}👤 OYUNCU 1:{RenkliCikti.RESET}")
        print(f"   Kart Sayısı: {kart_sayisi1} | Puan: {puan1}")
        print(f"   {self.ilerleme_cubugu(oran1)}")
        
        # Oyuncu 2
        puan2 = self.toplam_puan(self.oyuncu2_el)
        kart_sayisi2 = len(self.oyuncu2_el)
        oran2 = kart_sayisi2 / 14 if kart_sayisi2 <= 14 else 1
        oyuncu2_isim = "🤖 AI" if self.oyun_modu == 1 else "👤 OYUNCU 2"
        print(f"\n{RenkliCikti.MAGENTA}{oyuncu2_isim}:{RenkliCikti.RESET}")
        print(f"   Kart Sayısı: {kart_sayisi2} | Puan: {puan2}")
        print(f"   {self.ilerleme_cubugu(oran2)}")
        
        # AI İstatistikleri
        if self.oyun_modu == 1 and self.ai:
            print(f"\n{RenkliCikti.SARI}📊 AI İstatistikleri:{RenkliCikti.RESET}")
            print(f"   Doğru söyleme: {self.ai.dogru_sayisi} | Blöf: {self.ai.blof_sayisi}")
        
        print(f"{RenkliCikti.CYAN}{'='*60}{RenkliCikti.RESET}\n")
    
    def toplam_puan(self, el):
        """Eldeki kartların toplam puanını hesaplar"""
        return sum([self.kart_puani(k) for k in el])
    
    def oyun_bitir(self):
        """Oyunu bitirir ve kazananı belirler"""
        puan1 = self.toplam_puan(self.oyuncu1_el)
        puan2 = self.toplam_puan(self.oyuncu2_el)
        
        print(f"\n{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}{'='*60}{RenkliCikti.RESET}")
        print(f"{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}🏁 OYUN BİTTİ! 🏁{RenkliCikti.RESET}")
        print(f"{RenkliCikti.MAGENTA}{'='*60}{RenkliCikti.RESET}\n")
        
        print(f"{RenkliCikti.YESIL}👤 OYUNCU 1:{RenkliCikti.RESET}")
        print(f"   Kalan Kartlar ({len(self.oyuncu1_el)}): {self.el_goster(self.oyuncu1_el)}")
        print(f"   {RenkliCikti.BOLD}Toplam Puan: {puan1}{RenkliCikti.RESET}")
        
        oyuncu2_isim = "🤖 AI" if self.oyun_modu == 1 else "👤 OYUNCU 2"
        print(f"\n{RenkliCikti.MAGENTA}{oyuncu2_isim}:{RenkliCikti.RESET}")
        print(f"   Kalan Kartlar ({len(self.oyuncu2_el)}): {self.el_goster(self.oyuncu2_el)}")
        print(f"   {RenkliCikti.BOLD}Toplam Puan: {puan2}{RenkliCikti.RESET}")
        
        # İstatistikler
        print(f"\n{RenkliCikti.CYAN}📊 OYUN İSTATİSTİKLERİ:{RenkliCikti.RESET}")
        print(f"   Toplam Hamle: {self.istatistik['toplam_hamle']}")
        print(f"   Oyuncu 1 Blöf: {self.istatistik['oyuncu1_blof']}")
        print(f"   Oyuncu 2 Blöf: {self.istatistik['oyuncu2_blof']}")
        
        # Kazanan
        print(f"\n{RenkliCikti.BOLD}{RenkliCikti.SARI}{'─'*60}{RenkliCikti.RESET}")
        if puan1 < puan2:
            print(f"{RenkliCikti.BOLD}{RenkliCikti.YESIL}🎉🎉🎉 OYUNCU 1 KAZANDI! 🎉🎉🎉{RenkliCikti.RESET}")
            self.istatistik['oyuncu1_kazanma'] += 1
        elif puan2 < puan1:
            print(f"{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}🎉🎉🎉 {oyuncu2_isim} KAZANDI! 🎉🎉🎉{RenkliCikti.RESET}")
            self.istatistik['oyuncu2_kazanma'] += 1
        else:
            print(f"{RenkliCikti.BOLD}{RenkliCikti.CYAN}🤝🤝🤝 BERABERE! 🤝🤝🤝{RenkliCikti.RESET}")
        print(f"{RenkliCikti.SARI}{'─'*60}{RenkliCikti.RESET}\n")
    
    def oyun_oyna(self):
        """Ana oyun döngüsü"""
        # Oyun hazırlığı
        print(f"\n{RenkliCikti.BOLD}{RenkliCikti.CYAN}🎮 OYUN HAZIRLANIYOR...{RenkliCikti.RESET}\n")
        time.sleep(0.5)
        
        print(f"{RenkliCikti.CYAN}🃏 Deste karıştırılıyor...{RenkliCikti.RESET}")
        self.deste_olustur()
        time.sleep(0.5)
        
        self.zemin_dagit()
        self.ilk_dagitim()
        self.zeminden_cek()
        
        print(f"\n{RenkliCikti.CYAN}🔍 Eş kartlar ayırılıyor...{RenkliCikti.RESET}")
        atilan1 = self.es_kontrol_ve_ayir(1)
        atilan2 = self.es_kontrol_ve_ayir(2)
        
        if atilan1:
            print(f"{RenkliCikti.YESIL}✓ Oyuncu 1 şu kartları attı: {self.el_goster(atilan1)}{RenkliCikti.RESET}")
        if atilan2:
            oyuncu2_isim = "AI" if self.oyun_modu == 1 else "Oyuncu 2"
            print(f"{RenkliCikti.MAGENTA}✓ {oyuncu2_isim} şu kartları attı: {self.el_goster(atilan2)}{RenkliCikti.RESET}")
        
        # Biri tüm kartlarını attı mı kontrol
        if not self.oyuncu1_el:
            print(f"\n{RenkliCikti.YESIL}🎉 Oyuncu 1 tüm kartlarını eşleştirdi! Oyun bitti!{RenkliCikti.RESET}")
            self.oyun_bitir()
            return
        if not self.oyuncu2_el:
            oyuncu2_isim = "AI" if self.oyun_modu == 1 else "Oyuncu 2"
            print(f"\n{RenkliCikti.MAGENTA}🎉 {oyuncu2_isim} tüm kartlarını eşleştirdi! Oyun bitti!{RenkliCikti.RESET}")
            self.oyun_bitir()
            return
        
        time.sleep(1)
        
        # Blöf turları
        print(f"\n{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}{'='*60}{RenkliCikti.RESET}")
        print(f"{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}🎭 BLÖF TURLARI BAŞLIYOR! 🎭{RenkliCikti.RESET}")
        print(f"{RenkliCikti.MAGENTA}{'='*60}{RenkliCikti.RESET}\n")
        time.sleep(1)
        
        for tur in range(5):
            self.durum_goster(tur + 1)
            
            # Oyuncu 1'in turu
            if self.oyuncu1_el:
                print(f"{RenkliCikti.BOLD}{RenkliCikti.YESIL}👤 OYUNCU 1'İN SIRASI{RenkliCikti.RESET}")
                print(f"{RenkliCikti.YESIL}{'─'*40}{RenkliCikti.RESET}")
                print(f"Elinizdeki kartlar: {self.el_goster(self.oyuncu1_el)}")
                
                # Sadece tek olan kartları göster
                deger_sayilari = Counter([k['deger'] for k in self.oyuncu1_el])
                tekler = [d for d, say in deger_sayilari.items() if say == 1]
                
                if not tekler:
                    print(f"{RenkliCikti.CYAN}ℹ️  Tek kart kalmadı, sıra geçiliyor{RenkliCikti.RESET}")
                else:
                    print(f"{RenkliCikti.SARI}Tek kalan kartlar: {', '.join(tekler)}{RenkliCikti.RESET}")
                    
                    while True:
                        istenen = input(f"\n{RenkliCikti.SARI}Hangi kartı istiyorsunuz? {RenkliCikti.RESET}").upper()
                        if istenen in tekler:
                            break
                        print(f"{RenkliCikti.KIRMIZI}❌ Sadece tek kalan kartlardan seçebilirsiniz!{RenkliCikti.RESET}")
                    
                    # AI'ya bildir
                    if self.ai:
                        self.ai.oyuncu_kart_istedi(istenen)
                    
                    self.istatistik['toplam_hamle'] += 1
                    
                    if self.oyun_modu == 1:
                        # AI'dan istiyor
                        if self.ai and hasattr(self.ai, 'karar_ver'):
                            kartlar, durum = self.ai.karar_ver(istenen, self.oyuncu2_el)
                        else:
                            # Fallback: eğer ai yoksa otomatik olarak doğru kartları ver (varsa)
                            kartlar = [k for k in self.oyuncu2_el if k['deger'] == istenen]
                            durum = 'dogru' if kartlar else 'yok'
                        
                        if durum == 'dogru':
                            # Güvenlik kontrolü: kartlar None olabilir, o yüzden önce doğrula
                            if kartlar:
                                for k in list(kartlar):
                                    self.oyuncu2_el.remove(k)
                                    self.oyuncu1_el.append(k)
                                if self.ai:
                                    self.ai.oyuncu_kart_verdi(istenen, len(kartlar))
                                print(f"{RenkliCikti.YESIL}✓ {len(kartlar)} adet {istenen} aldınız!{RenkliCikti.RESET}")
                                
                                atilan = self.es_kontrol_ve_ayir(1)
                                if atilan:
                                    print(f"{RenkliCikti.YESIL}🎯 Eş kartları attınız: {self.el_goster(atilan)}{RenkliCikti.RESET}")
                            else:
                                # AI 'dogru' dedi ama kartlar None veya boş döndü
                                print(f"{RenkliCikti.KIRMIZI}⚠️ AI {istenen} olduğunu söyledi fakat hiç kart vermedi!{RenkliCikti.RESET}")
                        elif durum == 'blof':
                            # AI yanlış kart verdi (kartlar None olabileceği için kontrol et)
                            if kartlar:
                                for k in list(kartlar):
                                    self.oyuncu2_el.remove(k)
                                    self.oyuncu1_el.append(k)
                                self.istatistik['oyuncu2_blof'] += 1
                                print(f"{RenkliCikti.KIRMIZI}⚠️  AI blöf yaptı! {self.kart_goster(kartlar[0])} aldınız ama {istenen} değil!{RenkliCikti.RESET}")
                                
                                atilan = self.es_kontrol_ve_ayir(1)
                                if atilan:
                                    print(f"{RenkliCikti.YESIL}🎯 Eş kartları attınız: {self.el_goster(atilan)}{RenkliCikti.RESET}")
                            else:
                                # AI blöf dedi ama kart vermedi; uygun bir mesaj göster ve blöf sayısını arttır
                                self.istatistik['oyuncu2_blof'] += 1
                                print(f"{RenkliCikti.KIRMIZI}⚠️  AI blöf yaptı ama kart vermedi!{RenkliCikti.RESET}")
                    else:
                        # 2 oyunculu mod
                        kartlar, durum = self.ai.karar_ver_verme(istenen, self.oyuncu2_el) if self.ai else (None, 'yok')
                        
                        # Manuel oyunda oyuncu 2 karar veriyor
                        kartlar_mevcut = [k for k in self.oyuncu2_el if k['deger'] == istenen]
                        if kartlar_mevcut:
                            print(f"\n{RenkliCikti.MAGENTA}Oyuncu 2, elinizde {len(kartlar_mevcut)} adet {istenen} var{RenkliCikti.RESET}")
                            print(f"1. Kartı ver (doğru)")
                            print(f"2. Kartı verme (blöf)")
                            print(f"3. Yanlış kart ver (blöf)")
                            
                            while True:
                                secim = input(f"{RenkliCikti.SARI}Seçiminiz (1/2/3): {RenkliCikti.RESET}")
                                if secim in ['1', '2', '3']:
                                    break
                            
                            if secim == '1':
                                for k in kartlar_mevcut:
                                    self.oyuncu2_el.remove(k)
                                    self.oyuncu1_el.append(k)
                                print(f"{RenkliCikti.YESIL}✓ Oyuncu 1, {len(kartlar_mevcut)} adet {istenen} aldı{RenkliCikti.RESET}")
                                
                                atilan = self.es_kontrol_ve_ayir(1)
                                if atilan:
                                    print(f"{RenkliCikti.YESIL}🎯 Oyuncu 1 eş kartları attı: {self.el_goster(atilan)}{RenkliCikti.RESET}")
                            elif secim == '3':
                                yanlis = [k for k in self.oyuncu2_el if k['deger'] != istenen]
                                if yanlis:
                                    verilen = yanlis[0]
                                    self.oyuncu2_el.remove(verilen)
                                    self.oyuncu1_el.append(verilen)
                                    self.istatistik['oyuncu2_blof'] += 1
                                    print(f"{RenkliCikti.KIRMIZI}✗ Oyuncu 2 blöf yaptı! Yanlış kart verdi: {self.kart_goster(verilen)}{RenkliCikti.RESET}")
                                    
                                    atilan = self.es_kontrol_ve_ayir(1)
                                    if atilan:
                                        print(f"{RenkliCikti.YESIL}🎯 Oyuncu 1 eş kartları attı: {self.el_goster(atilan)}{RenkliCikti.RESET}")
                                else:
                                    print(f"{RenkliCikti.CYAN}Blöf yapacak kart yok{RenkliCikti.RESET}")
                            else:
                                self.istatistik['oyuncu2_blof'] += 1
                                print(f"{RenkliCikti.KIRMIZI}✗ Oyuncu 2 kartı vermedi (blöf){RenkliCikti.RESET}")
                        else:
                            print(f"{RenkliCikti.CYAN}ℹ️  Oyuncu 2'de gerçekten {istenen} yok{RenkliCikti.RESET}")
            
            # Oyun bitti mi kontrol
            if not self.oyuncu1_el or not self.oyuncu2_el:
                self.oyun_bitir()
                return
            
            time.sleep(1)
            
            # Oyuncu 2'nin turu
            if self.oyuncu2_el:
                print(f"\n{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}{'─'*60}{RenkliCikti.RESET}")
                oyuncu2_isim = "🤖 AI" if self.oyun_modu == 1 else "👤 OYUNCU 2"
                print(f"{RenkliCikti.BOLD}{RenkliCikti.MAGENTA}{oyuncu2_isim}'NİN SIRASI{RenkliCikti.RESET}")
                print(f"{RenkliCikti.MAGENTA}{'─'*40}{RenkliCikti.RESET}")
                
                if self.oyun_modu == 1:
                    # AI soruyor
                    if not self.ai:
                        # Safeguard: AI nesnesi beklenmedik şekilde None ise hatayı önle
                        print(f"{RenkliCikti.CYAN}ℹ️  AI hazır değil, sıra geçiliyor{RenkliCikti.RESET}")
                        istenen = None
                    else:
                        istenen = self.ai.kart_sec(self.oyuncu2_el)
                    if not istenen:
                        print(f"{RenkliCikti.CYAN}ℹ️  AI'da tek kart kalmadı, sıra geçiliyor{RenkliCikti.RESET}")
                    else:
                        print(f"{RenkliCikti.MAGENTA}AI '{istenen}' kartını istiyor...{RenkliCikti.RESET}\n")
                        time.sleep(0.5)
                        
                        self.istatistik['toplam_hamle'] += 1
                        
                        # Safeguard: only call karar_ver_verme if ai exists and provides the method
                        if self.ai and hasattr(self.ai, 'karar_ver_verme'):
                            kartlar, durum = self.ai.karar_ver_verme(istenen, self.oyuncu1_el)
                        else:
                            # Fallback: no AI available -> opponent says 'yok'
                            kartlar, durum = (None, 'yok')
                        
                        if durum == 'dogru':
                            # Güvenlik: kartlar None veya tek bir dict olabilir; iterable hale getir
                            if not kartlar:
                                print(f"{RenkliCikti.KIRMIZI}⚠️ AI {istenen} olduğunu söyledi fakat hiç kart vermedi!{RenkliCikti.RESET}")
                            else:
                                if isinstance(kartlar, dict):
                                    kartlar = [kartlar]
                                # Kopya liste ile iterasyon, yalnızca mevcut kartları çıkar
                                for k in list(kartlar):
                                    if k in self.oyuncu1_el:
                                        self.oyuncu1_el.remove(k)
                                        self.oyuncu2_el.append(k)
                                print(f"{RenkliCikti.MAGENTA}✓ AI {len(kartlar)} adet {istenen} aldı!{RenkliCikti.RESET}")
                                
                                atilan = self.es_kontrol_ve_ayir(2)
                                if atilan:
                                    print(f"{RenkliCikti.MAGENTA}🎯 AI eş kartları attı{RenkliCikti.RESET}")
                        elif durum == 'blof':
                            # Yanlış kart verdiniz
                            if kartlar and len(kartlar) > 0:
                                secilen = kartlar[0]
                                self.oyuncu1_el.remove(secilen)
                                self.oyuncu2_el.append(secilen)
                                self.istatistik['oyuncu1_blof'] += 1
                                print(f"{RenkliCikti.KIRMIZI}😏 Blöf yaptınız! {self.kart_goster(secilen)} verdiniz{RenkliCikti.RESET}")
                                if self.ai:
                                    self.ai.oyuncu_blof_yapti(istenen)
                                
                                atilan = self.es_kontrol_ve_ayir(2)
                                if atilan:
                                    print(f"{RenkliCikti.MAGENTA}🎯 AI eş kartları attı{RenkliCikti.RESET}")
                            else:
                                # Oyuncu blöf dedi ama kart vermedi
                                self.istatistik['oyuncu1_blof'] += 1
                                if self.ai:
                                    self.ai.oyuncu_blof_yapti(istenen)
                                print(f"{RenkliCikti.KIRMIZI}😏 Blöf yaptınız! Kart vermediniz{RenkliCikti.RESET}")
                        elif durum == 'verme':
                            self.istatistik['oyuncu1_blof'] += 1
                            if self.ai:
                                self.ai.oyuncu_blof_yapti(istenen)
                            print(f"{RenkliCikti.KIRMIZI}😏 Blöf yaptınız! Kart vermediniz{RenkliCikti.RESET}")
                else:
                    # 2 oyunculu mod - Oyuncu 2 soruyor
                    print(f"Elinizdeki kartlar: {self.el_goster(self.oyuncu2_el)}")
                    
                    deger_sayilari = Counter([k['deger'] for k in self.oyuncu2_el])
                    tekler = [d for d, say in deger_sayilari.items() if say == 1]
                    
                    if not tekler:
                        print(f"{RenkliCikti.CYAN}ℹ️  Tek kart kalmadı, sıra geçiliyor{RenkliCikti.RESET}")
                    else:
                        print(f"{RenkliCikti.SARI}Tek kalan kartlar: {', '.join(tekler)}{RenkliCikti.RESET}")
                        
                        while True:
                            istenen = input(f"\n{RenkliCikti.SARI}Hangi kartı istiyorsunuz? {RenkliCikti.RESET}").upper()
                            if istenen in tekler:
                                break
                            print(f"{RenkliCikti.KIRMIZI}❌ Sadece tek kalan kartlardan seçebilirsiniz!{RenkliCikti.RESET}")
                        
                        self.istatistik['toplam_hamle'] += 1
                        
                        kartlar_mevcut = [k for k in self.oyuncu1_el if k['deger'] == istenen]
                        if kartlar_mevcut:
                            print(f"\n{RenkliCikti.YESIL}Oyuncu 1, elinizde {len(kartlar_mevcut)} adet {istenen} var{RenkliCikti.RESET}")
                            print(f"1. Kartı ver (doğru)")
                            print(f"2. Kartı verme (blöf)")
                            print(f"3. Yanlış kart ver (blöf)")
                            
                            while True:
                                secim = input(f"{RenkliCikti.SARI}Seçiminiz (1/2/3): {RenkliCikti.RESET}")
                                if secim in ['1', '2', '3']:
                                    break
                            
                            if secim == '1':
                                for k in kartlar_mevcut:
                                    self.oyuncu1_el.remove(k)
                                    self.oyuncu2_el.append(k)
                                print(f"{RenkliCikti.MAGENTA}✓ Oyuncu 2, {len(kartlar_mevcut)} adet {istenen} aldı{RenkliCikti.RESET}")
                                
                                atilan = self.es_kontrol_ve_ayir(2)
                                if atilan:
                                    print(f"{RenkliCikti.MAGENTA}🎯 Oyuncu 2 eş kartları attı: {self.el_goster(atilan)}{RenkliCikti.RESET}")
                            elif secim == '3':
                                yanlis = [k for k in self.oyuncu1_el if k['deger'] != istenen]
                                if yanlis:
                                    verilen = yanlis[0]
                                    self.oyuncu1_el.remove(verilen)
                                    self.oyuncu2_el.append(verilen)
                                    self.istatistik['oyuncu1_blof'] += 1
                                    print(f"{RenkliCikti.KIRMIZI}✗ Oyuncu 1 blöf yaptı! Yanlış kart verdi: {self.kart_goster(verilen)}{RenkliCikti.RESET}")
                                    
                                    atilan = self.es_kontrol_ve_ayir(2)
                                    if atilan:
                                        print(f"{RenkliCikti.MAGENTA}🎯 Oyuncu 2 eş kartları attı: {self.el_goster(atilan)}{RenkliCikti.RESET}")
                                else:
                                    print(f"{RenkliCikti.CYAN}Blöf yapacak kart yok{RenkliCikti.RESET}")
                            else:
                                self.istatistik['oyuncu1_blof'] += 1
                                print(f"{RenkliCikti.KIRMIZI}✗ Oyuncu 1 kartı vermedi (blöf){RenkliCikti.RESET}")
                        else:
                            print(f"{RenkliCikti.CYAN}ℹ️  Oyuncu 1'de gerçekten {istenen} yok{RenkliCikti.RESET}")
            
            # Oyun bitti mi kontrol
            if not self.oyuncu1_el or not self.oyuncu2_el:
                self.oyun_bitir()
                return
            
            time.sleep(1)
        
        # 5 tur bitti, puanlama
        self.oyun_bitir()
    
    def basla(self):
        """Ana menü ve oyunu başlatır"""
        while True:
            self.ascii_banner()
            
            # Ana menü
            print(f"{RenkliCikti.CYAN}Ana Menü:{RenkliCikti.RESET}")
            print(f"  {RenkliCikti.YESIL}1.{RenkliCikti.RESET} Bilgisayara karşı (AI)")
            print(f"  {RenkliCikti.MAVI}2.{RenkliCikti.RESET} İki oyunculu")
            print(f"  {RenkliCikti.SARI}3.{RenkliCikti.RESET} Nasıl Oynanır?")
            print(f"  {RenkliCikti.KIRMIZI}4.{RenkliCikti.RESET} Çıkış")
            
            while True:
                try:
                    secim = int(input(f"\n{RenkliCikti.SARI}Seçiminiz (1/2/3/4): {RenkliCikti.RESET}"))
                    if secim in [1, 2, 3, 4]:
                        break
                    print(f"{RenkliCikti.KIRMIZI}❌ Lütfen 1, 2, 3 veya 4 girin!{RenkliCikti.RESET}")
                except:
                    print(f"{RenkliCikti.KIRMIZI}❌ Geçersiz giriş!{RenkliCikti.RESET}")
            
            if secim == 3:
                self.nasil_oynanir()
                continue
            elif secim == 4:
                print(f"\n{RenkliCikti.MAGENTA}👋 Oynadığınız için teşekkürler! Görüşmek üzere!{RenkliCikti.RESET}\n")
                break
            
            self.oyun_modu = secim
            
            # AI zorluk seviyesi
            if self.oyun_modu == 1:
                print(f"\n{RenkliCikti.CYAN}AI Zorluk Seviyesi:{RenkliCikti.RESET}")
                print(f"  {RenkliCikti.YESIL}1.{RenkliCikti.RESET} Kolay (Rastgele oynuyor)")
                print(f"  {RenkliCikti.SARI}2.{RenkliCikti.RESET} Orta (Stratejik)")
                print(f"  {RenkliCikti.KIRMIZI}3.{RenkliCikti.RESET} Zor (Hafızalı ve çok stratejik)")
                
                while True:
                    try:
                        zorluk = int(input(f"\n{RenkliCikti.SARI}Seçiminiz (1/2/3): {RenkliCikti.RESET}"))
                        if zorluk == 1:
                            self.ai = AI('kolay')
                            break
                        elif zorluk == 2:
                            self.ai = AI('orta')
                            break
                        elif zorluk == 3:
                            self.ai = AI('zor')
                            break
                        print(f"{RenkliCikti.KIRMIZI}❌ Lütfen 1, 2 veya 3 girin!{RenkliCikti.RESET}")
                    except:
                        print(f"{RenkliCikti.KIRMIZI}❌ Geçersiz giriş!{RenkliCikti.RESET}")
            
            # Oyunu oyna
            self.oyun_oyna()
            
            # Tekrar oynamak ister misiniz?
            while True:
                tekrar = input(f"\n{RenkliCikti.SARI}Tekrar oynamak ister misiniz? (e/h): {RenkliCikti.RESET}").lower()
                if tekrar in ['e', 'h']:
                    break
            
            if tekrar == 'h':
                print(f"\n{RenkliCikti.MAGENTA}👋 Oynadığınız için teşekkürler! Görüşmek üzere!{RenkliCikti.RESET}\n")
                break
            
            # Yeni oyun için sıfırla
            self.__init__()

# Oyunu başlat
if __name__ == "__main__":
    oyun = KartOyunu()
    oyun.basla()