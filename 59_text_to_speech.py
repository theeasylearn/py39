from gtts import gTTS
from playsound import playsound

# 1. Generate and save the English audio
# print("Generating English audio...")
# tts_en = gTTS(text="Hello, how can I help you today?", lang="en")
# tts_en.save("english.mp3")

# # Play the English audio automatically
# print("Playing English audio...")
# playsound("english.mp3")


# 2. Generate and save the Hindi audio
print("\nGenerating Hindi audio...")
hindi_text = """UPI से ₹2,000 से ज्यादा पेमेंट पर 0.4% चार्ज लगेगा। फीस की मैक्सिमम लिमिट 300 रुपए तक की गई है। यह अमाउंट अलग-अलग ट्रांजैक्शन पर निर्भर करेगा। यह शुल्क ग्राहकों से नहीं बिजनसेमैन से लिया जाएगा।

हालांकि ₹2,000 तक पेमेंट करने पर ग्राहक और बिजनेसमैन दोनों से किसी तरह की फीस नहीं ली जाएगी। वित्त मंत्रालय ने सोमवार को नोटिफिकेशन जारी कर यह स्थिति साफ कर दी थी। RuPay डेबिट कार्ड से होने वाले पेमेंट को भी इस छूट में शामिल किया गया है।

दरअसल, अगस्त में संसद से टैक्सेशन एंड अदर लॉज (अमेंडमेंट) एक्ट, 2026 पास होने के बाद UPI पेमेंट पर चार्ज को लेकर चर्चा शुरू हुई थी।

सरकार ने छोटे दुकानदारों के लिए प्रोत्साहन योजना शुरू की थी"""
# text to speech
hindi = gTTS(text=hindi_text, lang="hi")
hindi.save("hindi.mp3")

# Play the Hindi audio automatically
print("Playing Hindi audio...")
playsound("hindi.mp3")

print("\nAll files generated and played successfully!")
