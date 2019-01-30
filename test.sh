res="1"

while true
do 
	echo "Hello"
	$(python -u test.py)
	res="$?"
	if [ $res -eq 1 ]; then
		sleep 5
	else 
		xterm -e 'python -u test.py'
		echo "Logged in"
	fi
done

 



