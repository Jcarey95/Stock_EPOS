# Check Self Integrity
import csv
import logging
import hashlib

log = logging.getLogger(__name__)
log.info('Start Up Script Begin')


def first_run():
    global hash_code, actual_hash_code, f_name

    checker = 0

    with open('StartUp/Files.csv', 'r') as f:
        hash_code_file = csv.reader(f)
        for row in hash_code_file:
            f_name = row[0]
            file_path = row[1]
            hash_code = row[2]
            # Create Actual Hash
            file_to_hash = open(file_path, mode='r')
            actual_hash_code = hashlib.md5()
            for buf in file_to_hash.read(128):
                actual_hash_code.update(buf.encode())
                # Compare Actual Against Expected
        if hash_code == actual_hash_code.hexdigest():
            log.info(f_name + ' Hash Passed')
        else:
            log.info(f_name + ' Hash Failed')
            checker += 1

    log.info('Hash Check Complete')

    return checker
