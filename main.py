import reedsolo
import os

num_shards = 10
num_redundant_shards = 2


filename = 'eg.txt'

with open(filename, 'rb') as f:
    data = f.read()


rs = reedsolo.RSCodec(num_redundant_shards)
shards = rs.encode(data)


for i, shard in enumerate(shards):
    with open('shard{}.txt'.format(i), 'w') as f:
        f.write(shard)



shard_files = [open('shard{}.txt'.format(i), 'rb') for i in range(num_shards)]
shard_contents = [f.read() for f in shard_files]

for f in shard_files:
    f.close()


recovered_data = rs.decoded(shard_contents)

with open('recoverd.txt', 'wb') as f:
    f.write(recovered_data)


