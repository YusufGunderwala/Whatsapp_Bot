import pyautogui
import time
import pyperclip
from groq import Groq

client = Groq(
    api_key="Your_Api_Key",
)


def is_last_message_from_sender(chat_log, sender_name="Neha R"):
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True
    return False


    # Step 1: Click on the chrome icon at coordinates (1639, 1412)
pyautogui.click(1343, 1044)

time.sleep(1)  # Wait for 1 second to ensure the click is registered
while True:
    time.sleep(5)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(683, 300)
    pyautogui.dragTo(1032, 880, duration=2.0,
                     button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed
    pyautogui.click(676, 296)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    # Print the copied text to verify
    print(chat_history)
    print(is_last_message_from_sender(chat_history))
    if is_last_message_from_sender(chat_history):
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system",
                 "content": "You are a person named Arjun K who speaks hindi as well as english. You are from India and you are all movie expert . You analyze chat history and answer it. Output should be the next chat response (text message only)"},
                {"role": "system",
                 "content": "Do not start like this [09:37, 8/20/2024] Neha R "},
                {"role": "user", "content": chat_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1184, 950)
        time.sleep(1)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        # Wait for 1 second to ensure the paste command is completed
        time.sleep(1)

        # Step 7: Press Enter
        pyautogui.press('enter')
