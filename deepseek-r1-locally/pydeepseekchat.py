from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="doesnt matter")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain quantum entanglement to me.",
        }
    ],
    model="deepseek-r1:14b",
)

print(chat_completion.choices[0].message.content)
