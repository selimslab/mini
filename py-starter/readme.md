# pystarter :snake: 

a modern python starter kit 

* automated tests
* code coverage
* linting
* styling
* type checking 
* docs

![Build Status](https://github.com/selimslab/py/workflows/test/badge.svg)

[![Codecov](https://img.shields.io/codecov/c/github/selimslab/py)](https://codecov.io/gh/selimslab/py)

[![MIT License](https://img.shields.io/github/license/selimslab/py)](https://github.com/selimslab/py/blob/master/LICENSE)


# from scratch 

## 1. install python 

do not use default system python for development to avoid messing up your system 

install a fresh separate python

pyenv makes it easy [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)

#### steps for macOS

#### 1. install pyenv

`brew install pyenv`

#### 2. make the latest python default for all pyenv environments

`pyenv global 3.8.2`

#### 3. make it accessible in shell 

`echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bash_profile`

if you use zsh, replace .bash_profile  with .zshrc

#### 4. restart the shell 

done. 


for more explanation, see [this article](https://opensource.com/article/19/5/python-3-default-mac)


## 2. package management

there are a few options pip, pipenv, poetry 

[poetry](https://python-poetry.org/) is more actively developed makes and it makes it easy to publish your package 



#### install poetry 

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
`

add it to the path

for zsh, add the following line to .zshrc

`export PATH=$PATH:$HOME/.poetry/bin`

#### create a new project 

`mkdir new-project`

`cd new-project`

#### init poetry 

`poetry init`

`poetry shell`

## test

add dev dependencies:

`poetry add --dev pytest`

run tests:

`pytest`

## code coverage 

`poetry add --dev coverage pytest-cov`

To enable coverage reporting, run pytest with the --cov option:

`pytest --cov`

add this to pyproject.toml for cleaner coverage reporting 

```yaml
[tool.coverage.paths]
source = ["src", "*/site-packages"]

[tool.coverage.run]
branch = true
source = ["src"]

[tool.coverage.report]
show_missing = true
```

`pytest --cov` 

## lint

`poetry add --dev pylint`

## type-check

`poetry add --dev mypy`

## format style 

`poetry add --dev black`

format all 

`black .`


## Github Actions 

create a .github/workflows directory

`mkdir .github/workflows`

create a .yml file 



# add badges 

## add a coverage report badge

visit codecov.io, signup or login

add 

```yaml
- uses: codecov/codecov-action@v1
    with:
    token: ${{ secrets.CODECOV_TOKEN }}
```

obtain a CODECOV_TOKEN and  add it to your repos secrets in settings/secrets 

[![Codecov](https://img.shields.io/codecov/c/github/selimslab/py)](https://codecov.io/gh/selimslab/py)

## add a build success badge 

modify this, replace repo name and workflows/test

`![Build Status](https://github.com/selimslab/py/workflows/test/badge.svg)`
