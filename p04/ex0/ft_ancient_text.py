#!/usr/bin/env python3

def recover_data() -> None:

    filename = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        vault = open(filename, "r")
        print(f"Accessing Storage Vault: {filename}")
        print("Connection established...\n")

        content = vault.read()

        print("RECOVERED DATA:")
        print(content.rstrip())

        vault.close()
        print("\nData recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_data()
