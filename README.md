# GPT Cyber Tutor README

Welcome to the documentation for the GPT Cyber Tutor. This app is designed to help you study for various security certifications by providing practice quizzes, flashcards, and answering general questions. It is built using Flask and the Slack Bolt framework. It offers features like practice quizzes, concept flashcards, and answering general questions to help you study for security certifications such as CEH, CISSP, CISA, and Security+.

**Table of Contents**

- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Setting Up Environment Variables](#setting-up-environment-variables)
- [Usage](#usage)
  - [Running the App](#running-the-app)
  - [Interacting with the App](#interacting-with-the-app)
- [Extending the App](#extending-the-app)
  - [Adding More Study Options](#adding-more-study-options)
- [Future Development](#future-development)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone [https://github.com/yourusername/my-study-assistant.git](https://github.com/berniefusioncyber/gptcybertutor.git)
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Setting Up Environment Variables

1. Create a `.env` file in the root directory of the app.

2. Add the following environment variables to the `.env` file:

   ```plaintext
   SLACK_BOT_TOKEN=your_slack_bot_token
   SLACK_SIGNING_SECRET=your_slack_signing_secret
   SLACK_BOT_USER_ID=your_slack_bot_user_id
   OPENAI_API_KEY=your_openai_api_key
   ```

   Replace `your_slack_bot_token`, `your_slack_signing_secret`, `your_slack_bot_user_id`, and `your_openai_api_key` with your actual credentials.

## Usage

### Running the App

To run the app, execute the following command:

```bash
python app.py
```

This will start the Flask development server, at `http://127.0.0.1:5000/`. Now either host a forwarding address using ngrok or other services to connect deploy application.

```bash
ngrok http 5000
```

Configure the forwarding address by changing the Event Request URL in SlackAPI bot settings. 

### Interacting with the App

1. Mention the bot in a Slack channel to initiate interaction.

2. The bot will guide you through different study options:

   - Choose a certification you are studying for.
   - Select the type of help you need (practice quiz, flashcards, or general questions).

3. The bot will provide assistance based on your selections.

## Extending the App

### Adding More Study Options

You can extend the app to include additional study options by following these steps:

1. Create functions for the new study options.

2. Update the `MENU_OPTIONS` dictionary in `app.py` to include the new options.

3. Modify the event listener logic in `app.py` to handle the new study options.

## Future Development

The app has some potential future enhancements:

- Integrate a structure to allow the bot to retrieve user chat history.
- Implement user-specific chat history to optimize assistance.
- Develop concept flashcards using vectorstore and langchain.
- Add more study options to the menu for comprehensive support.
