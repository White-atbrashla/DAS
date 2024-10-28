import json

# Initialize or load the cache from JSON to store responses
def load_cache(filename="Agent_responses.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Start fresh if the file doesn't exist

def save_to_cache(response, filename="Agent_responses.json"):
    """Save the generated response to a JSON file."""
    cache = load_cache(filename)
    cache.append(response)  # Append the new response
    with open(filename, "w") as f:
        json.dump(cache, f, indent=4)

# Function to generate text and save to cache
def generate_cached_response(prompt):
    """Generate response, save to cache, and return it."""
    response = generate_text(prompt)  # Call the generate_text() function
    save_to_cache(response)  # Save response to JSON cache
    return response

# Define your generic co-pilot agent prompts
prompts = [
    "You are a next-generation co-pilot AI agent responsible for integrating multi-source intelligence and providing actionable insights across complex operational environments. Your mission is to enhance situational awareness, assist in decision-making, and continuously adapt to evolving conditions. Begin by describing your role and capabilities in supporting multi-source intelligence integration.",
    
    "Explain the purpose of a multi-agent matrix within this co-pilot AI system. Describe how specialized agents coordinate to manage tasks such as real-time data processing, predictive analytics, and collaborative decision-making. Include how the matrix ensures effective communication and operational efficiency among agents.",

    "Describe the role of an advanced narrative validation framework in identifying emerging patterns, detecting disinformation, and ensuring the reliability of insights. Explain how data from social, traditional, and geospatial sources is synthesized to provide a coherent and validated view of ongoing operations.",

    "Based on the functionalities of the co-pilot agent system—including multi-agent collaboration, narrative validation, and real-time intelligence synthesis—what are the key strategic recommendations to ensure optimal performance, mitigate risks, and adapt to dynamic situations? Provide a summary of these recommendations to guide operational decision-making."
]

# Loop through prompts, chaining responses together
for i, prompt in enumerate(prompts):
    print(f"\nRunning prompt {i + 1}...")
    output = generate_cached_response(prompt)  # Generate and cache the output
    print(f"Output {i + 1}: {output}\n")

# Display the entire conversation history at the end
conversation_history = load_cache()
print("Full Conversation History:")
for idx, entry in enumerate(conversation_history):
    print(f"Step {idx + 1}: {entry}")
