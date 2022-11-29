Using Git in PyCharm
--------------------

To clone a project from GitLab in PyCharm follow these steps (assuming you have done the setup as per the above Git Installation guide):

1. Navigate to your GitLab project in your web browser and click the blue Clone button and then copy the URL for via HTTP
2. Open PyCharm and select Get From Version Control*
3. Paste your clone URL from step 1 into the URL field in PyCharm
4. (optional) Change the directory where you want to set up your local repository
5. Login to GitLab with your username and use your Access Token (see Git Installation) as your password

.. note:: \*If you already have a project open this option appears in the VCS menu

You should now have a local copy of the repository and can begin work (although you might want to create a branch first so that you're not working on the master branch, which is considered bad practice).

To create a new branch follow these steps:

1. Click on master in the bottom right
2. Click + New branch
3. Give your new branch a name that follows the naming protocol used in this project (usually ``username/task_youre_working_on``)
4. Click OK (leaving the checkout branch option ticked will switch you onto this branch and off master)
