add_executable(aget
        Aget.c
        Download.c
        Head.c
        main.c
        Misc.c
        Resume.c
        Signal.c)
target_include_directories(aget PUBLIC include)
target_link_libraries(aget pthread)
target_compile_options(aget PRIVATE ${TEST_FLAGS})

