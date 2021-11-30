add_executable(blackscholes blackscholes-pthread.cpp)
target_link_libraries(blackscholes pthread)
target_compile_options(blackscholes PRIVATE ${TEST_FLAGS} "-DENABLE_THREADS" "-DPARALLEL" "-DNCO=2" "-DN=960")

