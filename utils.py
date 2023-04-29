import openai
openai.api_key = "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"


def get_answer(phrase: str):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": phrase}])
    return completion.choices[0].message.content


def translator(phrase: str, language: str):
    if language == "English":
        return phrase
    elif language == "Spanish":
        return get_answer(f"Translate from Spanish to English: {phrase}")
    elif language == "German":
        return get_answer(f"Translate from German to English: {phrase}")
    else:
        raise ValueError("Language not supported")

def text_generator(phrase: str):
    return get_answer(f"Convert the following bullet points into a report: {phrase}")

