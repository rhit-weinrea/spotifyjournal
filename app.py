from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory storage for journal entries (in a real app, use a database)
journal_entries = []

@app.route('/')
def index():
    """Main page with HTMX-powered journal interface"""
    return render_template('index.html', entries=journal_entries)

@app.route('/entries', methods=['GET'])
def get_entries():
    """HTMX endpoint to fetch all journal entries"""
    return render_template('partials/entries.html', entries=journal_entries)

@app.route('/entries', methods=['POST'])
def add_entry():
    """HTMX endpoint to add a new journal entry"""
    title = request.form.get('title', '')
    content = request.form.get('content', '')
    
    if title and content:
        entry = {
            'id': len(journal_entries) + 1,
            'title': title,
            'content': content,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        journal_entries.insert(0, entry)  # Add to beginning
        
    return render_template('partials/entries.html', entries=journal_entries)

@app.route('/entries/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    """HTMX endpoint to delete a journal entry"""
    global journal_entries
    journal_entries = [e for e in journal_entries if e['id'] != entry_id]
    return '', 200

@app.route('/search', methods=['POST'])
def search_entries():
    """HTMX endpoint to search journal entries"""
    query = request.form.get('query', '').lower()
    
    if query:
        filtered_entries = [
            e for e in journal_entries 
            if query in e['title'].lower() or query in e['content'].lower()
        ]
    else:
        filtered_entries = journal_entries
    
    return render_template('partials/entries.html', entries=filtered_entries)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
