#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys

import _pyhash

fnv1_32 = _pyhash.fnv1_32
fnv1a_32 = _pyhash.fnv1a_32
fnv1_64 = _pyhash.fnv1_64
fnv1a_64 = _pyhash.fnv1a_64

lookup3 = _pyhash.lookup3_little if sys.byteorder == 'little' else _pyhash.lookup3_big
lookup3_little = _pyhash.lookup3_little
lookup3_big = _pyhash.lookup3_big

super_fast_hash = _pyhash.super_fast_hash

city_64 = _pyhash.city_64
city_128 = _pyhash.city_128

spooky_32 = _pyhash.spooky_32
spooky_64 = _pyhash.spooky_64
spooky_128 = _pyhash.spooky_128

import unittest
import logging

class TestHasher(unittest.TestCase):
    def setUp(self):
        self.data = b'test'
        self.udata = u'test'

    def doTest(self, hasher_type, bytes_hash, seed_hash, unicode_hash):
        hasher = hasher_type()

        self.assertEqual(bytes_hash, hasher(self.data))

        self.assertEqual(seed_hash, hasher(self.data, seed=bytes_hash))

        self.assertEqual(seed_hash, hasher(self.data, self.data))

        self.assertEqual(unicode_hash, hasher(self.udata))

class TestFNV1(TestHasher):
    def testFNV1_32(self):
        self.doTest(hasher_type=fnv1_32,
                    bytes_hash=3698262380L,
                    seed_hash=660137056,
                    unicode_hash=3910690890L)

    def testFNV1a_32(self):
        self.doTest(hasher_type=fnv1a_32,
                    bytes_hash=1858026756,
                    seed_hash=1357873952,
                    unicode_hash=996945022)

    def testFNV1_64(self):
        self.doTest(hasher_type=fnv1_64,
                    bytes_hash=17151984479173897804L,
                    seed_hash=6349570372626520864L,
                    unicode_hash=14017453969697934794L)

    def testFNV1a_64(self):
        self.doTest(hasher_type=fnv1a_64,
                    bytes_hash=11830222609977404196L,
                    seed_hash=8858165303110309728L,
                    unicode_hash=14494269412771327550L)


class TestLookup3(TestHasher):
    def testLookup3(self):
        self.doTest(hasher_type=lookup3,
                    bytes_hash=3188463954L,
                    seed_hash=478901866,
                    unicode_hash=1380664715)


class TestSuperFastHash(TestHasher):
    def testSuperFastHash(self):
        self.doTest(hasher_type=super_fast_hash,
                    bytes_hash=942683319,
                    seed_hash=777359542,
                    unicode_hash=1430748046)


class TestCityHash(TestHasher):
    def testCityHash64(self):
        self.doTest(hasher_type=city_64,
                    bytes_hash=17703940110308125106L,
                    seed_hash=8806864191580960558L,
                    unicode_hash=7557950076747784205L)

        self.assertFalse(hasattr(city_64, 'has_sse4_2'))

    def testCityHash128(self):
        self.doTest(hasher_type=city_128,
                    bytes_hash=195179989828428219998331619914059544201L,
                    seed_hash=206755929755292977387372217469167977636L,
                    unicode_hash=211596129097514838244042408160146499227L)

        self.assertTrue(city_128.has_sse4_2, "support SSE 4.2")


class TestSpookyHash(TestHasher):
    def testSpookyHash32(self):
        self.doTest(hasher_type=spooky_32,
                    bytes_hash=1882037601L,
                    seed_hash=1324274298L,
                    unicode_hash=2977967976L)

    def testSpookyHash64(self):
        self.doTest(hasher_type=spooky_64,
                    bytes_hash=10130480990056717665L,
                    seed_hash=1598355329892273278L,
                    unicode_hash=4093159241144086376L)

    def testSpookyHash128(self):
        self.doTest(hasher_type=spooky_128,
                    bytes_hash=241061513486538422840128476001680072033L,
                    seed_hash=315901747311404831226315334184550174199L,
                    unicode_hash=207554373952009549684886824908954283880L)

if __name__ == '__main__':
    if "-v" in sys.argv:
        level = logging.DEBUG
    else:
        level = logging.WARN

    logging.basicConfig(level=level, format='%(asctime)s %(levelname)s %(message)s')

    unittest.main()
