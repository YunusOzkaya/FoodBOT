# Yemek Chatbot

Bu proje, kullanıcıların yemekle ilgili sorular sormasına ve cevaplar almasına olanak tanıyan bir sohbet uygulamasıdır. Kullanıcılar, metin veya ses girişiyle yemek tarifleri, pişirme yöntemleri veya malzeme önerileri gibi yemekle ilgili soruları yönlendirebilirler. Chatbot, bu sorulara yapay zeka ve sesli yanıtlarla yanıt verir.

## Gereksinimler

- Python 3.x
- `dotenv` kütüphanesi
- `speech_recognition` kütüphanesi
- `streamlit` kütüphanesi
- Google GenAI API Anahtarı
- ElevenLabs API Anahtarı

## Kurulum

1. Anaconda veya Python sanal ortamınızı oluşturun.
2. Projeyi klonlayın veya indirin.
3. Terminali veya komut istemcisini proje dizinine ayarlayın.
4. Gerekli kütüphaneleri yüklemek için `pip install -r requirements.txt` komutunu çalıştırın.
5. Google GenAI API ve ElevenLabs API anahtarlarını `.env` dosyasına ekleyin.

## Kullanım

- Uygulamayı başlatmak için terminalde `streamlit run yemek_chatbot.py` komutunu çalıştırın.
- Metin girişiyle bir soru sormak için metin giriş kutusuna soruyu yazın ve "Sorunuzu sorun" düğmesine tıklayın.
- Sesli girişle bir soru sormak için "Sesli Komutla Başlat" düğmesine tıklayın ve sorunuzu konuşun.
- Soru geçmişini görmek için sayfanın alt kısmında "Soru geçmişiniz" bölümüne bakın.

## Özellikler

- Sesli girişle soru sorma ve sesli cevap alma.
- Metin girişiyle soru sorma ve metin cevabı alma.
- Yemekle ilgili soruları algılama ve sadece bu tür sorulara cevap verme.

## Katkıda Bulunma

- Kodu anlamak veya geliştirmek için kod tabanını inceleyin.
- Hata raporları ve öneriler için bir GitHub Issue oluşturun.
- Kod katkısı yapmak için bir Pull Request gönderin.
