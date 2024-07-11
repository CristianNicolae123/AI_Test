from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Încarcă modelul antrenat și tokenizer-ul
model = GPT2LMHeadModel.from_pretrained("./results")
tokenizer = GPT2Tokenizer.from_pretrained("./results")

# Funcție pentru generarea de text
def generate_offer(prompt, max_new_tokens=150, temperature=0.7, top_p=0.9, repetition_penalty=1.2):
    inputs = tokenizer(prompt, return_tensors='pt', padding=True)
    outputs = model.generate(
        inputs.input_ids,
        attention_mask=inputs.attention_mask,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Exemplu de utilizare
if __name__ == "__main__":
    prompt = (
        "Cerința clientului: O aplicație de tip Glovo.\n\n"
        "Descrierea aplicației solicitate:\n"
        "Aplicația va permite utilizatorilor să comande mâncare de la diverse restaurante și să gestioneze livrările printr-un sistem logistic eficient. Utilizatorii vor putea adăuga și elimina produse din meniul restaurantelor, să plătească cu cardul și să primească comenzi în timp real.\n\n"
        "Tehnologiile folosite:\n"
        "Aplicația va fi dezvoltată folosind React Native pentru interfața de utilizator, Node.js pentru backend, și MongoDB pentru baza de date. Vom folosi Stripe pentru procesarea plăților cu cardul și Google Maps API pentru tracking-ul livrărilor.\n\n"
        "Task-urile concrete și detaliate necesare pentru dezvoltarea aplicației:\n"
        "- Designul interfeței utilizatorului folosind React Native\n"
        "- Implementarea funcționalității de înregistrare a restaurantelor\n"
        "- Dezvoltarea sistemului de logistică pentru rideri\n"
        "- Configurarea plăților cu cardul folosind Stripe\n"
        "- Integrarea Google Maps API pentru tracking-ul livrărilor\n"
        "- Testarea aplicației pe diverse dispozitive mobile\n"
        "- Implementarea feedback-ului de la utilizatori și ajustarea funcționalităților\n"
        "- Secțiunea financiară: cum restaurantele solicită bani de la administratorii aplicației\n"
        "- Modalități de plată pentru rideri\n"
        "- Generarea automată a facturilor și posibilitatea clientului de a descărca factura generată\n"
    )
    generated_offer = generate_offer(prompt)
    print(generated_offer)
