from hashlib import sha256
import os
pass_list = []
salt_list = []
limit = 10
icount = 0
jcount = 0
with open('random_passes.txt', 'r') as f:
    for line in f:
        pass_list.append(line)
        if icount < limit:
            icount = icount + 1
        else: 
            break
with open('random_salts.txt', 'r') as g:
    for line in g:
        salt_list.append(line)
        if jcount < limit:
            jcount = jcount + 1
        else: 
            break

for salt in salt_list:
    salt = str(salt.split("\n")[0])
    fname = 'hash_table_'+salt+'.txt'
    if os.path.exists(fname):
        continue
    with open(fname, "w") as f:
        for pas in pass_list:
            pas = str(pas.split("\n")[0])
            f.write(str(sha256(str(sha256(pas).hexdigest())+salt).hexdigest())+":"+salt+":"+pas)


