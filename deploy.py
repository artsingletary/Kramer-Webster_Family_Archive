import argparse
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def run_script(script_name, *args):
    script_path = BASE_DIR / script_name

    print(f"Running {script_name}...", flush=True)

    command = [sys.executable, str(script_path), *args]

    subprocess.run(
        command,
        cwd=BASE_DIR,
        check=True
    )

def main():
    parser = argparse.ArgumentParser(
        description="Deploy the Kramer-Webster Family Archive."
    )

    parser.add_argument(
        "--sort",
        action="store_true",
        help="Sort people and sources before building."
    )

    parser.add_argument(
        "--upload",
        action="store_true",
        help="Upload photos and documents to S3."
    )

    args = parser.parse_args()

    print("Starting Kramer-Webster deployment...")

    if args.sort:
        run_script("sort_people.py")
        run_script("sort_sources.py")

    if args.upload:
        run_script("sync_media.py", "--upload")
    else:
        run_script("sync_media.py")

        run_script("build_site.py")

        print("Deployment preparation completed successfully.")

if __name__ == "__main__":
    main()