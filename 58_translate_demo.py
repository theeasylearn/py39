# pip install translators
import translators as ts
text = """the accused in the Golf Course Road hit-and-run case was injured after he allegedly tried to flee from police custody following his arrest in Rajasthan, police said on Tuesday.Kalyan Singh Bainsla fell while attempting to escape and was apprehended by the police again, officials said.Police spokesperson Sandeep Turan said Bainsla told investigators that he wanted to urinate before attempting to flee. He allegedly ran away but fell and sustained injuries before police caught him again."""
#trasnalte english text into gujarat
result = ts.translate_text(text, from_language='en', to_language='hi', translator='google')
print(result)  # Gujarati output