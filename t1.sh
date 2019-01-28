nohup bash ./test.sh > .test.log 2>&1 &
echo $! > save_pid.txt
