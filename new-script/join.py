import os
import pyeclib.ec_iface as ec_iface

def join_files(input_dir_path, output_file_path):
    # Get list of input shard files
    shard_files = [os.path.join(input_dir_path, f) for f in os.listdir(input_dir_path) if f.endswith('.part')]

    # Initialize erasure coding interface
    shard_count = len(shard_files)
    ec = ec_iface.ECChunker(k=shard_count, m=2)

    # Read each shard file into memory
    shards = []
    for shard_file in shard_files:
        with open(shard_file, 'rb') as file:
            shards.append(file.read())

    # Use erasure coding interface to reconstruct original data
    original_data = ec.decode(shards)

    # Write reconstructed data to output file
    with open(output_file_path, 'wb') as output_file:
        output_file.write(original_data)

