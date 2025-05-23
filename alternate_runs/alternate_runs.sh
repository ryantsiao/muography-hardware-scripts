#!/bin/bash

run_num=2

PTRIG_runtime=20
TLOGIC_runtime=300

for i in $(seq 1 $run_num); do
    echo "=== Run $i: PTRIG mode ==="
    cp config_PTRIG.txt Janus_Config.txt

    # Start JanusC in a tmux session
    tmux new-session -d -s janus_ptrig './JanusC'
    sleep 2  # Give it time to load

    # Send 's' to start, then wait, then send 'S' to stop
    tmux send-keys -t janus_ptrig 's' C-m
    sleep $PTRIG_runtime
    tmux send-keys -t janus_ptrig 'S' C-m

    sleep 2
    tmux kill-session -t janus_ptrig

    sleep 10

    echo "=== Run $i: TLOGIC mode ==="
    cp config_TLOGIC.txt Janus_Config.txt

    tmux new-session -d -s janus_tlogic './JanusC'
    sleep 2

    tmux send-keys -t janus_tlogic 's' C-m
    sleep $TLOGIC_runtime
    tmux send-keys -t janus_tlogic 'S' C-m

    sleep 2
    tmux kill-session -t janus_tlogic

    sleep 10
done
