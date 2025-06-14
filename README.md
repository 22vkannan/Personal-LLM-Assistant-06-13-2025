# Personal LLM Assistant

A Privacy-First, On-Device Retrieval-Augmented Generation (RAG) Assistant.  
Runs on both **web** and **mobile** (React Native) with long-term memory, local speech input, and flexible LLM backend.

---

## Project Objectives

- Run on web + mobile (React Native)
- Store long-term memory with ChromaDB + vector embeddings
- Retrieve and reason over emails, documents, alerts
- Respond via OpenAI API or fallback to local Ollama model
- Use Whisper for potential voice input
- Keep all data and processing locally (privacy-first)

---

## Tech Stack Overview

| Component      | Purpose |
|----------------|---------|
| Flask          | Backend server for routing, LLM calls, responses |
| OpenAI API     | Online GPT 3.5/4 completions |
| ChromaDB       | Vector DB for memory storage + semantic retrieval |
| React Native   | Unified cross-platform UI (mobile) |
| Python         | Primary backend language |
| Ollama         | Local LLM fallback (offline mode) |
| Whisper        | Speech-to-text transcription |

---

## Folder Structure

