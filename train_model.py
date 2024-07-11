from transformers import GPT2Tokenizer, GPT2LMHeadModel, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset, Dataset

# Încarcă tokenizer-ul și modelul GPT-2
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Adaugă un token de padding la tokenizer
tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained('gpt2')

# Pregătirea dataset-ului
def load_dataset(file_path, tokenizer):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # Split text into lines și creează dataset
    lines = text.split('\n')
    data = {'text': lines}
    dataset = Dataset.from_dict(data)
    # Tokenizează dataset-ul
    tokenized_dataset = dataset.map(lambda e: tokenizer(e['text'], truncation=True, padding='max_length', max_length=512), batched=True)
    return tokenized_dataset

# Calea către fișierul de antrenament
train_file_path = "train_data.txt"
train_dataset = load_dataset(train_file_path, tokenizer)

# Data collator pentru modelarea limbajului
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)

# Setări pentru antrenare
training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Antrenează modelul
trainer.train()

# Salvează modelul și tokenizer-ul
model.save_pretrained("./results")
tokenizer.save_pretrained("./results")
