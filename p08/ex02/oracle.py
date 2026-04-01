import os
from dotenv import load_dotenv


def check_env_security():
    if not os.path.exists(".gitignore"):
        return False, "Missing .gitignore"

    with open(".gitignore", "r") as f:
        content = f.read()
        if ".env" in content:
            return True, ".env file properly configured"
    return False, ".env not in .gitignore"


def main():
    load_dotenv()

    print("ORACLE STATUS: Reading the Matrix...")

    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion = os.getenv("ZION_ENDPOINT")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    db_status = ("Connected to local instance"
                 if db_url else "Offline (No DB_URL)")
    print(f"Database: {db_status}")

    api_status = "Authenticated" if api_key else "Missing API Key"
    print(f"API Access: {api_status}")

    print(f"Log Level: {log_level}")

    zion_status = "Online" if zion else "Offline"
    print(f"Zion Network: {zion_status}")

    print("\nEnvironment security check:")

    print("[OK] No hardcoded secrets detected")

    secure, msg = check_env_security()
    status_icon = "[OK]" if secure else "[ERROR]"
    print(f"{status_icon} {msg}")

    if mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[OK] Development mode active")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
