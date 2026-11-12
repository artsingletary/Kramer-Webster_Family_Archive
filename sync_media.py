from pathlib import Path
import subprocess
import argparse

# Project configuration
BASE_DIR = Path(__file__).resolve().parent

S3_BUCKET = "kramer-webster-archive-media"
AWS_PROFILE = "genealogy-archive"

def sync_directory(local_dir, s3_prefix, dry_run=True):
    """Synchronize a local directory with an S3 location."""

    command = [
        "aws",
        "s3",
        "sync",
        str(local_dir),
        f"s3://{S3_BUCKET}/{s3_prefix}/",
        "--profile",
        AWS_PROFILE,
        "--exclude",
        ".DS_Store",
    ]

    if dry_run:
        command.append("--dryrun")

    print(f"\nSynchronizing {local_dir.name}...")
    subprocess.run(command, check=True)

def main():
    """Synchronize photographs and documents with AWS S3."""

    parser = argparse.ArgumentParser(
        description="Synchronize genealogy media with AWS S3."
    )

    parser.add_argument(
        "--upload",
        action="store_true",
        help="Upload files to S3 instead of performing a dry run."
    )

    args = parser.parse_args()
    dry_run = not args.upload

    print("KRAMER-WEBSTER MEDIA SYNCHRONIZATION")
    print("===================================")

    if dry_run:
        print("Mode: DRY RUN (preview only)")
    else:
        print("Mode: LIVE UPLOAD")

    sync_directory(BASE_DIR / "photos", "photos", dry_run)
    sync_directory(BASE_DIR / "documents", "documents", dry_run)

    print("\nMedia synchronization completed.")


if __name__ == "__main__":
    main()
