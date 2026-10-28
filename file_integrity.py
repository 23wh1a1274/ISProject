
import hashlib
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATABASE_FILE = BASE_DIR / "hashes.json"


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


def load_hashes():
    if DATABASE_FILE.exists():
        try:
            with open(DATABASE_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Error: Could not read the hash database.")
            return None

    return {}


def save_hashes(hashes):
    try:
        with open(DATABASE_FILE, "w", encoding="utf-8") as file:
            json.dump(hashes, file, indent=4)
        return True
    except OSError as error:
        print(f"Error saving hashes: {error}")
        return False


def get_file_path():
    raw_path = input("Enter the file path: ").strip().strip('"')
    path = Path(raw_path).expanduser()

    if not path.is_absolute():
        path = Path.cwd() / path

    return path.resolve()


def register_file():
    path = get_file_path()

    if not path.is_file():
        print("Error: File does not exist.")
        return

    hashes = load_hashes()
    if hashes is None:
        return

    try:
        file_hash = calculate_sha256(path)
        hashes[str(path)] = file_hash

        if save_hashes(hashes):
            print("\nFile registered successfully!")
            print(f"File: {path.name}")
            print(f"SHA-256: {file_hash}")
    except OSError as error:
        print(f"Error reading file: {error}")


def verify_file():
    path = get_file_path()

    if not path.is_file():
        print("Error: File does not exist.")
        return

    hashes = load_hashes()
    if hashes is None:
        return

    stored_hash = hashes.get(str(path))

    if stored_hash is None:
        print("File not registered. Register it first.")
        return

    try:
        current_hash = calculate_sha256(path)

        print(f"\nStored hash:  {stored_hash}")
        print(f"Current hash: {current_hash}")

        if current_hash == stored_hash:
            print("\nRESULT: INTEGRITY VERIFIED - File is unchanged.")
        else:
            print("\nRESULT: WARNING - File has been modified!")
    except OSError as error:
        print(f"Error reading file: {error}")


def main():
    while True:
        print("\n===== FILE INTEGRITY VERIFICATION SYSTEM =====")
        print("1. Register a file")
        print("2. Verify file integrity")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            register_file()
        elif choice == "2":
            verify_file()
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
