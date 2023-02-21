import os
import pyeclib.ec_iface as ec_iface

def split_file(input_file_path, output_dir_path, shard_size):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)

    # Read input file into memory
    with open(input_file_path, 'rb') as input_file:
        input_data = input_file.read()

    # Get total size of input file
    input_size = len(input_data)

    # Calculate number of shards needed
    shard_count = (input_size + shard_size - 1) // shard_size

    # Initialize erasure coding interface
    ec = ec_iface.ECChunker(k=shard_count, m=2)

    # Split input data into shards
    shards = ec.encode(input_data)

    # Write each shard to separate file
    for i, shard in enumerate(shards):
        shard_path = os.path.join(output_dir_path, f"{i}.part")
        with open(shard_path, 'wb') as shard_file:
            shard_file.write(shard)

    # Return number of shards created
    return shard_count

