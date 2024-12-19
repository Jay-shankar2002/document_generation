import sqlite3

def setup_database():
    """
    Sets up the database with a table for storing template metadata.
    """
    conn = sqlite3.connect('templates.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            file_path TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_template(name, description, file_path):
    """
    Adds a new template record to the database.

    Args:
        name (str): Template name.
        description (str): Template description.
        file_path (str): Path to the template file.
    """
    conn = sqlite3.connect('templates.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO templates (name, description, file_path)
        VALUES (?, ?, ?)
    ''', (name, description, file_path))
    conn.commit()
    conn.close()

def get_templates():
    """
    Retrieves all templates from the database.
    
    Returns:
        List of tuples containing template metadata (name, description, file_path).
    """
    conn = sqlite3.connect('templates.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM templates")
    templates = cursor.fetchall()
    conn.close()
    return templates
