from app import app

# Run the app
if __name__ == '__main__':
    app.run(port=app.config['PORT'])
