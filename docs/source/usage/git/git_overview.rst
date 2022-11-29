Git overview
------------
First let's clarify some software and their roles (colours relate to the diagram below):

* **GitLab**: Is a remote repository for storing version controlled code. TMR's GitLab server is hosted within the TMR AWS tenancy.
* **PyCharm / VSCode**: These are IDEs you're using to write code in a workspace (which remains "staged" there until you commit it to your local repository)
* **Git**: Is the software that handles the version controlling of your code and acts as the communication interface between your IDE and GitLab.

Now for some jargon, explained in the context of starting work on an existing project, where you would go through these steps (colours relate to the diagram below, except purple which are not shown in the diagram):

* **Clone/pull**: Clone/pull a project (set of code) from a remote repository to your workspace (local)
* **Branch**: All code has a "master" branch. The master branch contains the latest working version of all code. You will probably have cloned this branch (although you can clone others). Now you want to start making some changes so you will create a branch of your own, which is a point-in-time deviation from the master branch.
* **Commit**: You're now working on the branch you created making changes that won't impact the master branch. Well done, this is good practice. As you make changes in an IDE they're probably being saved automatically, but when you reach particular milestones you may want to commit those changes. Think of this as a hard save so you have a marker in time that you can go back to. But commits are still only local.
* **Push**: Because you live in fear of losing your work that was not backed up, at the end of each day you make a habit of pushing your code to the remote repository to back it up and let others see where you're up to. When you push whilst on a branch, you're still not messing with the master branch, you're now putting your branch in the remote repository and pushing to that. No harm done!
* **Merge**: You've now made all the changes you want to make on that branch and you're ready to merge it into the master branch. To do this you create a merge request. The maintainer of your repository can talk you through protocols around this as they may vary from project to project.

The below diagram outlines additional actions you can take to move code around and the terms used to make different movements.

.. image:: /usage/git/images/git_flow.png
