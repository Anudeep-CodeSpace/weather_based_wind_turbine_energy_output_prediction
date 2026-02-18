# Entry point and router for the application.

import sys
import runpy
from pathlib import Path
from dotenv import load_dotenv

def run_script(path: str):
    script_path = Path(path)

    if not script_path.exists():
        print(f"[ERROR] Script not found: {script_path}")
        sys.exit(1)

    print(f"\n========== Running: {script_path} ==========\n")

    # Executes the script as if run with: python script.py
    runpy.run_path(str(script_path), run_name="__main__")

    print(f"\n========== Finished: {script_path} ==========\n")

def train():
    run_script("download_data.py")
    run_script("wind turbine energy prediction.py")


def test():
    run_script("test_model.py")


def serve():
    run_script('flask_server/app.py')


if __name__ == "__main__":
    load_dotenv()  # Load environment variables from .env file
    if len(sys.argv) != 2:
        print("Usage: python main.py [train | test | serve | full]")
        sys.exit(1)

    command = sys.argv[1].lower()
    
    if command == "train":
        train()
    elif command == "test":
        test()
    elif command == "serve":
        serve()
    elif command == "full":
        train()
        test()
        serve()
    else:
        print("Invalid command. Use 'train', 'test', or 'serve'.")
        sys.exit(1)
