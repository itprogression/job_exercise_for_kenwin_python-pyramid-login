
--------------------------------------------------------------------------------
Proyecto: install paquetes (python + pyramid + postgres)
--------------------------------------------------------------------------------

Install: python + pipenv
-----------------------------------------
so: ubuntu 16.04.5 LTS
srv app:
    If you are using Python 3, type:
        sudo apt-get update && sudo apt-get upgrade
        sudo apt-get install python3 python3-pip python3.5-venv
        * Packages and development tools to install to ensure that we have a robust set-up for our programming environment
            sudo apt-get install build-essential libssl-dev libffi-dev python3-dev libpq-dev
    CHECK:
        python3 -V
            Python 3.5.2
  Install virtual environment: pipenv
    https://opensource.com/article/18/2/why-python-devs-should-use-pipenv
    If you are using Python 3, type:
      sudo pip3 install pipenv


Install: srv db: postgresql 9.5
-----------------------------------------
    sudo apt-get update
    sudo apt-get install postgresql postgresql-contrib

Proyecto: crear "virtual environment"
-----------------------------------------
https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv

    mkdir ~/proyecto
    cd ~/proyecto
    pipenv install
    pipenv shell
    (pyramid-someHash) $ pipenv install "pyramid==1.9.2"

Proyecto: pipenv, Managing Python dependencies 
-----------------------------------------
To install a Python package for your project use the install keyword. For example,

pipenv install beautifulsoup4

A package can be removed in a similar way with the uninstall keyword,

pipenv uninstall beautifulsoup4

It’s worth adding the Pipfiles to your Git repository, so that if another user were to clone the repository, all they would have to do is install Pipenv on their system and then type,

pipenv install


Proyecto: gestionar "virtual environment"
-----------------------------------------
In order to keep your environment consistent, it’s a good idea to “freeze” the current state of the environment packages. To do this, run

$ pip freeze > requirements.txt

This will create a requirements.txt file, which contains a simple list of all the packages in the current environment, and their respective versions. You can see the list of installed packages without the requirements format using “pip list”. Later it will be easier for a different developer (or you, if you need to re-create the environment) to install the same packages using the same versions:

$ pip install -r requirements.txt


Proyecto: Installing Pyramid on a "virtual environment"
-----------------------------------------
Link:
    https://docs.pylonsproject.org/projects/pyramid/en/1.9-branch/narr/install.html#installing-chapter

    https://opensource.com/article/18/5/pyramid-framework

Install:
    pipenv install pyramid


