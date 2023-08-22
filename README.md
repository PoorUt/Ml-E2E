# Ml-E2E
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



