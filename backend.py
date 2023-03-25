import openai
import time
from datetime import datetime, timedelta
from config import CHATGPT_KEY

class GetTime():
    def __init__(self):
        self.today = datetime.now()
        self.tomorrow = self.today + timedelta(1)
        self.yesterday = self.today - timedelta(1)

    def time_check(self):
        self.today = self.today.strftime('%d-%m')
        self.tomorrow = self.tomorrow.strftime('%d-%m')
        
        if self.today == self.tomorrow:
            return True
        else:
            return False

class RestrictCommand:
    def __init__(self):
        self.calls = 0;

    def update_calls(self):
        self.calls += 1

    def retrieve_calls(self):
        return self.calls
        
class Bozobot:
    def __init__(self):
        openai.api_key = CHATGPT_KEY

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_tokens=4000,
                temperature=0.7
            ).choices[0].text
            return response
        except openai.InvalidRequestError as e:
            message = f"Invalid Reuest: {e}"
            return message
        except openai.APIError as e:
            message = f"OpenAI API returned an API Error: {e}"
            return message
    
    def get_prompt(self, user_input):
        try:
            response = openai.Image.create(
                prompt = user_input,
                n=1,
                size="512x512"
            )
            image_url = response['data'][0]['url']
            return image_url
        except openai.InvalidRequestError as e:
            message = f"Invalid Request: {e}"
            return message
        
        except openai.APIError as e:
            message = f"OpenAI API returned an API Error: {e}"
            return message
 