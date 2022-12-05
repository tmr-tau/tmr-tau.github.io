Using Git in PyCharm
--------------------
To clone a project from GitHub in PyCharm follow these steps (assuming you have done the setup as per the above installation guide):

1. In GitHub (via web browser) navigate to the repository, click the green Code button and then copy the URL shown.
2. Open PyCharm (if you have a project already open, close it) and select Get From Version Control
3. Paste your clone URL from step 1 into the URL field in PyCharm
4. (optional) Change the directory where you want to set up your local repository
5. You will be asked to Log in via GitHub or Use Token. Select Log in via GitHub.
6. Click through the relevant screens to authorise JetBrains to access GitHub; you may need to click the blue request button next to the TAU organisation when you get to the GitHub authorisation screen.

If the authorisation has worked, PyCharm will start cloning your repository and open it as a new PyCharm project. If Step 6 from above doesn't allow you to authorize Github in PyCharm or if you get some SSH/proxy sounding error, there's an alternative method to access the repository:

1. Create a personal access token (Creating a personal access token - GitHub Docs). Important to save this token somewhere safe.
2. Authorize token to access tmr-tau team (Authorizing a personal access token for use with SAML single sign-on - GitHub Docs)
3. In GitHub (via web browser) navigate to the repository, click the green Code button and then copy the URL shown.
4. Open PyCharm (if you have a project already open, close it) and select Get From Version Control
5. Paste your clone URL from step 3 into the URL field in PyCharm
6. (optional) Change the directory where you want to set up your local repository
7. You will be asked to Log in via GitHub or Use Token. Select Use Token.
8. Insert token when asked.

Navigation between branches and creation of new branches can all be done via your repository menu in the bottom right (it will likely say master after cloning). To create a new branch follow these steps:

1. Click on master in the bottom right
2. Click + New branch
3. Give your new branch a name that follows the naming protocol used in this project (usually ``username/task_youre_working_on``)
4. Click OK (leaving the checkout branch option ticked will switch you onto this branch and off master)
