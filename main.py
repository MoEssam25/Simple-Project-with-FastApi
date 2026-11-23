import uvicorn
# We say I wanna use this webserver

if __name__ == "__main__":
    # First app is the folder second one is the file third one is the var app
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)
    # And I wanna run app file in the app folder with calling the app variable (app = FastAPI())
    # host="0.0.0.0" means run it on any available domain which means local hostapp
    # (What is the funcion of the port ?)
    # Reload means everytime I make a change to the file the server is shut down and restart
    #  
