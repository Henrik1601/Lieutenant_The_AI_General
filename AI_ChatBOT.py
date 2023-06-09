import openai
import gradio as gr

openai.api_key = "API_KEY"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        try:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            user = [" Colonel!"," Cheif!"]
            reply = chat.choices[0].message.content+random.choice(user)
            messages.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            # Handle the error here, such as logging the error or returning a helpful message to the user
            return "An error occurred: {}".format(str(e))


inputs = gr.inputs.Textbox(lines=7, label="Orders for Lieutenant")
outputs = gr.outputs.Textbox(label="Intels from Lieutenant")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Lieutenant : The AI General",
             description="Cheif! Armadas are set to go. Give us your order!",
             theme="compact").launch(share=True)
