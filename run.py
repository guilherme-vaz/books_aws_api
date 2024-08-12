from src.main.server.server import app
# from src.models.settings.db_connection_handler import table

if __name__ =="__main__":        
    app.run(host="0.0.0.0", port=3000, debug=True)