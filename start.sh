echo "install npm modules"
npm install > /dev/null

if [[ -z $(command -v zerorpc) ]]; then
    echo "install zerorpc"
    pip3 install zerorpc > /dev/null 
fi

echo "---------- ICS START ----------"
python3 ICS_Server/serverAPI.py &
npm start &
