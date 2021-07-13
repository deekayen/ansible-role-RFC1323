RFC1323
=======

[![CI](https://github.com/deekayen/ansible-role-RFC1323/actions/workflows/ci.yml/badge.svg)](https://github.com/deekayen/ansible-role-RFC1323/actions/workflows/ci.yml) [![Project Status: Inactive – The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows.](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

Manage TCP timestamps for hosts implementing RFC1323/RFC7323.

Hosts may leak system uptime information through TCP timestamps. Various vulnerability scanners may surface this issue with a CVSS Score of 2.6.

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
