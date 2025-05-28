import pyautogui
import pyperclip
import time
from openai import OpenAI


  
client = OpenAI(
    api_key="", # Replace with your OpenAI API key
)

def is_last_message_from_sender(chat_log, sender_name="jawale"):
    messages = chat_log.strip().split("/2025]")[-1]
    if sender_name in messages:
       return True
    return False    


# Step 1: Click on the icon at (1537, 1045)
pyautogui.click(1417,1062) # enter your own coordinates through running program.py
time.sleep(1)  # Wait for the app or window to respond          
# Optional: Small delay before script starts so you can get ready
# time.sleep(2)
while True:
    
# Step 2: Drag from (538, 138) to (2270, 949)
  pyautogui.moveTo(795, 238)
  pyautogui.dragTo(2524, 935, duration=1)  # Drag with a duration for smoothness

# Step 3: Copy selected text using Ctrl+C
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.click(910, 385)
  time.sleep(1)  # Give clipboard time to update

# Step 4: Get copied text into a variable
  chat_history = pyperclip.paste()
  print(chat_history)

  if is_last_message_from_sender(chat_history):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system","content": "You are a person named krrish who speaks hindi and english. you are from india and you are a coder. you analyze chat history and respond like krrish. output should be the next chat response (text message only)"},
        {"role": "user","content": chat_history}
    ]
    )

    response = completion.choices[0].message.content
    pyperclip.copy(response)  # Copy the response to clipboard


    pyautogui.click(950, 972)
    time.sleep(1)  # Wait for the input field to be ready

    pyautogui.hotkey('ctrl', 'v')  # Paste the response
    time.sleep(1)  

    pyautogui.press('enter')  # Send the response