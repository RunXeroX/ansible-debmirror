#!/usr/bin/python
# -*- coding: utf-8 -*-

import gnupg
import sys
import os.path
import os



def main():
    module = AnsibleModule(
        argument_spec={
            'path': {'required': True},
            'keyring': {'required': False},
        },
    )

    # verbose needs to be False otherwise ansible cannot parse stdout
    gpg = gnupg.GPG(keyring=module.params['keyring'], verbose=False)

    new_key = gpg.scan_keys(module.params['path'])[0]
    for known_key in gpg.list_keys():
        if new_key['fingerprint'] == known_key['fingerprint']:
            module.exit_json(changed=False)

    key = open(module.params['path']).read()
    result = gpg.import_keys(key)

    # handle error cases
    if not result.fingerprints:
        module.fail_json(msg='Could not import the key',
                         results=result.results,
                         reasons=result.problem_reason,
                         params=module.params)

    # success
    elif result.unchanged == 0:
        module.exit_json(changed=True)
    else:  # importing keys is idempotent
        module.exit_json(changed=False)


from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
