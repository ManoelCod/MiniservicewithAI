import sqlite3

DB_NAME = 'messages.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Tabela de histórico
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            user_message TEXT,
            ai_response TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Tabela de erros
    c.execute('''
        CREATE TABLE IF NOT EXISTS errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone TEXT,
            user_message TEXT,
            error_message TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

def save_message_pair(phone, user_message, ai_response, whatsapp_link=None):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO messages (phone, user_message, ai_response, whatsapp_link)
        VALUES (?, ?, ?, ?)
    ''', (phone, user_message, ai_response, whatsapp_link))
    conn.commit()
    conn.close()


def get_last_messages(limit=10):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT phone, user_message, ai_response, whatsapp_link, timestamp
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
            'whatsapp_link': row[3],
            'timestamp': row[4]
        }
        for row in rows
    ]

def save_error(phone, user_message, error_message):
    """Armazena um erro ocorrido durante o processamento."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO errors (phone, user_message, error_message)
        VALUES (?, ?, ?)
    ''', (phone, user_message, error_message))
    conn.commit()
    conn.close()

def get_last_errors(limit=10):
    """Retorna os últimos erros registrados."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        SELECT phone, user_message, error_message, timestamp
        FROM errors
        ORDER BY timestamp DESC
        LIMIT ?
    ''', (limit,))
    rows = c.fetchall()
    conn.close()
    return [
        {
            'phone': row[0],
            'user_message': row[1],
            'error_message': row[2],
            'timestamp': row[3]
        }
        for row in rows
    ]