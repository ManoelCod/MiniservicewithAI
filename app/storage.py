import sqlite3

DB_NAME = 'messages.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            user_message TEXT,
            ai_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_message_pair(phone, user_message, ai_response):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO messages (phone, user_message, ai_response)
        VALUES (?, ?, ?)
    ''', (phone, user_message, ai_response))
    conn.commit()
    conn.close()

def get_last_messages(limit=10):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT phone, user_message, ai_response, timestamp
        FROM messages
        ORDER BY timestamp DESC
        LIMIT ?
    ''', (limit,))
    rows = c.fetchall()
    conn.close()
    return [
        {
            'phone': row[0],
            'user_message': row[1],
            'ai_response': row[2],
            'timestamp': row[3]
        }
        for row in rows
    ]