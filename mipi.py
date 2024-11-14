from datasets import load_dataset
from transformers import AutoTokenizer
import torch

print(torch.cuda.is_available())
print("Cargando Dataset")
ds = load_dataset("qq8933/OpenLongCoT-Pretrain")
print("Importando")
# Importaciones
print("Tokenizando dataset")

def tokenizar(examples):
    
result = ds.map(tokenizar)

# Tokenizando
# tokenizer = AutoTokenizer.from_pretrained("unsloth/Meta-Llama-3.1-8B-bnb-4bit").to('cuda')

#def tokenize_function(examples):
#    return tokenizer(examples["text"], padding="max_length", truncation=True)

#dataset = ds.map(tokenize_function, batched=True)

#print(dataset[0])
