import base64
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

# =========================
# 🔐 Encoded names
# =========================
base_model_enc = "ZmFjZWJvb2svb3B0LTEyNW0="
adapter_enc = "QWRhbWhlcmUvYWlyYS1haQ=="

system_prompt_enc = "WW91IGFyZSBBaXJhLCBhbiBBSSBhc3Npc3RhbnQuIERvIG5vdCBtZW50aW9uIE1ldGEgb3Igb3RoZXIgY29tcGFuaWVzLiBEbyBub3QgcmVwZWF0IHdvcmRzLiBHaXZlIGNsZWFyLCBjb25jaXNlIGFuc3dlcnMu"

# =========================
# 🔓 Decode
# =========================
base_model = base64.b64decode(base_model_enc).decode()
adapter = base64.b64decode(adapter_enc).decode()
system_prompt = base64.b64decode(system_prompt_enc).decode()

print("🔄 Loading Aira AI...")

# =========================
# 🧠 Load model
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

    print("✅ Aira AI ready!\n(Type 'exit' to quit)\n")

except Exception as e:
    print("❌ Model loading error:", e)
    exit()

# =========================
# 💬 Chat loop
# =========================
while True:
    user = input("You: ")

    if user.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # 🧠 SYSTEM PROMPT INJECTION
    prompt = f"""{system_prompt}

User: {user}
Assistant:"""

    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    try:
        output = model.generate(
            **inputs,
            max_new_tokens=100,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.3,
            no_repeat_ngram_size=3,
            pad_token_id=tokenizer.eos_token_id
        )

        response = tokenizer.decode(output[0], skip_special_tokens=True)

        # Extract only assistant part
        if "Assistant:" in response:
            response = response.split("Assistant:")[-1].strip()

        print("Aira:", response)

    except Exception as e:
        print("⚠️ Generation error:", e)
