# Ml-E2E

First We created a clone of our git repository so that we can push or pull changes from our local systems and we can also collaborate with other team members.


To create a git clone follow the following steps
    from your terminal(Git bash) type git clone "the github page link" - Enter
    

This repository contains Machine learning End to End projects. 
We will have the following in this project
    1- Data import and data cleaning
    2- Feature selection and Feature Engineering
    3- Model Building
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
```
Regarding Git repository

Once you have the git repository and git clone set up, As long as you're working within the cloned directory, your code editor should recognize the Git connection automatically. You won't need to repeatedly set up the connection each time you open the folder, assuming you haven't deleted the .git directory or made changes that would disrupt the Git repository's integrity.. Once you have cloned the repository, you can open the cloned directory in your code editor. Most code editors, such as Visual Studio Code, Atom, or Sublime Text, will automatically recognize that you're working within a Git repository and provide Git-related functionality.

```
pip install -r requirements.txt
Regarding requirements.txt file

why do i need the requirements.txt file before deployment of a ml model?

The requirements.txt file is a commonly used tool in the Python ecosystem for specifying and managing dependencies for a project. While it's not strictly necessary for every deployment of a machine learning (ML) model, it serves several important purposes:

Dependency Management: ML projects often rely on specific versions of libraries and packages. These dependencies can include machine learning frameworks (e.g., TensorFlow, PyTorch), data processing libraries (e.g., NumPy, pandas), and other utilities. By listing these dependencies in a requirements.txt file, you document the exact versions that are known to work with your project. This helps ensure that your ML model works as expected when deployed, as you can reproduce the same environment.

Environment Reproducibility: When deploying an ML model to a production environment, it's crucial to replicate the same software environment as the one used during development and training. By providing a requirements.txt file, you enable easy replication of the environment on the deployment server. This ensures consistency and reduces the chances of compatibility issues or unexpected behavior due to different library versions.

Ease of Collaboration: If you're working on an ML project as part of a team or sharing your code with others, a requirements.txt file makes it simple for collaborators to set up their development environment. They can use the same dependencies you've specified, reducing friction in the collaboration process.

Simplifies Deployment: Many deployment platforms and containerization tools, such as Docker, Heroku, and cloud-based services like AWS Lambda, support the use of requirements.txt to automatically install project dependencies during deployment. This streamlines the deployment process and ensures that the production environment is consistent with the development environment.

Here's how you can create a requirements.txt file:

Activate your Python virtual environment if you're using one.

Use the pip freeze command to generate a list of installed packages and their versions:

pip freeze > requirements.txt

The requirements.txt file will now contain a list of dependencies and their versions, which can be used to recreate the environment.

In summary, while a requirements.txt file may not be strictly required for every ML model deployment, it's a best practice to include one. It helps ensure a smooth and reproducible deployment process, reduces the risk of compatibility issues, and simplifies collaboration with others.



Q- I only used pandas, numpy, scikit learn, and flask. but when I use pip freeze > requirements.txt i get a huge list. what is this?

When you use the pip freeze command to generate a requirements.txt file, it captures not only the packages you've directly installed but also all the packages that those dependencies, and their dependencies, depend on. This includes all transitive dependencies, which can result in a longer list of packages than you might expect.

For example, if you have installed pandas, it relies on numpy, and numpy may have its own dependencies. Similarly, if you've installed scikit-learn, it has its own dependencies, and so on. Flask, being a web framework, also has its dependencies.

So, when you run pip freeze > requirements.txt, it produces a comprehensive list of all packages currently installed in your environment, including the ones indirectly installed due to dependencies.

To create a more concise requirements.txt file that only includes the packages you've explicitly installed (i.e., pandas, numpy, scikit-learn, and Flask), you can manually create the requirements.txt file by listing these packages and their versions explicitly. Here's an example of what the contents of your requirements.txt file might look like:

pandas==x.x.x
numpy==x.x.x
scikit-learn==x.x.x
Flask==x.x.x

Replace x.x.x with the specific versions of these packages that you are using in your project. This way, you'll have a much shorter and cleaner requirements.txt file that only includes the packages you've intentionally added to your project.

Q-  So if I only write pandas, numpy, scikitlearn, and flask in my requirements.txt file, will it still work?

If you only include pandas, numpy, scikit-learn, and Flask in your requirements.txt file without specifying version numbers, it will still work, but it might not be the best practice for a production environment or collaborative project. Without specifying version numbers, you're essentially telling Python to use the latest versions of these packages available at the time of installation. While this is generally fine for development, it can lead to compatibility issues or unexpected behavior in the future when new versions of these packages are released.

It's a good practice to specify version numbers in your requirements.txt file to ensure consistency and avoid potential problems. By specifying versions, you have more control over which package versions are used, and you can ensure that your code works as expected even if newer versions of the packages are released.

Here's how you can specify version numbers in your requirements.txt file:

pandas==1.3.3
numpy==1.21.2
scikit-learn==0.24.2
Flask==2.0.1

In this example, I've added version numbers (e.g., 1.3.3, 1.21.2, etc.) to each package. You should replace these with the specific versions that you have tested and confirmed to work with your project. When you specify versions, you make your project more reproducible and reduce the risk of issues related to unexpected updates in the packages.


**Q- __So while writing a python code if i use pip freeze > requirements.txt from cmd, then it will create a requirments.txt file? do i need to be in the same directory first in cmd?  can i do this for a python code that i write in jupyter notebook?**

Include ** to make bold


es, you can create a requirements.txt file for a Python project using the pip freeze command from the Command Prompt (CMD). Here are the steps:

Open the Command Prompt.

Navigate to the directory where your Python project is located. You can use the cd command to change the directory. For example:

cd path\to\your\project

Replace path\to\your\project with the actual path to your project directory.

Activate your Python virtual environment if you're using one. If you're not using a virtual environment, you can skip this step.

Run the pip freeze command to generate a requirements.txt file:

pip freeze > requirements.txt
This command will create a requirements.txt file in the current directory, listing all the installed packages and their versions.

Regarding Jupyter Notebook, you can create a requirements.txt file for a Jupyter Notebook-based project in the same way. Just make sure you're in the directory where your Jupyter Notebook project resides when you run the pip freeze command. The requirements.txt file will capture the Python packages that are installed in the environment associated with your Jupyter Notebook project.










ML-E2E Requirements



