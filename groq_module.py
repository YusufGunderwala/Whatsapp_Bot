from groq import Groq


client = Groq(
    api_key="Your_Api_Key",
)

command = '''
[09:37, 8/20/2024] Arjun K: Hey, you there?
[09:37, 8/20/2024] Neha R: Yep, what's up?
[09:38, 8/20/2024] Arjun K: Just checking, did the team get access to the new analytics tool?
[09:38, 8/20/2024] Neha R: Hmm, I think only Raj has access right now.
[09:38, 8/20/2024] Arjun K: Oh, got it. So he’ll be handling reports?
[09:39, 8/20/2024] Neha R: Yes, but I’ll ask him to share a summary with us.
[09:40, 8/20/2024] Arjun K: Great, thanks! Let me know if there’s anything I can help with.
[15:10, 8/20/2024] Neha R: Hey, quick question – could you share the script details for the project setup?
[15:13, 8/20/2024] Arjun K: Sure, I’ll send it over in a bit
'''
completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {"role": "system", "content": "You are a person named Arjun K who speaks hindi as well as english. He is from India and is a Pro coder. You analyze chat history and respond like Arjun K"},
        {"role": "user", "content": command}
    ]
)

print(completion.choices[0].message.content)
