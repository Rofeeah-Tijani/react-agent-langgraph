# Multi-Tool ReAct AI Agent using LangGraph, Groq and FastAPI

## Overview

This project is a multi-tool AI agent built using LangGraph and LangChain that follows the ReAct (Reason + Act) agent architecture.

Unlike a traditional chatbot that only generates text responses, this agent is capable of reasoning about user requests, selecting the appropriate tool, executing actions, and returning the final result.

The agent uses Groq as the Large Language Model provider and LangGraph to manage the workflow between the reasoning layer and external tools.

The system is exposed through a FastAPI backend, making it accessible as an API service.

---

## Core Concept

The agent follows the ReAct pattern:

1. Receive user input
2. Analyze the request
3. Decide whether a tool is required
4. Select the appropriate tool
5. Execute the tool
6. Use the returned result to generate the final response

This allows the AI system to interact with external services and perform real-world tasks beyond text generation.

---

## Architecture

```
User
 |
 v
FastAPI Server
 |
 v
LangGraph Agent
 |
 v
Groq LLM
 |
 +----------------------+
 |                      |
 v                      v
Tool Selection     Response Generation
 |
 +------------------------------------------------+
 |        |          |          |          |
 v        v          v          v          v

Calculator Weather  News   Files  Translator

 |
 +---------------------------------------------+
 |          |             |                    |
 v          v             v                    v

Email   Calendar     Reminder          Database Query

```

---

## Technologies Used

### Programming Language
- Python

### AI Frameworks
- LangChain
- LangGraph

### Large Language Model Provider
- Groq API

### Backend Framework
- FastAPI

### External APIs
- Weather API
- News API
- Google APIs

### Environment Management
- python-dotenv

---

# Features

## ReAct Agent

The agent can reason about requests and determine when external tools are required.

It dynamically selects the appropriate tool instead of requiring manual routing.

---

# Available Tools

## 1. Calculator Tool

### Purpose
Performs mathematical calculations.

### Function
- Evaluates mathematical expressions
- Handles arithmetic operations
- Returns calculated results

---

## 2. Weather Tool

### Purpose
Provides real-time weather information.

### Function
- Connects with weather API services
- Retrieves current weather conditions
- Returns temperature and weather descriptions

---

## 3. News Tool

### Purpose
Retrieves current news information.

### Function
- Searches for recent articles
- Fetches news data from external sources
- Returns relevant news information

---

## 4. Web Search Tool

### Purpose
Allows the agent to search the web for information.

### Function
- Performs online searches
- Retrieves external information
- Helps answer queries requiring updated knowledge

---

## 5. File Writer Tool

### Purpose
Creates and writes files.

### Function
- Generates new files
- Writes user-provided content
- Stores information locally

---

## 6. File Reader Tool

### Purpose
Reads existing files.

### Function
- Opens stored files
- Extracts file content
- Returns information to the agent

---

## 7. PDF Reader Tool

### Purpose
Processes PDF documents.

### Function
- Reads PDF files
- Extracts text content
- Allows the agent to work with documents

---

## 8. Translation Tool

### Purpose
Translates text between languages.

### Function
- Converts text from one language to another
- Supports multilingual interactions

---

## 9. Email Tool

### Purpose
Handles email-related actions.

### Function
- Sends emails through configured services
- Automates communication tasks

---

## 10. Calendar Tool

### Purpose
Manages calendar events.

### Function
- Creates calendar events
- Helps schedule activities
- Integrates with calendar services

---

## 11. Reminder Tool

### Purpose
Creates reminders.

### Function
- Stores reminder tasks
- Helps users remember important activities

---

## 12. Database Query Tool

### Purpose
Interacts with databases.

### Function
- Executes database queries
- Retrieves stored information
- Allows the agent to work with structured data

---

# Project Structure

```
react_agent_project/

│
├── agent.py
├── server.py
├── tools.py
├── test_agent.py
├── test_tools.py
├── requirements.txt
├── README.md
├── .env
│
└── tools/
    ├── calculator.py
    ├── weather.py
    ├── news.py
    ├── translator.py
    ├── files.py
    ├── reminder.py
    ├── database.py
    └── other tools

```

---

# Environment Variables

Create a `.env` file:

```
GROQ_API_KEY=

WEATHER_API_KEY=

NEWS_API_KEY=

GOOGLE_CLIENT_ID=

GOOGLE_CLIENT_SECRET=

DATABASE_URL=
```

These variables store credentials required for external services.

---

# Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate into the project:

```bash
cd react_agent_project
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

## Test Tools

Run individual tool tests:

```bash
python test_tools.py
```

---

## Test Agent

Run full agent testing:

```bash
python test_agent.py
```

---

## Start API Server

Run FastAPI:

```bash
python -m uvicorn server:app --reload
```

API documentation:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## Chat Endpoint

```
POST /chat
```

The endpoint receives user messages and sends them through the LangGraph agent.

---

# Error Handling

The project includes handling for:

- API failures
- Invalid tool inputs
- External service errors
- Failed requests

This prevents tool failures from crashing the entire agent.

---

# Future Improvements

Possible improvements include:

- Add persistent long-term memory
- Add user authentication
- Add frontend chat interface
- Add Docker support
- Add monitoring and logging
- Add automated evaluation
- Improve database integration
- Deploy to cloud infrastructure

---

# Learning Outcomes

This project demonstrates practical understanding of:

- AI agent development
- LLM tool calling
- LangGraph workflows
- API integrations
- Backend development
- AI system architecture
- Production-style AI applications

---

## Author

Tijani Rofee'ah Feyishara
