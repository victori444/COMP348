cmake_minimum_required(VERSION 3.28)
project(COMP348_A1 C)

set(CMAKE_C_STANDARD 11)

add_executable(COMP348_A1
        assignment_1/ssort.c
        assignment_1/ssort.h
        assignment_1/wordtype.c
        assignment_1/wordtype.h
        assignment_1/fileread.c
        assignment_1/fileread.h
        assignment_1/output.c
        assignment_1/output.h)
