from gtts import gTTS

text="Tamper,alert"
tts=gTTS(text,lang='en', tld='com.au')
tts.save("alert.mp3")

text="Hi,before starting surveillance,please choose the following options"
tts=gTTS(text,lang='en', tld='com.au')
tts.save("hello.mp3")

text="Starting Surveillance"
tts=gTTS(text,lang='en', tld='com.au')
tts.save("Starting_Simulation.mp3")
