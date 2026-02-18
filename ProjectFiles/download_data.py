import os
import sys
import zipfile
from dotenv import load_dotenv

DATASET = "berkerisen/wind-turbine-scada-dataset"
DATA_DIR = "data"
ZIP_NAME = "wind-turbine-scada-dataset.zip"
LOCK_FILE = os.path.join(DATA_DIR, ".dataset.lock")


def load_env():
    load_dotenv()
    username = os.getenv("KAGGLE_USERNAME")
    key = os.getenv("KAGGLE_KEY")

    if not username or not key:
        print("❌ Kaggle credentials not found in .env file.")
        sys.exit(1)


def dataset_already_downloaded():
    return os.path.exists(LOCK_FILE)


def create_lock_file():
    with open(LOCK_FILE, "w") as f:
        f.write("Dataset successfully downloaded.\n")


def download_data():
    os.makedirs(DATA_DIR, exist_ok=True)

    if dataset_already_downloaded():
        print("✅ Dataset already downloaded. Skipping.")
        return

    print("⬇ Downloading dataset...")
    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()
    api.dataset_download_files(DATASET, path=DATA_DIR, unzip=True)
    '''
        zip_path = os.path.join(DATA_DIR, ZIP_NAME)

        print("📦 Extracting dataset...")
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(DATA_DIR)

        os.remove(zip_path)
    '''
    create_lock_file()
    print("✅ Dataset ready.")


if __name__ == "__main__":
    load_env()
    download_data()
