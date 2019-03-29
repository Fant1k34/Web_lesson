import sqlite3

class Help:
    def new_base():
        conn = sqlite3.connect('./files/base.db')
        
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS auth   ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                           login TEXT, 
                                                           Hash TEXT, 
                                                           level INTEGER ) ''')
        
        cur.execute(''' INSERT INTO auth (login, Hash, level) VALUES ('nikitadukin', 'abc123', 0) ''')
        
        
        conn.commit()
        cur.close()
        conn.close()
        
        conn = sqlite3.connect('./files/base.db')
        
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS info   ( l_id INTEGER, 
                                                           path TEXT, 
                                                           text TEXT, 
                                                           name TEXT,
                                                           description TEXT) ''')
        cur.execute(''' INSERT INTO info VALUES (1, '/somepath', 't1', 'algebra', '10 form') ''')
        cur.execute(''' INSERT INTO info VALUES (2, '/somepath', 'tt1', 'algebra', '11 form') ''')
        cur.execute(''' INSERT INTO info VALUES (1, '/somepath', 't2', 'algebra', '10 form') ''')
        cur.execute(''' INSERT INTO info VALUES (1, '/somepath', '2t', 'English', '10 form') ''')
        conn.commit()
        cur.close()
        conn.close()
        
        
    def exists(user_name, password_hash):
        conn = sqlite3.connect('./files/base.db')
        
        cur = conn.cursor() 
        
        
        cur.execute("SELECT * FROM auth WHERE login = ? AND Hash = ?",
                       (user_name, password_hash))
        row = cur.fetchone()
        cur.close()
        conn.close()    
        
        return (True, row[0]) if row else (False,)
    
    
    def watch(user_name, password_hash):
        
        if exists(user_name, password_hash)[0]:
            conn = sqlite3.connect('./files/base.db')
            cur = conn.cursor()
            cur.execute("SELECT * FROM info WHERE l_id = ?",
                           str(exists(user_name, password_hash)[1]))
            row = cur.fetchall()
            cur.close()
            conn.close()  
            return row
        
        
        
    def open_s(user_name, password_hash, subj):
        if exists(user_name, password_hash)[0]:
            conn = sqlite3.connect('./files/base.db')
            
            cur = conn.cursor()
            cur.execute("SELECT * FROM info WHERE l_id = ? AND name = ?",
                           (str(exists(user_name, password_hash)[1]), subj))
            row = cur.fetchall()
            cur.close()
            conn.close()  
            return row    
    
    
    def add(user_name, password_hash, path, text, name, description):
        if exists(user_name, password_hash)[0]:
            conn = sqlite3.connect('./files/base.db')
            
            cur = conn.cursor()
            cur.execute(''' INSERT INTO info VALUES ({}, '{}', '{}', '{}', '{}') '''.format(str(exists(user_name, password_hash)[1]), path, text, name, description))
            conn.commit()
            cur.close()
            conn.close()
            print(watch(user_name, password_hash))
    
    
    def delete(user_name, password_hash, name):
        if exists(user_name, password_hash)[0]:
            conn = sqlite3.connect('./files/base.db')
            
            cur = conn.cursor()
            cur.execute(''' DELETE FROM info WHERE name = '{}' '''.format(name))
            conn.commit()
            cur.close()
            conn.close()
            print(watch(user_name, password_hash))