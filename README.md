# ChatGPT-Cord

ChatGPT-Cord is a Discord chatbot powered by OpenAI's GPT language model. It can be used to generate human-like responses to user queries and engage in natural language conversations.

## Usage

To use ChatGPT-Cord, simply type the command "!ask" followed by your question or statement in a Discord chat channel where the bot is present. For example:

 `!ask What is the capital of France?`

The bot will then process your input and generate a response based on its training and context. The response will be posted in the same channel where the command was issued.

## Installation

To use ChatGPT-Cord, you will need to create a Discord bot account and obtain its token. You will also need to have Python 3.6 or higher installed on your system.



1. Clone this repository to your local machine.
2. Install the required Python packages by running the following command in the terminal:

`git clone https://github.com/4cecoder/chatgpt-cord/`

`pip install -r requirements.txt`


3. Set the environment variable `DISCORD_TOKEN` to the token of your Discord bot account.

`.env` file needs to be created that has `DISCORD_TOKEN=<paste your bot token>` for your bot


# To create a Discord bot, follow these steps:

    Create a Discord account or log in to your existing account at https://discord.com/.

    Go to the Discord Developer Portal at https://discord.com/developers/applications and click on "New Application" to create a new application.

    Give your application a name and click on "Create".

    On the next page, click on "Bot" in the left sidebar and then click on "Add Bot" to create a bot user for your application.

    Customize your bot user's name and avatar if desired.

    Copy the bot token by clicking on "Copy" under the "Token" section. Keep this token secret and do not share it with anyone.

    Invite your bot to a Discord server by replacing CLIENT_ID in the following link with your application's Client ID, which can be found under the "General Information" section:


4. Run the bot by executing the following command in the terminal:

`python main.py`

The bot will start listening for commands in all channels it has access to.


## Configuration


## Credits

ChatGPT-Cord was created by [4cecoder](https://github.com/4cecoder/) and is based on the OpenAI GPT 3.5 language model. 

### Licence
The code is released under the MIT License.

## Support

If you have any questions, issues, or suggestions for improvement, please feel free to open an issue in the GitHub repository or contact me directly. Thanks for using ChatGPT-Cord!
