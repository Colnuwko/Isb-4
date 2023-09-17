import hashlib
import multiprocessing as mp
from random import randint


def check_hash(bin: str, six_numbers: int, last_num: str, hash: str, hash_format: str) -> bool:
    full_card_num = f"{bin}{six_numbers:06d}{last_num}"
    print(full_card_num)
    match hash_format:
        case 'blake2b':
            if hashlib.blake2b(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'blake2s':
            if hashlib.blake2s(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha1':
            if hashlib.sha1(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha224':
            if hashlib.sha224(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha256':
            if hashlib.sha256(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha384':
            if hashlib.sha384(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha3_224':
            if hashlib.sha3_224(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha3_256':
            if hashlib.sha3_256(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha3_384':
            if hashlib.sha3_384(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha3_512':
            if hashlib.sha3_512(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'sha512':
            if hashlib.sha512(full_card_num.encode()).hexdigest() == hash:
                return True
        case 'md5':
            if hashlib.md5(full_card_num.encode()).hexdigest() == hash:
                return True
    return False


def num_selection():
    print('erw')
