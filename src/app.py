from groq_integration import call_groq_api

if __name__ == "__main__":
    query = "Your GROQ query here"
    try:
        result = call_groq_api(query)
        print(f"GROQ API Response: {result}")
    except Exception as e:
        print(f"Error: {e}")
