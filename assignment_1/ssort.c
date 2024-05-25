//
// Created by Victoria Hoang on 2024-05-22.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ssort.h"

// argc: number of values passed to command line incl. program name !!
// argv: array of char pointers listing all arguments (> 0 => argv[0:argc - 1] = array of pointers to strings
// argv[0] = name of program
// argv = {programName, fileName, array size n, wordtype, sorttype, skipkeywords...}
int main(int argc, char *argv[]) {

    FILE *filePtr;

    int n; // array size

    filePtr = fopen(argv[1], "r");
    if (filePtr == NULL) {
        printf("Error opening file %", argv[1]);
        return 1;
    }

    char ch;
    while ((ch = fgetc(filePtr)) != EOF)
        putchar(ch);

    return 0;
}