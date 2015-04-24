#include "Hash.h"

#include "FNV1.h"
#include "Lookup3.h"
#include "SuperFastHash.h"
#include "CityHash.h"
#include "SpookyHash.h"

BOOST_PYTHON_MODULE(_pyhash)
{
  fnv1_32_t::Export("fnv1_32");
  fnv1a_32_t::Export("fnv1a_32");
  fnv1_64_t::Export("fnv1_64");
  fnv1a_64_t::Export("fnv1a_64");

  lookup3_little_t::Export("lookup3_little");
  lookup3_big_t::Export("lookup3_big");

  super_fast_hash_t::Export("super_fast_hash");

  city_hash_64_t::Export("city_64");
  city_hash_128_t::Export("city_128");

  spooky_hash_32_t::Export("spooky_32");
  spooky_hash_64_t::Export("spooky_64");
  spooky_hash_128_t::Export("spooky_128");
}
