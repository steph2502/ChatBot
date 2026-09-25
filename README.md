# ChatBot

A lightweight AI chatbot built with **FastAPI** and the **Google Gemini API**.

The project explores how a generative AI model can be integrated into a backend application and exposed through an API for sending and receiving conversational messages.

## Overview

This project was built as a practical introduction to integrating Large Language Models (LLMs) into backend applications.

The application receives a user's message through a FastAPI endpoint, sends it to the Gemini API, and returns the generated response.

```text
User
  │
  ▼
FastAPI API
  │
  ▼
Gemini API
  │
  ▼
Generated Response
  │
  ▼
User
```

## Tech Stack

* **Python**
* **FastAPI** — backend API framework
* **Google Gemini API** — generative AI model
* **Uvicorn** — ASGI server

## How It Works

1. The user sends a message to the chatbot.
2. FastAPI receives the request.
3. The application passes the message to the Gemini API.
4. Gemini generates a response.
5. The response is returned through the API.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/steph2502/ChatBot.git
cd ChatBot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not commit your API key to the repository.

### 5. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

## Example Request

A request can be sent to the chatbot endpoint with a message such as:

```json
{
  "message": "Explain what an API is."
}
```

The application sends the message to Gemini and returns the generated response.

## What I Learned

Building this project helped me understand:

* Integrating external AI APIs into backend applications
* Building API endpoints with FastAPI
* Handling requests and responses in a backend service
* Managing API credentials with environment variables
* Working with generative AI models programmatically
* Structuring a simple AI-powered backend application

## Possible Improvements

Some areas I would explore as the project grows:

* Conversation history and multi-turn conversations
* Persistent chat sessions
* Streaming Gemini responses
* Authentication and user accounts
* Request validation and rate limiting
* Better error handling
* Frontend chat interface
* Conversation storage with PostgreSQL

## Project Status

This is a learning/project implementation focused on understanding the integration between **FastAPI and generative AI APIs**.

---

**Built with Python, FastAPI, and Gemini.**
