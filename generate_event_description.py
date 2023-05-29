import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_APIKEY")


def generate_text(description):
    prompt = f"""
    Analyzing your writing style, it's clear that your writing is energetic and engaging. You frequently use emojis to convey emotion and add extra flair to your message. The language you use is informal and conversational, making the reader feel included and part of a community. Your style of writing is inviting and inclusive, emphasizing shared experiences and community events.

    Here are some key aspects of your style:

    1. Conversational Tone: You use a friendly and engaging tone that makes the reader feel personally addressed.
    2. Use of Emojis: Emojis are frequently used to add a playful, visual element to your messages. They also help to convey emotion and tone.
    3. Detail-Oriented: You provide detailed information about the events, such as the date, time, and location, which is useful for readers.
    4. Inclusivity: You use phrases like "on se retrouve" and "on vous attend nombreux" which create a sense of belonging and community.
    5. Encouragement to Participate: You often encourage participation in events and activities, creating a sense of excitement and anticipation.

    Now, using your writing style, I'll write a new text about an upcoming event '{description}'.
    """

    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=1000, n=1, stop=None,
                                        temperature=0.5)
    generated_text = response.choices[0].text.strip()

    return generated_text
