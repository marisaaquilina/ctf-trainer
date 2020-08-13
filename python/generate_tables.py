from hashlib import sha256
pass_list = []
with open('random_passes.txt', 'r') as f:
    for line in f:
        pass_list.append(line)

with open('hash_table.txt', "w") as f:
    for pas in pass_list:
        f.write(str(sha256(pas).hexdigest())+":"+pas)
