add_executable(dedup
        binheap.c
        decoder.c
        dedup.c
        encoder.c
        hashtable.c
        queue.c
        rabin.c
        tree.c
        util.c)
target_include_directories(dedup PUBLIC include)
target_link_directories(dedup PRIVATE lib)
target_link_libraries(dedup pthread dl
        libcrypto.a
        libssl.a
        libz.a)
