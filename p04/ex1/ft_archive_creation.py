#!/usr/bin/env python3

def create_archive() -> None:

    filename = "new_discovery.txt"

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")

    try:
        vault = open(filename, "w")
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        entry1 = "[ENTRY 001] New quantum algorithm discovered\n"
        entry2 = "[ENTRY 002] Efficiency increased by 347%\n"
        entry3 = "[ENTRY 003] Archived by Data Archivist trainee\n"

        vault.write(entry1)
        vault.write(entry2)
        vault.write(entry3)

        print(entry1.rstrip())
        print(entry2.rstrip())
        print(entry3.rstrip())

        vault.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except PermissionError:
        print("ERROR: Security protocols deny write access to this location.")
    except OSError:
        print("ERROR: System failure during data inscription.")


if __name__ == "__main__":
    create_archive()
