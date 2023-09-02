# Ml-E2E

First We created a clone of our git repository so that we can push or pull changes from out local systems and we can also collaborate with other team members.


To create a git clone follow the following steps
    from your terminal(Git bash) type git clone "the github page link" - Enter
    

This repository contains Machine learning End to End projects. 
We will have the following in this project
    1- Data import and data cleaning
    2- Feature selection and Feature Engineering
    3- Modeli Building
    4- Model Deployment

These are the Software and account Requirement.
You should have a github account, Heroku Account, VS code IDE, and GIt cli in your pc.

If you dont have these you can get them from the links below.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/download)


The Next step will be to create a simple hello world flask application and deploy it to heroku using docker.
First of all we will configure our continous integration and continous deployment (CI-CD) pipeline in a fully automated way using git hub excels.
So, if we make any changes to our code, the automated CI-CD pipeline will continously trigger the deployment to heroku.


We will use Docker for this project

Docker -    Provides portability of our code
            We need to make our code portable and for this we need a container
            portability -   To run our code in any operating system. 
                            It isolates our code from any underlying operating system
            Container   -   
            Image       -   We can save our docker image on docker hub
            Simple explanation of Docker:

            [ Imagine you have a special box called a "container." Inside this box, you can put all the things your computer program needs to work, like the program itself, the tools it uses, and even a little world where it can run safely. This box is like a tiny computer world just for your program, and it's separate from the big computer it's on.]

So, when you want to share your program with others or make it work on a different computer, you just give them this special box. They can open it and everything your program needs is right there. This way, no matter where your program goes, it will work the same because it's in its own little container world. This makes it much easier to share and use programs without causing problems on the big computer.

Docker is like a magic tool that helps you make and use these special containers for your programs. It makes sure they all work the same way, no matter where they're running. Just like having different toy blocks that fit together no matter where you go!]

Is it similar to Conda Environment?

[Yes, that's a great way to think about it! Just like how Conda helps you create separate environments for your Python programs, Docker helps you create little worlds (containers) for your programs that have everything they need to run. These containers are like portable and self-contained packages that you can easily share and use on different computers without worrying about differences in settings or dependencies. So, both Conda and Docker help you keep your programs organized and working smoothly, even when you move them around.]

Once we have the docker image ready, we can download it and run it in AWS, GCP, Azure, or your local system.

In short, Docker provides isolated run time environment to run your application independent of operating system.

A container is a virtual machine. Or its the virualization of hardware  that contains the OS and all the dependencies just to run the app. It provides an isolated minimum required environment for your app.


Lets Understand CI-CD Pipeline
                CI                          CD
Local System ->               github   ->            Heroku

CI - Continous Integration
CD - Continous Deployment
 

The following is the agenda for our ML-E2E project
1- Create a flask App ( Hello World)
2- Write a docker file for flask application
3- Create github action for CI-CD
4- Heroku app for flask deployment
5- Create a structure for ML app
6- Build machine learning pipeline


First we need to create a conda environment
 
```
conda create -p venv python==3.7 -y
using "p" in the above command stands for prefix with the name "venv"
If we use just "p" then the virtual environment will create in the folder where conda is installed. And after some days your c drive will be full.
using "-p" allows us to create the virtual environment in the current working directory. So when we delete that folder the virtual environment will be deleted.


Then activate the conda environment. Use from the cmd terminal. conda activate venv/ (use the slash at the end if conda activate venv doesnt work )

Run this code in the terminal
```
use conda init command for the following

The conda init command is used in the Command Prompt (cmd) or other shell environments to set up the Conda package manager for managing Python and other software packages. Conda is a popular package and environment management system commonly used in data science and scientific computing.

When you run conda init in cmd or a similar shell, it performs the following tasks:

Shell Initialization: It configures your shell (Command Prompt, PowerShell, Bash, etc.) to work with Conda by modifying shell configuration files. This typically involves modifying shell startup scripts like .bashrc, .bash_profile, .zshrc, or .profile to include Conda-specific commands and settings.

Activate Conda Base Environment: It ensures that the Conda base environment (the default environment) is activated when you open a new shell session. This means that Conda's Python and packages will be available by default, allowing you to use Conda-managed packages and environments without needing to explicitly activate them every time you start a new shell session.

Initialize Conda Auto-Activation: In some shells, conda init can also set up auto-activation of Conda environments. This means that when you navigate to a directory containing a Conda environment, it will automatically activate that environment, making it easier to work with multiple environments for different projects.

Here's an example of how you might use conda init in the Command Prompt:


```

pip install -r requirements.txt





ML-E2E Requirements



