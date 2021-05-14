# create enivornment for linux
sudo pip install pipenv
pipenv shell

# install dependencies
pipenv install -r requirements.txt

# start training
python run.py

echo "Training Completed!"
