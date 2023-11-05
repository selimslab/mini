## Aircraft radar 

Follow and plot aircraft position 

## Setup 

Requirements in pyproject.toml

`bash ./setup.sh` 

This script will install poetry package manager, create a virtual env folder .venv. and install project dependencies 


## If your virtual env is not auto-activated 

please run

 `poetry shell`

 or

 `source .venv/bin/activate`

## Run 

run 

`python tests/test_airforce.py`

this will start a repl 

commands  

`help`  

`stats` : view latest stats

`plot`  : plot targets seen 

`ctrl + z` to exit 

