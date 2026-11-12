import json
import shutil
from pathlib import Path

# File locations
BASE_DIR = Path(__file__).resolve().parent
SOURCES_FILE = BASE_DIR / "data" / "sources.json"
BACKUP_FILE = BASE_DIR / "data" / "sources_backup.json"

# Sort by date, then title
def sort_key(source):
    date = str(source.get("date") or "").strip()
    title = str(source.get("title") or "").lower()

    # Put sources without dates at the end
    if not date:
        return ("9999-12-31", title)

    # Convert year-only dates to YYYY-01-01
    if len(date) == 4 and date.isdigit():
        date = f"{date}-01-01"

    return (date, title)

def main():
    # Read the existing sources
    with open(SOURCES_FILE, "r", encoding="utf-8") as file:
        sources = json.load(file)

    # Verify the expected JSON structure
    if not isinstance(sources, list):
        raise ValueError("Expected sources.json to contain a list of sources.")

    # Sort sources by date, then title
    sorted_sources = sorted(sources, key=sort_key)

    # Back up the original file
    shutil.copy2(SOURCES_FILE, BACKUP_FILE)

    # Write the sorted records
    with open(SOURCES_FILE, "w", encoding="utf-8") as file:
        json.dump(sorted_sources, file, indent=4, ensure_ascii=False)
        file.write("\n")

    print(f"Successfully sorted {len(sorted_sources)} sources.")
    print(f"Backup created: {BACKUP_FILE}")


if __name__ == "__main__":
    main()
