RFC1323
=======

[![Build Status](https://travis-ci.org/deekayen/ansible-role-RFC1323.svg?branch=main)](https://travis-ci.org/deekayen/ansible-role-RFC1323) [![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

Manage TCP timestamps.

Hosts may leak uptime information through TCP timestamps.

https://www.ietf.org/rfc/rfc1323.txt

Role Variables
--------------

```
tcp_timestamps_enabled: False
```

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - deekayen.RFC1323

License
-------

BSD
