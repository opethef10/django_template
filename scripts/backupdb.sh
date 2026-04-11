#!/bin/bash
set -euo pipefail

# --- CONFIG / ENV -------------------------------------------------------------

# Get the absolute path of the script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$SCRIPT_DIR/.."
PROJECT_ROOT="$(cd "$PROJECT_ROOT" && pwd)"  # resolve absolute

echo "[INFO] Project root: $PROJECT_ROOT"

# Load only the PROJECT_SLUG from the .env file (absolute path)
ENV_FILE="$PROJECT_ROOT/.env"
if [[ ! -f "$ENV_FILE" ]]; then
    echo "[ERROR] .env file not found at $ENV_FILE"
    exit 1
fi

export $(grep -v '^#' "$ENV_FILE" | grep 'PROJECT_SLUG' | xargs)
echo "[INFO] PROJECT_SLUG: ${PROJECT_SLUG:-<not set>}"

# Absolute paths for backup folder and DB
BACKUP_FOLDER="$HOME/.backups"
mkdir -p "$BACKUP_FOLDER"
BACKUP_FOLDER="$(cd "$BACKUP_FOLDER" && pwd)"

DB_FILE="$PROJECT_ROOT/$PROJECT_SLUG.sqlite3"
BACKUP_FILE_PREFIX="$PROJECT_SLUG."
DB_EXTENSION=".sqlite3"

echo "[INFO] Backup folder: $BACKUP_FOLDER"
echo "[INFO] Database file: $DB_FILE"

# --- FUNCTIONS ----------------------------------------------------------------

get_file_mtime_formatted() { date -r "$1" +"%Y%m%d_%H%M%S"; }
get_file_mtime_epoch()     { date -r "$1" +"%s"; }

# --- FIND LATEST BACKUP --------------------------------------------------------

latest_backup=$(ls -1t "$BACKUP_FOLDER" \
    | grep "^${BACKUP_FILE_PREFIX}.*\.gz$" \
    | head -n 1 || true)

if [[ -n "$latest_backup" ]]; then
    echo "[DEBUG] Latest backup candidate: $BACKUP_FOLDER/$latest_backup"
else
    echo "[DEBUG] Latest backup candidate: <none>"
fi

# --- DECIDE IF BACKUP NEEDED ---------------------------------------------------

should_copy=true
db_mtime_epoch=$(get_file_mtime_epoch "$DB_FILE")

if [[ -n "$latest_backup" ]]; then
    latest_backup_file="$BACKUP_FOLDER/$latest_backup"
    backup_mtime_epoch=$(get_file_mtime_epoch "$latest_backup_file")

    if [[ "$db_mtime_epoch" -le "$backup_mtime_epoch" ]]; then
        should_copy=false
    fi
fi

# --- BACKUP --------------------------------------------------------------------

if $should_copy; then
    DATETIME_FORMAT=$(get_file_mtime_formatted "$DB_FILE")
    BACKUP_FILE="$BACKUP_FOLDER/$BACKUP_FILE_PREFIX$DATETIME_FORMAT$DB_EXTENSION"

    echo "[INFO] Creating a vacuumed backup..."
    echo "[INFO] Destination: $BACKUP_FILE.gz"

    sqlite3 "$DB_FILE" "VACUUM INTO '$BACKUP_FILE'"
    gzip "$BACKUP_FILE"

    echo "[INFO] Backup successfully created and compressed."
else
    echo "[INFO] No new backup needed - database not modified since last backup."
fi
