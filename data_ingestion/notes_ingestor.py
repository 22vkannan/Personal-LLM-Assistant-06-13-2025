import os
from memory.memory_store import store_memory

def ingest_notes(folder):
    for file in os.listdir(folder):
        if file.endswith(('.txt', '.md')):
            with open(os.path.join(folder, file)) as f:
                store_memory(f.read())
