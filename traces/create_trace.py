# 0x1FF96FC0 WRITE   160
# 0x2000D600 IFETCH  165
# 0x1FF97000 READ    192

# start with "mase"

import random
import sys

random.seed(30)

# read_write = ['READ', 'WRITE'] # Just should make them .lower()

# Create the address space
addresses = []
for i in range(2):
    for j in range(2):
        for k in range(2):
            # Addresses which will allow the highest throughput
            # address = (i << 29) | (j << 28) | (k << 27) | (7 << 2)
            # Addresses which will access one bank with 50% row miss
            address = (i << 4) | (j << 5) | (k << 6)
            if (i*j*k):
                address |= (1 << 17)
            addresses.append(hex(address))

# to track on which clock cycle we are
cycle = 0
# To track the number of transactions
transactions = 0

with open("../../dram.sys/DRAMSys/library/resources/traces/python-script.stl", "r") as file_source:
    with open("mase_script.trc", "w") as file_destination:
        for old_access in file_source:
            text = old_access[:-1].split('\t')
            text[2] = text[2][:2] + '0'*(10-len(text[2])) + text[2][2:]
            file_destination.write("%s %s %s\n" % (text[2],text[1].upper(),text[0][:-1]))



# with open("traces/mase_art.trc", "r") as example:
#     for i in range(10):
#         print (repr(example.readline()))
