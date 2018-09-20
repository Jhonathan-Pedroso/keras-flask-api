from src import app
from src.model import load_model


if __name__ == "__main__":
    load_model()
    app.run()
