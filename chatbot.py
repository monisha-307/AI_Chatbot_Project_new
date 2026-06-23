from google import genai

client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

history = []

print("Chatbot ready! Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Bye!")
        break

    if not user_input:
        print("Please enter a message.")
        continue

    history.append({"role": "user", "parts": [{"text": user_input}]})

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=history
    )

    reply = response.text
    print("Bot:", reply)

    history.append({"role": "model", "parts": [{"text": reply}]})