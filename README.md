# spotifyjournal

A music journal web application built with **Python**, **Flask**, and **HTMX**.

## Features

- 🎵 Create and manage music journal entries
- ⚡ Dynamic content updates without page reloads (powered by HTMX)
- 🔍 Real-time search functionality
- 🗑️ Delete entries with confirmation
- 📱 Responsive design
- ✨ Smooth animations and transitions

## Tech Stack

- **Backend**: Python + Flask
- **Frontend**: HTML + HTMX + CSS
- **Architecture**: Server-side rendering with AJAX-like interactions

## Getting Started

### Prerequisites

- Python 3.7 or higher

### Installation

1. Clone the repository:
```bash
git clone https://github.com/rhit-weinrea/spotifyjournal.git
cd spotifyjournal
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

## How It Works

This application demonstrates the power of HTMX with Flask:

- **No JavaScript needed**: HTMX handles all dynamic interactions through HTML attributes
- **Server-side rendering**: All HTML is generated on the server
- **Partial updates**: Only the necessary parts of the page are updated
- **Real-time search**: Search results appear as you type with debouncing
- **Smooth UX**: Add and delete entries without page reloads

## HTMX Features Demonstrated

- `hx-post`: Submit forms via AJAX POST requests
- `hx-delete`: Delete resources via AJAX DELETE requests
- `hx-target`: Specify which element to update
- `hx-swap`: Control how content is swapped
- `hx-trigger`: Define when requests are triggered
- `hx-confirm`: Show confirmation dialogs
- `hx-on::after-request`: Execute code after requests complete

## Project Structure

```
spotifyjournal/
├── app.py                      # Flask application
├── requirements.txt            # Python dependencies
├── static/
│   └── css/
│       └── style.css          # Styling
├── templates/
│   ├── index.html             # Main page
│   └── partials/
│       └── entries.html       # Entry list partial
└── README.md
```

## License

MIT