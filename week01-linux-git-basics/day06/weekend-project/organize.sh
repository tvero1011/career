#!/bin/bash

# --------------------------
# Linux File Organizer Script
# --------------------------

LOGFILE="organize.log"
DATE=$(date "+%Y-%m-%d %H:%M:%S")

echo "=== File Organizer Started at $DATE ===" >> "$LOGFILE"

# Function: Create folder if it doesn't exist
create_folder() {
    if [ ! -d "$1" ]; then
        mkdir "$1"
        echo "[CREATED] $1/" >> "$LOGFILE"
    fi
}

# Create target folders
create_folder images
create_folder videos
create_folder documents
create_folder others

# Move files based on extension
for file in *; do
    if [ -f "$file" ]; then

        case "$file" in
            *.jpg|*.jpeg|*.png) 
                mv "$file" images/
                echo "[MOVED] $file → images/" >> "$LOGFILE"
                ;;
            
            *.mp4|*.mov) 
                mv "$file" videos/
                echo "[MOVED] $file → videos/" >> "$LOGFILE"
                ;;
            
            *.pdf|*.docx|*.txt)
                mv "$file" documents/
                echo "[MOVED] $file → documents/" >> "$LOGFILE"
                ;;

            *)
                mv "$file" others/
                echo "[MOVED] $file → others/" >> "$LOGFILE"
                ;;
        esac

    fi
done

echo "=== Organizer Finished ===" >> "$LOGFILE"
echo "Organization complete!"
