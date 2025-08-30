import os
from dotenv import load_dotenv, find_dotenv

# Load .env
_ = load_dotenv(find_dotenv())

# Read key just to confirm (you already tested this)
api_key = os.getenv("OPENAI_API_KEY")
print("Your API key starts with:", api_key[:7])

# -------------------------
# FAKE OPENAI RESPONSE
# -------------------------
class FakeChoice:
    def __init__(self, content):
        self.message = type("msg", (), {"content": content})

class FakeResponse:
    def __init__(self, content):
        self.choices = [FakeChoice(content)]

# Pretend the API replied with "Hi there!"
response = FakeResponse("Hi there! 👋 This is a fake test response.")

print(response.choices[0].message.content)