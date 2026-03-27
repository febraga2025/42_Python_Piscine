import sys
import os
import site

def detect_matrix_environment() -> None:
    """
    Detecta se o script está rodando em um ambiente virtual (Construct)
    ou no ambiente global (Matrix) e exibe o relatório correspondente.
    """
    try:
        # Comparação entre o prefixo atual e o prefixo base do sistema
        # Se forem diferentes, estamos em um ambiente virtual (venv)
        is_venv = sys.prefix != sys.base_prefix
        
        # Obtém o caminho do executável Python atual
        current_python = sys.executable

        if is_venv:
            # --- MODO: INSIDE THE CONSTRUCT ---
            venv_path = sys.prefix
            venv_name = os.path.basename(venv_path)
            
            # Tenta capturar o caminho do site-packages de forma dinâmica
            try:
                package_path = site.getsitepackages()[0]
            except Exception:
                # Fallback caso getsitepackages falhe em algumas plataformas
                package_path = f"{venv_path}/lib/python{sys.version_info.major}.{sys.version_info.minor}/site-packages"

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
            print("python3 -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print("matrix_env\\Scripts\\activate    # On Windows")
            print("\nThen run this program again.")

    except Exception as e:
        print(f"ERROR: A glitch occurred in the Matrix: {e}")

if __name__ == "__main__":
    detect_matrix_environment()
    