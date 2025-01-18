# Configuration and environment variable handling
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configuration variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print(GROQ_API_KEY)  # Output: "your-api
