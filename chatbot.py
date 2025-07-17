# chatbot.py
def chatbot_response(user_input):
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()

    # Dictionary of query patterns and responses
    responses = {
        "hi|hello|hey": "Hello! Welcome to our customer service. How can I help you?",
        "hours|opening hours|time": "We are open from 9 AM to 5 PM, Monday to Friday.",
        "refund|return": "Our refund policy allows returns within 30 days with a receipt.",
        "contact|support": "You can reach us at support@example.com or call 1-800-123-4567.",
        "price|cost": "Please provide the product name for pricing details!",
        "thank you|thanks": "You're welcome! Have a great day!",
        "bye|goodbye": "Goodbye! Thanks for reaching out."
    }

    # Default response if no match is found
    default_response = "Sorry, I didn't understand. Please try again or contact support@example.com."

    # Check for matching patterns
    for pattern, response in responses.items():
        if any(word in user_input for word in pattern.split("|")):
            return response

    return default_response


def main():
    print("Customer Service Chatbot - Type 'bye' to exit")
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() == "bye":
            print("Chatbot: Goodbye! Thanks for reaching out.")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()