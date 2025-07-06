from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

def get_goals(user_input):
    model_id = "meta-llama/Llama-2-7b-chat-hf"
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=150)

    prompt = f"You are a health planner. Based on the user's goal: '{user_input}', generate a 2-month plan including daily steps and calorie intake."
    output = pipe(prompt)[0]['generated_text']
    return {
        "goal": user_input,
        "plan": output
    }