RFC1323
=======

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
