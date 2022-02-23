#!/usr/bin/python 
# -*- coding: utf-8 -*-
from ansible.module_utils.basic import AnsibleModule  

def main(): 
    module = AnsibleModule( 
        argument_spec=dict( 
            db_name    = dict(required=True, type=str), 
            request    = dict(required=True, type=str), 
        ) 
    )

    db_name_local = module.params.get('db_name') 
    request_local = module.params.get('request')
    results = {"db_name":db_name_local, "request":request_local}
    module.exit_json(changed=False, results=results)  

if __name__ == "__main__": 
    main()