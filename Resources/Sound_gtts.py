from gtts import gTTS

text="Tamper alert"
tts=gTTS(text)
tts.save("/Users/timara/PycharmProjects/Cse_520_VS_System/Resources/alert.mp3")
