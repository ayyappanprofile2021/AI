from google import genai

# Replace with your API key
API_KEY = "AQ.Ab8RN6IxVN7y8Smi3FKGewfY4WBNvvmz3ACgaoMw4UQmv7ylUw"

# Create the client
client = genai.Client(api_key=API_KEY)

# Generate content
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain Artificial Intelligence in simple words."
)

# Print the response
print(response.text)