#!/bin/bash
docker build -t pp-container .
docker run -e INPUT_OWNER_NAME=stephend017 -e INPUT_REPOSITORY_NAME=discord_ritoman -e INPUT_PERSONAL_ACCESS_TOKEN=$(echo $GH_PAT) -e INPUT_CONFIG_FILE=pencil_pusher.config.json pp-container
