import streamlit as st
import speech_recognition as sr

def speech_to_text(language='en-US'):
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)
    
    try:
        st.write("Recognizing...")
        text = recognizer.recognize_google(audio, language=language)  # Recognize speech with specified language
        return text
    except sr.UnknownValueError:
        st.error("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        st.error("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def main():
    st.title("Multilingual Speech to Text Application By Drex-Dang")
    st.write("Press the 'Start Recording' button and start speaking. Once done, click 'Stop Recording' to see the text.")
    
    input_language = st.selectbox("Select Input Language", ["English", "French", "German", "Spanish", "Chinese", "Korean"])
    output_language = st.selectbox("Select Output Language", ["English", "French", "German", "Spanish", "Chinese", "Korean"])
    
    lang_code_map = {
        "English": "en-US",
        "French": "fr-FR",
        "German": "de-DE",
        "Spanish": "es-ES",
        "Chinese": "zh-CN",
        "Korean": "ko-KR"
    }
    
    input_language_code = lang_code_map.get(input_language, "en-US")
    output_language_code = lang_code_map.get(output_language, "en-US")
    
    if st.button("Start Recording"):
        text = speech_to_text(input_language_code)
        if text:
            st.success("You said: {}".format(text))

if __name__ == "__main__":
    main()