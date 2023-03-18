import openai
from config import CHATGPT_KEY

class GptBot:
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
    
    def get_prompt(self, user_input):
        try:
            response = openai.Image.create(
                prompt = user_input,
                n=1,
                size="1024x1024"
            )
            image_url = response['data'][0]['url']
            return image_url
        except openai.InvalidRequestError:
            message = "Error! Try asking Bozo again."
            return message