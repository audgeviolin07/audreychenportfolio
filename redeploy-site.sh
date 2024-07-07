#!/bin/bash
tmux kill-server
cd ~/audreychenportfolio
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s my_flask_app "cd ~/audreychenportfolio && source python3-virtualenv/bin/activate && flask run --host=0.0.0.0"