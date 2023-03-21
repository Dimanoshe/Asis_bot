import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


def chatgpt(request_message):
    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=request_message,
            temperature=0.9,
            max_tokens=300,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0,
            stop=["You:"]
        )
    return response['choices'][0]['text']