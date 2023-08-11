import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_bolt import App
from dotenv import find_dotenv, load_dotenv
from flask import Flask, request
from functions import test_quiz

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Set Slack API credentials
SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
SLACK_SIGNING_SECRET = os.environ["SLACK_SIGNING_SECRET"]
SLACK_BOT_USER_ID = os.environ["SLACK_BOT_USER_ID"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

# Initialize the Slack app
app = App(token=SLACK_BOT_TOKEN)

# Initialize the Flask app
flask_app = Flask(__name__)
handler = SlackRequestHandler(app)

# Initialize conversation state variables
chat_history = []  # Stores conversation history
current_state = None  # Tracks the current state of the conversation
selected_certification = None  # Stores the selected certification
selected_help = None  # Stores the selected type of help

# Menu options for user interaction
MENU_OPTIONS = {
    "start": "Which certification are you studying for?\n"
             "1. Certified Ethical Hacker (CEH)\n"
             "2. Certified Information Systems Security Professional (CISSP)\n"
             "3. Certified Information Systems Auditor (CISA)\n"
             "4. Security Certification (Security+)",
    "choose_help": "What help would you like?\n"
                   "1. Practice Quiz Question\n"
                   "2. Concept Flashcards\n"
                   "3. General Questions"
}

def get_bot_user_id():
    """
    Get the bot user ID using the Slack API.
    
    Returns:
        str: The bot user ID.
    """
    try:
        # Initialize the Slack client with your bot token
        slack_client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
        response = slack_client.auth_test()
        return response["user_id"]
    except SlackApiError as e:
        print(f"Error: {e}")

def my_function(text):
    """
    Custom function to process the text and return a response.
    
    Args:
        text (str): The input text to process.
    
    Returns:
        str: The processed text.
    """
    response = text.upper()
    return response

@app.event("app_mention")
def handle_mentions(body, say):
    """
    Event listener for mentions in Slack.
    This function processes the user's text and responds accordingly.
    
    Args:
        body (dict): The event data received from Slack.
        say (callable): A function for sending a response to the channel.
    """
    global current_state, selected_certification, selected_help
    text = body["event"]["text"]
    user_id = body["event"]["user"]
    
    mention = f"<@{SLACK_BOT_USER_ID}>"
    text = text.replace(mention, "").strip()
    
    if current_state is None:
        current_state = "start"
        say(MENU_OPTIONS["start"])
        print(chat_history)
    
    # Logic for handling different conversation states
    if current_state == "start":
        if text in ["1", "2", "3", "4"]:
            selected_certification = text
            current_state = "choose_help"
            say(MENU_OPTIONS["choose_help"])
            print(chat_history)
    elif current_state == "choose_help":
        if text in ["1", "2", "3"]:
            selected_help = text
            current_state = "interaction"
            say("Great! Let's start your chosen help.")
            print(chat_history)
    elif current_state == "interaction":
        if text == "end":
            # Reset the conversation state after interaction
            current_state = None
            selected_certification = None
            selected_help = None
            say("Ended")
        if selected_help == "1":
            # Call the function for Practice Quiz Question
            say(test_quiz(text, chat_history))
            print(chat_history)
        elif selected_help == "2":
            # Call the function for Concept Flashcards
            say("You have chosen Concept Flashcards")
        elif selected_help == "3":
            # Call the function for General Questions
            say("Ask me any question")
        #FUTURE DEV: Add cases for other help options
        else:
            say("Please select a valid option.")
    else:
        say("Sorry, I didn't understand that.")

@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    """
    Route for handling Slack events.
    This function passes the incoming HTTP request to the SlackRequestHandler for processing.
    
    Returns:
        Response: The result of handling the request.
    """
    return handler.handle(request)

# Run the Flask app
if __name__ == "__main__":
    flask_app.run()