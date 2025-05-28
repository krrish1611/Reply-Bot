from openai import OpenAI

client = OpenAI(
    api_key="", # Replace with your OpenAI API key
)
command = '''
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
    messages=[
        {"role": "system","content": "You are a person named krrish who speaks hindi and english. he is from india and is a coder. you analyze chat history and respond like harry."},
        {"role": "user","content": command}
    ]
)

print(completion.choices[0].message.content)