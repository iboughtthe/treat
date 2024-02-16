Telegram Dialog Scraper
This Python script scrapes the dialogs (conversations) from a Telegram account and prints the name and message of each dialog. The script uses the telethon library to connect to the Telegram API and retrieve the dialogs.
Prerequisites
To run this script, you need to have the following dependencies installed:

Python 3.x
telethon Python library
You can install the telethon library using pip:

Edit
Download
Copy code
pip install telethon
Configuration
Before running the script, you need to create a config.json file in the same directory as the script with the following contents:

json
Edit
Download
Copy code
{
    "API_ID": "<your_api_id>",
    "API_HASH": "<your_api_hash>",
    "BOT_TOKEN": "<your_bot_token>"
}
Replace <your_api_id>, <your_api_hash>, and <your_bot_token> with your actual Telegram API ID, API hash, and bot token, respectively.

Usage
To run the script, simply execute the main.py file:

Edit
Download
Copy code
python main.py
This will retrieve the list of dialogs from the Telegram client and print the name and message of each dialog.

Heroku Deployment
You can also deploy this script to Heroku using the following steps:

Create a new Heroku app from the Heroku Dashboard or CLI.
Connect the app to your local Git repository using the Heroku CLI:
Edit
Download
Copy code
heroku git:remote -a <heroku-app-name>
Replace <heroku-app-name> with the name of your Heroku app.

Create a new Procfile in the root directory of your project with the following contents:
Edit
Download
Copy code
worker: python main.py
Add and commit the changes to your local Git repository:
Edit
Download
Copy code
git add .
git commit -m "Add Heroku configuration files"
Push the changes to Heroku:
Edit
Download
Copy code
git push heroku main
Replace main with the name of your Git branch if it's different.

Once the app is deployed, you can open it in a web browser using the following command:
Edit
Download
Copy code
heroku open
This will open the app in your default web browser, allowing you to test its functionality.

Contributing
Contributions to this project are welcome. To get started, fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License.

Deploy Button
<a href="https://heroku.com/deploy?template=https://github.com/<iboughtthe>/telegram-dialog-scraper.git"><img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy to Heroku"></a>
