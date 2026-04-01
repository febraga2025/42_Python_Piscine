import sys
import os
import site


def detect_matrix_environment() -> None:
    """
    Detects the Python environment using only authorized modules: sys, os, site.
    """
    try:
        # Detectando se estamos no Construct (Venv)
        is_venv = sys.prefix != sys.base_prefix
        current_python = sys.executable

        if is_venv:
            # --- MODO: INSIDE THE CONSTRUCT ---
            venv_path = sys.prefix
            venv_name = os.path.basename(venv_path)

            # Usando o módulo 'site' que é autorizado para pegar os pacotes
            # site.getsitepackages() retorna uma lista. Pegamos o primeiro item.
            try:
                package_path = site.getsitepackages()[0]
            except Exception:
                # Fallback manual usando 'os' e 'sys' caso o site falhe
                # Isso respeita a estrutura do Python em ambientes Unix
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
            # --- MODO: OUTSIDE THE MATRIX ---
            print("MATRIX STATUS: You're still plugged in")
            print(f"Current Python: {current_python}")
            print("Virtual Environment: None detected")
            print("\nWARNING: You're in the global environment!")
            print("The machines can see everything you install.")
            print("\nTo enter the construct, run:")
            
            # Detectando SO com 'os.name' (também autorizado)
            if os.name == 'nt':  # Windows
                print("python -m venv matrix_env")
                print("matrix_env\\Scripts\\activate")
            else:  # Unix (Linux/Mac)
                print("python3 -m venv matrix_env")
                print("source matrix_env/bin/activate")
            
            print("\nThen run this program again.")

    except Exception as e:
        # Handling exceptions gracefully as requested in Chapter III.1
        print(f"ERROR: A glitch occurred in the Matrix: {e}")


if __name__ == "__main__":
    detect_matrix_environment()