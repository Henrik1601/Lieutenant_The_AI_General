import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        user = [" Colonel!"," Cheif!"]
        reply = chat.choices[0].message.content+random.choice(user)
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Orders for Lieutenant")
outputs = gr.outputs.Textbox(label="Intels from Lieutenant")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Lieutenant : The AI General",
             description="Cheif! Armadas are set to go. Give us your order!",
             theme="compact").launch(share=True)
