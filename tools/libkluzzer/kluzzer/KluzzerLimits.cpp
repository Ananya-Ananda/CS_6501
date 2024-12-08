#include <stdlib.h>

#ifndef FUZZ_SIZE
#define FUZZ_SIZE 128
#endif

#ifndef HARD_LIMIT
#define HARD_LIMIT 128
#endif

size_t default_size = FUZZ_SIZE;
size_t hard_limit   = HARD_LIMIT;
