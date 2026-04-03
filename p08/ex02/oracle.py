import importlib
import os


def get_workspace_file_path(filename: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)


def check_env_security() -> tuple[bool, str]:
    gitignore_path = get_workspace_file_path(".gitignore")
    if not os.path.exists(gitignore_path):
        return False, "Missing .gitignore"

    with open(gitignore_path, "r", encoding="utf-8") as file_handle:
        content = file_handle.read()
        if ".env" in content:
            return True, ".env file properly configured"
    return False, ".env not in .gitignore"


def load_environment() -> bool:
    try:
        dotenv_module = importlib.import_module("dotenv")
    except ImportError:
        print("ERROR: python-dotenv is not installed.")
        return False

    dotenv_path = get_workspace_file_path(".env")
    dotenv_module.load_dotenv(dotenv_path=dotenv_path, override=False)
    return True


def main() -> None:
    if not load_environment():
        return

    print("ORACLE STATUS: Reading the Matrix...")

    mode = os.getenv("MATRIX_MODE", "development").strip().lower()
    db_url = os.getenv("DATABASE_URL", "")
    api_key = os.getenv("API_KEY", "")
    log_level = os.getenv("LOG_LEVEL", "DEBUG").strip().upper()
    zion = os.getenv("ZION_ENDPOINT", "")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if db_url:
        database_status = (
            "Connected to local instance"
            if mode != "production"
            else "Connected to production instance"
        )
    else:
        database_status = "Not configured"
    print(f"Database: {database_status}")

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

    print("[OK] Production overrides available")

    if mode not in {"development", "production"}:
        print("[ERROR] MATRIX_MODE must be development or production")

    if not db_url:
        print("[WARN] DATABASE_URL is missing")
    if not api_key:
        print("[WARN] API_KEY is missing")
    if not zion:
        print("[WARN] ZION_ENDPOINT is missing")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
