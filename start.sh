if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MutyalaHarshith/mhbeast.git /mhbeast
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /mhbeast
fi
cd /mhbeast
pip3 install -U -r requirements.txt
echo "Starting MH Bot...."
python3 bot.py
