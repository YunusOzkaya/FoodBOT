from dotenv import load_dotenv
import speech_recognition as sr
import streamlit as st
import os
import google.generativeai as genai
from elevenlabs import play
from elevenlabs.client import ElevenLabs


# .env dosyasını yükleyin
load_dotenv()

# Google API ve ElevenLabs istemci yapılandırması
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
client = ElevenLabs(api_key=os.getenv("XI_API_KEY"))

# GenAI modelini başlatın
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Streamlit sayfa konfigürasyonunu ayarlayın
st.set_page_config(page_title="Yemek Chatbot")
st.title("Yemek Hakkında Her Şey")
st.subheader(
    "202523011 Nasuhan Yunus Özkaya İSTE Bilgisayar Mühendisliği Bitirme Projesi - II"
)

# Sohbet geçmişini saklamak için session state kullanın
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Kullanıcı girişini alın
input_question = st.text_input("Sorunuzu yazın: ", key="input_question")
submit = st.button("Sorunuzu sorun")


# Ses tanıma fonksiyonu
def voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        st.text("Ses dinleniyor...")
        audio = r.listen(source, timeout=5)
        try:
            text = r.recognize_google(audio, language="tr")
            st.text(f"Ses Tanıma: {text}")
            return text
        except sr.UnknownValueError:
            st.warning("Ses anlaşılamadı.")
            return None
        except sr.RequestError:
            st.error("Google API'ye ulaşılamadı.")
            return None


# Yemekle ilgili soruları kontrol etme fonksiyonu
def is_food_related(question):
    # Yemekle ilgili anahtar kelimelerin listesi
    food_keywords = ["yemek", "tarif", "mutfak", "pişirme", "malzeme"]
    return any(keyword in question.lower() for keyword in food_keywords)


# Sesli komutla sohbeti başlatma ve sesli soruları işleme
if st.button("Sesli Komutla Başlat"):
    st.session_state["voice_active"] = True  # Sesli komutları aktif et
    while st.session_state["voice_active"]:
        question = voice_to_text()
        if question:
            if is_food_related(question):
                response = chat.send_message(
                    question
                    + " Yanıtın öncesinde bu tarifin ya da önerinin hangi diyet türlerine uygun olduğunu, kişilerin yemekle ilgili rahatsızlıklarını da göz önüne alarak yani şeker hastalığı; gut; kalp-damar tıkanılığı gibi hastaların yiyip; yiyemeceği gibi bilgileri, kaç kişilik olduğunu, toplam kaç kalori olduğunu ve makro besin değerlerini de belirt.  ",
                    stream=True,
                )
                full_response = ""
                for chunk in response:
                    full_response += chunk.text + " "  # Parçaları birleştir
                st.session_state["chat_history"].append(("Siz", question))
                st.subheader("Cevap: ")
                st.write(full_response.strip())  # Tek bir metin olarak göster
                audio = client.generate(
                    text=full_response.strip(),
                    voice="Rachel",
                    model="eleven_multilingual_v2",
                    stream=True,
                )
                play(audio)
                break  # Döngüyü sonlandır
            else:
                st.warning("Lütfen yemekle ilgili bir soru sorun.")
                audio = client.generate(
                    text="Lütfen yemekle ilgili bir soru sorun.",
                    voice="Rachel",
                    model="eleven_multilingual_v2",
                    stream=True,
                )
                play(audio)
                break  # Döngüyü sonlandır

# Yazılı olarak soru sorma ve cevap alma
elif submit and input_question:
    if is_food_related(input_question):
        response = chat.send_message(input_question, stream=True)
        full_response = ""
        for chunk in response:
            full_response += chunk.text + " "  # Parçaları birleştir
        st.session_state["chat_history"].append(("Siz", input_question))
        st.subheader("Cevap: ")
        st.write(full_response.strip())  # Tek bir metin olarak göster
        audio = client.generate(
            text=full_response.strip(),
            voice="Rachel",
            model="eleven_multilingual_v2",
            stream=True,
        )
        play(audio)
    else:
        st.warning("Lütfen yemekle ilgili bir soru sorun.")
        audio = client.generate(
            text="Lütfen yemekle ilgili bir soru sorun.",
            voice="Rachel",
            model="eleven_multilingual_v2",
            stream=True,
        )
        play(audio)

# Soru geçmişini göster
st.subheader("Soru geçmişiniz:")
for role, text in st.session_state["chat_history"]:
    st.write(f"{role}: {text}")
