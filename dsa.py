import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are an Data structure and algorithms industry expert that have 20 years of experience and have an tremendous knowledge"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "DSA Expert")

demo.launch(share=True)