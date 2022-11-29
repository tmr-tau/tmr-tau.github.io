Setting up two-factor authentication in GitLab
----------------------------------------------

Login to your account here [https://qtmcop.tmr.qld.gov.au]

If you don't have an account, contact `TAU <transport_analysis_requests@tmr.qld.gov.au>`_.

Once you login to your account, make sure you setup Two Factor Authentication in `settings <https://qtmcop.tmr.qld.gov.au/profile/two_factor_auth>`_.

Keep in mind to save the backup codes somewhere safe in case you loose your device.

Now, when you have 2FA activated, your password would not work from command prompt for authentication. You need to create a access token.
This token would then be used instead of the password when prompted by git on your machine.

To do so, go to your account settings and create an access token, note down this token because it would only be visible once.

Make sure to choose only read and write repository scopes as shown below.

.. image:: /usage/git/images/scope.png

