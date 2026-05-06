import base64
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# =========================
# 🔐 Encoded model names
# =========================
base_model_enc = "ZmFjZWJvb2svb3B0LTEyNW0="
adapter_enc = "QWlyYWFkYW0vYWlyYS1haQ=="

# Decode
base_model = base64.b64decode(base_model_enc).decode()
adapter = base64.b64decode(adapter_enc).decode()

print("🔄 Loading Aira AI...")

# =========================
# 🧠 Load model + tokenizer
# =========================
try:
    tokenizer = AutoTokenizer.from_pretrained(base_model)

    model = AutoModelForCausalLM.from_pretrained(
        base_model,
        torch_dtype=torch.float32
    )

    model = PeftModel.from_pretrained(model, adapter)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device)

    print("✅ Aira is ready!\n(Type 'exit' to quit)\n")

except Exception as e:
    print("❌ Error loading model:", e)
    exit()

# =========================
# 💬 Chat loop
# =========================
while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    prompt = f"User: {user}\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    try:
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.2,
            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Clean output (only assistant part)
        if "Assistant:" in response:
            response = response.split("Assistant:")[-1].strip()

        print("Aira:", response)

    except Exception as e:
        print("⚠️ Generation error:", e)
