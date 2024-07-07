#!/bin/bash
tmux kill-server
cd /audreychenportfolio
git fetch && git reset origin/main --hard
source venv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s my_flask_app "cd /audreychenportfolio && source venv/bin/activate && flask run --host=0.0.0.0"
