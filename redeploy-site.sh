#!/bin/bash

LOGFILE=~/redeploy.log

{
  echo "Starting redeployment at $(date)"

  cd ~/audreychenportfolio || exit

  git fetch && git reset origin/main --hard

  docker compose -f docker-compose.prod.yml down

  docker compose -f docker-compose.prod.yml up -d --build

  echo "Redeployment completed at $(date)"
} >> "$LOGFILE" 2>&1
