from transformers import GPT2Tokenizer, GPT2LMHeadModel, DataCollatorForLanguageModeling, Trainer, TrainingArguments
from datasets import load_dataset, Dataset


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')


tokenizer.pad_token = tokenizer.eos_token

model = GPT2LMHeadModel.from_pretrained('gpt2')


def load_dataset(file_path, tokenizer):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    lines = text.split('\n')
    data = {'text': lines}
    dataset = Dataset.from_dict(data)
    
    tokenized_dataset = dataset.map(lambda e: tokenizer(e['text'], truncation=True, padding='max_length', max_length=512), batched=True)
    return tokenized_dataset


train_file_path = "train_data.txt"
train_dataset = load_dataset(train_file_path, tokenizer)


data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False,
)


training_args = TrainingArguments(
    output_dir="./results",
    overwrite_output_dir=True,
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
)


trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)


trainer.train()


model.save_pretrained("./results")
tokenizer.save_pretrained("./results")
