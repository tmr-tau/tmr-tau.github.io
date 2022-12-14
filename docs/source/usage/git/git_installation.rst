Installing Git on your PC
-------------------------
Most TAU projects are now hosted on GitHub and requires git to be installed on your machine.

For TMR staff, the best way to do this is to place a SCO request for Git / GitHub access. The packaged installer will deal with some TMR environment specific challenges.

For external staff, consult your IT department or download and install from `here <https://git-scm.com/downloads>`_.

Once you have done the installation, open git bash and run the following:

.. code:: text

    git config --global user.name "your name here" 
    git config --global user.email email@domain

Do the following if you need to add proxy settings.

.. code:: text

    git config --global http.proxy http://user:password@www-proxy.qdot.qld.gov.au:8080
    git config --global https.proxy https://user:password@www-proxy.qdot.qld.gov.au:8080
    git config --global credential.useHttpPath true

Remember to change proxy string as per your organization if you are not using this from TMR's network.

This completes setup for git on your machine.

Once you are done with this stuff please head over to the :doc:`/usage/git/git_2fa`
