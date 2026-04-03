import os
import site
import sys


def get_package_location() -> str:
    try:
        return site.getsitepackages()[0]
    except Exception:
        return os.path.join(
            sys.prefix,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            "site-packages",
        )


def detect_matrix_environment() -> None:
    try:
        is_venv = sys.prefix != sys.base_prefix
        current_python = sys.executable

        if is_venv:
            venv_path = sys.prefix
            venv_name = os.path.basename(venv_path)

            try:
                package_path = site.getsitepackages()[0]
            except Exception:
                package_path = os.path.join(
                    venv_path, "lib",
                    f"python{sys.version_info.major}.{sys.version_info.minor}",
                    "site-packages"
                )

            print("MATRIX STATUS: Welcome to the construct")
            print(f"Current Python: {current_python}")
            print(f"Virtual Environment: {venv_name}")
            print(f"Environment Path: {venv_path}")
            print("\nSUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print("\nPackage installation path:")
            print(package_path)

        else:
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {current_python}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")

            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate # On Windows")

            print("\nThen run this program again.")

    except Exception as e:
        print(f"ERROR: A glitch occurred in the Matrix: {e}")


if __name__ == "__main__":
    detect_matrix_environment()
