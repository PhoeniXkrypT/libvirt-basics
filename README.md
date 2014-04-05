libvirt-basics in python
==============

Implements basic operation (start,stop,resume) for Xen VM using libvirt API

Start : start.py

It takes an xml file as an input to create a domain.The xml file added here is 'xyz.xml' which creates a domain 'Ubuntu001'.

python start.py xyz.xml

Save : save.py
-----

It saves an existing domain.

python save.py Ubuntu001

Resume : resume.py
-----

It resumes an existing domain.

python resume.py Ubuntu001


Stop : stop.py
-----

It shuts down an existing domain.

python stop.py Ubuntu001
