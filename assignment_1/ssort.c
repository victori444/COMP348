//
// Created by Victoria Hoang on 2024-05-22.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "ssort.h"
#include "fileread.h"

// argc: number of values passed to command line incl. program name !!
// argv: array of char pointers listing all arguments (> 0 => argv[0:argc - 1] = array of pointers to strings
// argv[0] = name of program
// argv = {programName, fileName, array size n, wordtype, sorttype, skipkeywords...}
int main(int argc, char *argv[]) {

    if (argc < 4) {
        fprintf(stderr, "Invalid amount of inputs. Format: %s <inputFile> <n> <wordtype> <sorttype> [<skipword1>, <skipword2>, ...]\n", argv[0]);
        return 1;
    }

    // input file
    FILE *filePtr = fopen(argv[1], "r");
    if (filePtr == NULL) {
        printf("Error opening file %s", argv[1]);
        return 1;
    }

    // array size n
    int n = atoi(argv[2]);
    if (n <= 0) {
        fprintf(stderr, "Invalid array size.");
        return 1;
    }

    // wordtype
    char *wordType = argv[3];

    // sorttype
    char *sortType;
    if (argc == 4) sortType = "ASC";
    else if (strcmp(argv[4], "DESC") == 0) sortType = "DESC";
    else sortType = "ASC";

    // array of skipwords
    char *skipWords[100];
    int nbSkipWords = 0;
    if (argc > 5) {
        for (int i = 5; i < argc; i++) {
            skipWords[nbSkipWords++] = argv[i];
        }
    }

    // word array
    // add exception handling if arraySize input is not an integer or < 0
    char **wordArray = malloc(n * sizeof(char *));

    // amount of valid words added to array
    int *nbWords = 0;
    readFile(filePtr, wordArray, nbWords, wordType, skipWords, nbSkipWords);
    printf("%d", *nbWords);

    return 0;
}