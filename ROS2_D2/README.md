# AQUABOT ROS2-D2 TEAM REPO

This is were we are going to work on our aquabot.

**ATTENTION** : this tuto can change as I don't already know how I will setup my own fork, but don't worry you'll be told of the future adjustements.

## Create your own fork 

Go to the main page of this repo and click on create a new fork : 
![image](https://github.com/user-attachments/assets/0943bce1-29a8-4fad-bffb-20a005b371aa)

Then git clone your fork in the aquabot source directory. 

```
cd ~/vrx_ws/src/
git clone <your_fork_ssh>
```

Now you have a copy of the original repo. But you cannot fetch the upstream project.
To enable this, you have to add ROS2_D2 original repo : 

```
cd ~/vrx_ws/src/ROS2_D2
git remote add upstream git@github.com:MatisViozelange/ROS2_D2.git
``` 

Now type : 
```
git remote -v
```

You should be able to see your **origin** and the **upstream** repo.

## Fork gestion 

To update your fork and work with a synchronized version of the upstream repo, type : 

```
git fetch upstream
```

This will add all branches of the upstream repo to your local image.

To create pull request, we will see together how it works on github directly.


# Some git command you shoud know 
(if you don't want to use git graph or you're just curious ;) )

```
git status
```
To see the different modification and their stage of commit compared to your last branch pushed commits.

```
git commit –m “message”
```

Commit all your last modifications

```
git add <your_files>
```

Add the commited modifaication of _your_file_ to the intermediate state.

```
git push <fork> <branch>
```
To push your intermediate commited code on designed fork and branch. It is better to precise every time if your using the terminal to not to push code on the wrong branch. (like the upstream :)) But don't worry you shouldn't be able to do so without a request to every one. You can add the `-f` argument to force certain pushes on your branches.


```
git checkout <branch-name>
```

To swing from a branch to another. You can use the argument `-b` to create a new branch.

```
git diff <source-branch> <target-branch>
```

List all the conflicts between to branches. You have a graphical tool on vscode you wanna use instead of this.

```
git stash
```
To pseudo-commit changements you don't want to commit for now. It is very use full if you are working on two branches simultaneously.

```
git fetch <fork>
```
This one has been seen upward.

```
git rebase --interactive
```

See a good documentation on [this page](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase). 
It is a very important tool we are gooing to use every time we want to update our code to the upstream. There is also a graphical tool on git_graph which is very convinient. 

We use `fetch` + `rebase` instead of juste `git pull` beceause `pull` does almost the same thing but resolves the conflicts itself et don't give you the control and the option `rebase` has.  

Finaly, if you want to go back to a previous commit because you did something wrong, you want to know these commands : 

```
git log
git reset <commit_ID>
```

