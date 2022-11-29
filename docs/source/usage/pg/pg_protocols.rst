Database development protocols
------------------------------

There are certain protocols which must be followed when undertaking database development work to ensure collaborators can work together effectively.


Object ownership
****************

Object ownership must be managed carefully to ensure that all users collaborating on a project can do everything they need to do. Ownership and it's associated privileges are not grantable, but they can be inherited by being a member of the role that owns the object. For example, if ``proj_dev`` owns ``this_table`` and ``org_proj`` is a member of ``proj_dev`` then ``org_proj`` inherits ownership of ``this_table`` by proxy. But ``this_table`` must be owned by ``proj_dev`` (as opposed to being owned by ``org_proj``) otherwise other memebrs of ``proj_dev`` won't be able to interact with it fully.

To ensure this happens, users must always take one of these two paths when interacting with the server:

1. After establishing a connection to the server as your user, use the ``SET ROLE`` SQL command to assume the ``proj_dev`` role, so that by default all database admin activities (such as creating and altering tables) are performed as the project role (`more info <https://www.postgresql.org/docs/11/sql-set-role.html>`_), or
2. After creating objects under your user then as soon as practical (or ideally as part of the same script), you must use the ``ALTER ... OWNER TO proj_dev`` command to hand ownership over to the project role (`more info in relation to altering tables <https://www.postgresql.org/docs/11/sql-altertable.html>`_ noting that there are separate ``ALTER`` commands for other database objects too).
