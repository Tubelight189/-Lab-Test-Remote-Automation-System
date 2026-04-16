#!/bin/bash

SOURCE_DIR="../data/landing"
DEST_DIR="../data/processing"
LOG_FILE="../logs/ingestion.log"

# Create log file if not exists
touch $LOG_FILE

echo "---- Ingestion Started at $(date) ----" >> $LOG_FILE

# Check if CSV files exist
if ls $SOURCE_DIR/*.csv 1> /dev/null 2>&1; then
    for file in $SOURCE_DIR/*.csv
    do
        mv "$file" $DEST_DIR/
        echo "Moved $(basename $file) at $(date)" >> $LOG_FILE
    done
else
    echo "No files found at $(date)" >> $LOG_FILE
fi

echo "---- Ingestion Completed ----" >> $LOG_FILE
