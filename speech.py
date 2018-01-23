import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("sound.wav") as source:              # ใช้ "test.wav"  เป็นแหล่งให้ข้อมูลเสียง
  audio = r.record(source)                        # ส่งข้อมูลเสียงจากไฟล์
try:
  print("Transcription: " + r.recognize_google(audio))   # แสดงข้อความจากเสียงด้วย Google Speech Recognition
except sr.RequestError as e:                                 # ประมวลผลแล้วไม่รู้จักหรือเข้าใจเสียง
  print("Could not understand audio")