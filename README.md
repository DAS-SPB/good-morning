# Telegram Bot AIOgram

Telegram bot built for a single user, using OpenAI and CatAPI integration.

Pet project implemented using AIOgram, MongoDB.

Currently deployed on Google Cloud Platform.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Usage](#usage)
    - [Running the Application](#running-the-application)
- [Potential Improvements](#potential-improvements)

## Features

- User id validation. Implemented via middleware
- Scheduled messages with inline keyboard every morning if chat is active
- Integration with CatAPI to fetch photos
- Integration with OpenAI to make conversation with bot more meaningful
- Using MongoDB to keep chat state and phrases for daily messages private
- Sending error logs to email has been implemented
- Aiogram was used for educational purposes; this project does not require extensive asynchronous capabilities since it
  is intended for a single user
- Simple and straightforward project structure

## Project Structure

The project follows the following directory structure:

```
good-morning/
├── config/
│   ├── config
├── db
│   ├── connection
│   ├── database
├── external_api
│   ├── cats
│   ├── openai
├── handlers
│   ├── other_handlers
├── lexicon
│   ├── lexicon
├── logging_settings
│   ├── logging_config
│   ├── logging_config.example
│   ├── logging_module
├── middlewares
│   ├── outer
├── notifications
│   ├── motifications
│   ├── scheduller
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
```

- `config`: Contains configuration model for Bot, DB and external API interaction.
- `db`: Database connection and interaction.
- `external_api`: Contains interaction logic with external APIs.
- `handlers`: Handlers to route received messages and manage responses.
- `lexicon`: Allows to use some not private phrases without MongoDB.
- `logging_settings`: Settings to manage log level, format, handlers, output mode.
- `middleware`: Custom middleware to bloc any other user except 'Main user'.
- `notifications`: Allows to manage schedule of notification and it's payload.
- `.env`: Store environment variables (e.g., database credentials).
- `.env.example`: Example of .env file structure. To keep .env values private.
- `.gitignore`: Lists files and directories to be ignored by version control system.
- `main`: Entrance point. Allows to assemble all modules together.
- `README.md`: Documentation about the project.
- `requirements.txt`: List of project dependencies.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- Python 3.10+ (3.12 recommended).
- MongoDB.

### Installation

1. Create a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Clone the repository:

   ```bash
   git clone https://github.com/DAS-SPB/good-morning.git
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To run application locally, you can just run `main.py`:

```bash
python3 main.py
```

## Potential improvements


This bot can be adapted to support multiple users.
