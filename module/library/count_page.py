#!/usr/bin/python
#-*- coding: utf-8 -*-

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            msg = dict(required=True, type='str')
        )
    )
    _msg = 'reading: '+module.params.get('msg')
    module.exit_json(changed=False, resultat=_msg)
DOCUMENTATION='''
module: count_page
author: Aadil
description: Module qui permet de lire un message
options:
  pass
'''

EXAMPLES='''
task example
'''

RETURN='''
resltat:
  description: retourne reading: message read
'''

if __name__=='__main__':
    main()