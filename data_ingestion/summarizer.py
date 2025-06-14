from llm_engine.openai_engine import get_openai_response

def summarize_week():
    prompt = "Summarize this week's emails and calendar events..."
    # Retrieve memory from past 7 days only (extend logic as needed)
    memory_text = "\n".join(retrieve_memory("week"))
    return get_openai_response(f"{prompt}\n\n{memory_text}")



 






