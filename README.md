# Elyx Chat Analysis

A web application that analyzes chat files and generates visual insights using LLM-powered analysis.

## Overview

Elyx Chat Analysis is a tool that processes chat text files to generate comprehensive health journey insights. The application extracts patient personas, health progress tracking, clinical decision analysis, and professional time tracking from conversation data.



## Features

- **Upload Interface**: Simple interface for uploading chat text files
- **Real-time Processing**: Visual feedback during analysis with task progress tracking
- **Interactive Dashboard**: Explore analysis results with an interactive tabbed interface
- **Regeneration**: Ability to regenerate specific analyses as needed

## Prerequisites

- Python 3.6+
- Flask
- Ollama (LLM inference engine)

## Installation

### 1. Clone the repository


### 2. Install Ollama

Download and install Ollama from the [official website](https://ollama.ai/download).

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Setup

### 1. Pull the LLM model

Run the following command to download the LLama 3 model:

```bash
ollama pull llama3:8b
```

### 2. Run the model

Ensure the Ollama service is running with the Llama 3 model available:

```bash
ollama run llama3:8b
```

This will start the Ollama service with the Llama 3 model loaded.

## Usage

### 1. Start the backend server

Run the Flask backend:

```bash
python backend.py
```

The server will start and display a URL (typically http://127.0.0.1:5000/).

### 2. Access the web interface

Open your browser and navigate to the URL shown in the terminal. Alternatively, you can press Ctrl+Click on the link in most terminal emulators to open it directly.

### 3. Upload a chat file

- Click "Choose Chat File" to select a text file containing the chat data
- Click "Process Chat" to begin analysis
- The system will display a progress screen as it processes the data

### 4. Explore the analysis

Once processing is complete, you'll be taken to an interactive dashboard with:

- **Patient Persona**: Detailed month-by-month patient state analysis
- **Health Progress**: Tracking of medical conditions and improvements
- **Decision Analysis**: Clinical decisions made throughout treatment
- **Resource Tracking**: Time spent by different healthcare professionals

## Project Structure

```
elyx/
├── app.py                # Main application file
├── backend.py            # Backend server with API routes
├── chat.txt              # Example chat file
├── static/               # Static assets
│   ├── index.html        # Upload interface
│   ├── loading.html      # Processing screen
│   └── interactive.html  # Analysis dashboard
├── templates/            # HTML templates
├── persona.txt           # System prompt for persona generation
├── progress.txt          # System prompt for progress analysis
├── decision.txt          # System prompt for decision analysis
└── track.txt             # System prompt for time tracking
```

## Customization

You can customize the system prompts by modifying the following files:
- `persona.txt` - Controls how personas are generated
- `progress.txt` - Controls health progress tracking
- `decision.txt` - Controls decision analysis extraction
- `track.txt` - Controls time tracking analysis

## Troubleshooting

- **Model not found error**: Ensure Ollama is running and the Llama 3 model is properly installed
- **File upload issues**: Check that your chat file is in plain text format (.txt)
- **Empty results**: Verify that your chat file contains sufficient data for analysis

## License

[MIT](LICENSE)

## Acknowledgements

- This project uses the [Ollama](https://ollama.ai/) inference engine
- UI powered by [Spline](https://spline.design/) for 3D backgrounds
- Powered by Llama 3 model from Meta
