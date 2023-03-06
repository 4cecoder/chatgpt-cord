# ChatGPT-Cord

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://www.buymeacoffee.com/4cecoder)

![image](https://user-images.githubusercontent.com/88108711/223172044-a1af5641-a540-4763-bb28-39265db8c5ec.png)

ChatGPT-Cord is a Discord chatbot powered by OpenAI's ChatGPT API.

It can be used to generate human-like responses to user queries and engage in natural language conversations.

## Usage

To use ChatGPT-Cord, simply type the command "!ask" followed by your question or statement in a Discord chat channel where the bot is present. For example:

 `!ask What is the capital of France?`

The bot will then process your input and generate a response based on its training and context. The response will be posted in the same channel where the command was issued.

## Configuration

1. Create account on [OpenAI's ChatGPT](https://chat.openai.com/)
2. Save your email and password

### authentication config file location

`mkdir -p ~/.config/revChatGPT/ && touch ~/.config/revChatGPT/config.json`

### Next add one of the following methods to link your OPENAI Account to the `~/.config/revChatGPT/config.json`

### Authentication method: (Choose 1)
#### - Email/Password
Not supported for Google/Microsoft accounts
```json
{
  "email": "email",
  "password": "your password"
}
```
#### - Session token
Comes from cookies on chat.openai.com as "__Secure-next-auth.session-token"

```json
{
  "session_token": "..."
}
```
#### - Access token
https://chat.openai.com/api/auth/session
```json
{
  "access_token": "<access_token>"
}
```

#### - Optional configuration:

```json
{
  "conversation_id": "UUID...",
  "parent_id": "UUID...",
  "proxy": "...",
  "paid": false
}
```

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



3. Save this as `$HOME/.config/revChatGPT/config.json`
4. If you are using Windows, you will need to create an environment variable named ```HOME``` and set it to your home profile for the script to be able to locate the config.json file.

## Credits

- ChatGPT-Cord was created by [4cecoder](https://github.com/4cecoder/) and is based on the OpenAI GPT 3.5 language model. 
- ChatGPT-Cord would not be possible without the incredible natural language processing capabilities of the [OpenAI](https://openai.com/) ChatGPT model. We are grateful for their contributions to the field of AI and machine learning.
- Thanks to [Antonio Cheong](https://github.com/acheong08) who reverse engineered the chatGPT API.
- Thanks to [Rajtilak Bhattacharjee](https://github.com/rajtilakjee) for good documentation sections that I borrowed.

## Support

If you have any questions, issues, or suggestions for improvement, please feel free to open an issue in the GitHub repository or contact me directly. Thanks for using ChatGPT-Cord!

### Licence

MIT license with exceptions. See the full license for details.

Copyright (c) 2023-present, Rajtilak Bhattacharjee

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
