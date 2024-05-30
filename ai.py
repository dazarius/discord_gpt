

from openai import OpenAI
import time
import os
class AI:
    def __init__(self, ap):
        self.api = ap
        self.openai = OpenAI(api_key=self.api)
    
    def generate(self, prompt):
        chat_completion = self.openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo-instruct",
    )
        content = chat_completion.choices[0].message.content
        return content


    # def audio_to_text(self, file):
    #     audio_file = open(file, "rb")
    #     transcript = self.openai.audio.transcriptions.create(
    #     model="whisper-1",
    #     file=audio_file
    # )
    #     with open("transcript.txt", "w") as f:
    #         f.write(transcript.text)
    #     return "done"


    #     speech_file_path = "RU.mp3"
    #     response = self.openai.audio.speech.create(
    #     model="tts-1",
    #     voice="alloy",
    #     input="привет это пример моего русского голоса",
    #     )
    #     response.stream_to_file(speech_file_path)
    #     return speech_file_path

        
