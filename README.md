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
   git clone https://github.com/berniefusioncyber/gptcybertutor.git
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

   Replace `your_slack_bot_token`, `your_slack_signing_secret`, `your_slack_bot_user_id`, and `your_openai_api_key` with the actual bot credentials.

## Usage

### Running the App

To run the app, execute the following command:

```bash
python app.py
```

This will start the Flask development server, at `http://127.0.0.1:5000/`. Now either host a forwarding address using ngrok or other services to connect and deploy application.

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

## Future Development Potential Steps

The app has some potential future enhancements:

- Integrate a structure to allow the bot to retrieve user chat history.
- Implement user-specific chat history to optimize assistance.
- Develop concept flashcards using vectorstore and langchain.
- Add more study options to the menu for comprehensive support.

### Hosting the Application on AWS

#### Objective:
Deploy the study assistant app on AWS for online accessibility.

#### Steps:

1. Choose an AWS service:
   - Select an appropriate AWS service for hosting the Flask application (e.g., Amazon EC2, AWS Elastic Beanstalk).

2. Set up an EC2 instance (if applicable):
   - Configure a virtual machine instance with the required specifications.
   - Install necessary dependencies, including Python and packages listed in `requirements.txt`.

3. Configure security groups:
   - Define inbound and outbound rules for the instance's security group to allow access to the app.

4. Deploy the app:
   - Upload your application code and files to the instance.
   - Start the Flask application on the instance.

### Switching Between Different Certifications

#### Objective:
Allow users to switch between different certifications they are studying for.

#### Steps:

1. Update certification handling:
   - Modify the conversation state handling to account for certification selection.
   - Store certification choice in the user's context.

2. Add a certification menu:
   - Integrate a menu option that allows users to switch certifications.
   - Implement a function to display available certifications and handle user selection.

3. Adjust study materials:
   - Create data structures or databases that store certification-specific study materials.
   - Dynamically load content based on the user's chosen certification.

### Optimization of Functions for Switching

#### Objective:
Optimize app functions to handle switching between different certifications seamlessly.

#### Steps:

1. Modularize study materials:
   - Organize study materials (e.g., questions, flashcards) for each certification in separate modules or files.

2. Develop a switching mechanism:
   - Design a mechanism that facilitates smooth switching between certifications without data overlap.
   - Ensure that the user's progress and history for each certification are preserved.

3. Update interaction flows:
   - Adjust the conversation state logic to accommodate switching between certifications.
   - Allow users to switch certifications at any point during their interaction.

### Retrieving and Utilizing User Chat History

#### Objective:
Implement the capability for the bot to retrieve and utilize user chat history to enhance the study experience.

#### Steps:

1. Modify the conversation state handling:
   - Extend the `handle_mentions` function to store the conversation history for each user.
   - Store user-specific chat history in a data structure, e.g., a dictionary with user IDs as keys and chat histories as values.

2. Enhance interaction based on chat history:
   - Modify the chat logic to consider the user's chat history when responding.
   - Utilize the user's chat history to provide personalized assistance, review previous questions, and adapt responses.

3. Create an option to view chat history:
   - Add a menu option for users to request their chat history.
   - Implement a function that retrieves and displays the user's chat history upon request.

### User-Specific Chat History Storage

#### Objective:
Store and manage individual user chat histories for optimized study support.

#### Steps:

1. Update conversation state handling:
   - Extend the chat history storage to be user-specific, rather than global.
   - Modify the data structure to associate chat histories with user IDs.

2. User chat history management:
   - Implement functions to retrieve, update, and clear individual user chat histories.
   - Ensure that each user's chat history is accessible and modifiable only by the respective user.

### Concept Flashcards using Vectorstore and Langchain

#### Objective:
Provide concept flashcards as a study option, leveraging vectorstore and langchain for content generation and interaction.

#### Steps:

1. Gather terminology:
   - Compile a list of key terminology relevant to each certification.
   - Integrate a vocabulary extraction mechanism to select relevant terms from the documents.

2. Flashcard generation:
   - Create a function that randomly selects terms from the vocabulary.
   - Utilize langchain to generate flash

card-style questions and answers for each term.

3. Flashcard interaction:
   - Add a menu option for users to access concept flashcards.
   - Allow users to request random flashcards or select specific terms to study.

### Adding More Study Options to the Menu

#### Objective:
Expand the study options available in the menu to cover a wider range of study materials.

#### Steps:

1. Identify additional study materials:
   - Determine what other types of study materials would benefit users (e.g., practice exams, study guides, interactive simulations).

2. Implement new study option functions:
   - Create functions to handle the new study options, similar to the existing ones.
   - Develop appropriate interactions for each study option.

3. Update the menu options:
   - Extend the `MENU_OPTIONS` dictionary to include the new study options and their descriptions.

4. Modify the conversation state handling:
   - Integrate the new study options into the conversation state logic.
   - Allow users to choose from the new options within the interaction flow.
