Role Name
=========

This role sets up a mirrof of debian-style repositories using aptly.

Requirements
------------

**Host**

None

**Role**

Installed automatically:

- [Pxul](https://github.com/badi/pxul.git)

Role Variables
--------------

| Variable                  | Description                                                | Required | Default           |
|---------------------------|------------------------------------------------------------|----------|-------------------|
| `mirror_gpg_password`     | Password for the GPG (generated) key                       | yes      |                   |
| `mirror_gpg_name_real`    | Real name to create the key with                           | yes      |                   |
| `mirror_gpg_name_email`   | Eamil address for the key                                  | yes      |                   |
| `mirror_server_port`      | Port on which to serve the mirror                          | no       | 80                |
| `mirror_server_docroot`   | Where the mirror is located on dist                        | no       | `~/.aptly/public` |
| `mirror_gpg_key_type`     | Key type                                                   | no       | RSA               |
| `mirror_gpg_key_length`   | Length of the GPG key                                      | no       | 2048              |
| `mirror_gpg_expire_date`  | The date the key expires                                   | no       | 0 (never)         |
| `mirror_gpg_name_comment` | Comment with which to create the key                       | no       | Signing repos     |
| `mirrors`                 | A list of key/value pairs describing the mirrors to create | yes      |                   | 

A description of a mirror in the `mirrors` list contains the following

| Variable        | Description                                                      | Required | Example                   | Default           |
|-----------------|------------------------------------------------------------------|----------|---------------------------|-------------------|
| `name`          | The name of the mirror as used by aptly                          | yes      | aptly-squeeze             |                   |
| `uri`           | Location of the repository to be mirrored                        | yes      | "http://repo.aptly.info/" |                   |
| `distribution`  | Distribution component of the mirror                             | yes      | squeeze                   |                   |
| `components`    | List of the components of the mirror                             | yes      | ['main']                  |                   |
| `architectures` | List of the architectures to mirror                              | no       | ['amd64']                 | []                |
| `trusted_key`   | GPG key id of the mirrored repository to trust                   | yes      | 2A194991                  |                   |
| `keyserver`     | Location of the server to get `trusted_key` from                 | no       | "keys.gnupg.net"          | "keys.gnupg.net"  |
| `keyring`       | Name of the keyring to store the `trusted_key`                   | no       | "trustedkeys.gpg"         | "trustedkeys.gpg" |
| `within`        | Number of seconds within which a mirror is considered up-to-date | no       | 3600                      | 0                 |



Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      sudo: yes
      roles:
        - role: mirror
    
          mirror_gpg_password: "my super secret unknown passphrase"
          mirror_gpg_name_real: Firstname Lastname
          mirror_gpg_name_email: me@example.com
    
          mirrors:
    
            - name: aptly-squeeze-amd64
              uri: "http://repo.aptly.info/"
              distribution: "squeeze"
              components: ['main']
              trusted_key: 2A194991
              architectures: ['amd64']
              within: "{{ 60*60 }}"


License
-------

BSD

Author Information
------------------

Badi' Abdul-Wahid <abdulwahidc@gmail.com>
