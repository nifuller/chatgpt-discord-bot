import openai
from config import CHATGPT_KEY

class Chatbot:
    def __init__(self):
        openai.api_key = CHATGPT_KEY

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response