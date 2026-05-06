🤖 Aira AI

Aira AI is a lightweight, open-source conversational AI chatbot built using the OPT-125M language model with LoRA fine-tuning (PEFT).
It is designed for simple local chat, experimentation, and learning how custom AI assistants can be built and deployed.

---

🚀 Features

- 💬 Interactive command-line chatbot
- 🧠 Based on a fine-tuned transformer model
- ⚡ Lightweight (runs on CPU or GPU)
- 🔐 Basic obfuscation for model identifiers
- 🧩 Built using modern AI tooling (Transformers + PEFT)
- 🛠 Easy to modify and extend

---

🧠 Model Info

- Base Model: facebook/opt-125m
- Fine-tuning: LoRA (Low-Rank Adaptation)
- Frameworks: Transformers, PEFT
- Model Type: Causal Language Model (Text Generation)

---

📦 Installation

Clone the repository:

git clone https://github.com/your-username/aira-ai.git
cd aira-ai

Install dependencies:

pip install -r requirements.txt

---

▶️ Usage

Run the chatbot:

python app.py

Then start chatting:

You: Hello
Aira: Hi! How can I help you?

To exit:

exit

---

🖥 Requirements

- Python 3.8+
- PyTorch
- Transformers
- PEFT

---

⚙️ How It Works

1. Loads the base model (OPT-125M)
2. Applies the fine-tuned LoRA adapter
3. Takes user input from terminal
4. Generates AI response using sampling
5. Displays output in a conversational format

---

⚠️ Limitations

- Small model → limited intelligence
- May repeat responses sometimes
- Not optimized for production use
- No memory (stateless chat)

---

🔮 Future Improvements

- 🌐 Web UI (Streamlit / Flask)
- 📱 Mobile app integration
- 🧠 Better fine-tuning dataset
- 🗣 Multi-language support (Malayalam 🔥)
- 💾 Conversation memory

---

🤝 Contributing

Pull requests are welcome!
Feel free to fork this repo and improve Aira AI.

---

📜 License

This project is open-source and available under the MIT License.

---

👨‍💻 Author

Adam (Airaadam)
Creator of Aira AI

---

⭐ Support

If you like this project:

- ⭐ Star this repo
- 🍴 Fork it
- 🧠 Build your own AI

---

💬 Final Note

Aira AI is a beginner-friendly project to explore how AI assistants work under the hood.
It’s not perfect — but it’s a strong step into the world of AI development 🚀
