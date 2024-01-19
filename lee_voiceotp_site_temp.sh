#!/bin/bash

APP_DIR="/home/taitd/leeon_voiceotp/site_voiceotp"  # Đường dẫn đến thư mục chứa manage.py
PID_FILE="$APP_DIR/server.pid"
LOG_FILE="$APP_DIR/server.log"

start() {
    echo "Starting Lee VoiceOTP site..."
    source $APP_DIR/myworld/bin/activate
    nohup python3 $APP_DIR/manage.py runserver 5003 > $LOG_FILE 2>&1 &
    echo $! > $PID_FILE
    echo "Lee VoiceOTP site started."
}

stop() {
    echo "Stopping Lee VoiceOTP site..."
    if [ -f $PID_FILE ]; then
        PID=$(cat $PID_FILE)
        kill $PID
        rm $PID_FILE
        echo "Lee VoiceOTP site stopped."
    else
        echo "No active Lee VoiceOTP site found."
    fi
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        sleep 2
        start
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac

exit 0
