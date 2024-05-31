//
// Created by Victoria Hoang on 2024-05-22.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileread.h"
#include "output.h"

int main(int argc, char *argv[]) {

    if (argc < 4) {
        fprintf(stderr, "Invalid amount of inputs. Format: %s <inputFile> <n> <wordtype> <sorttype> [<skipword1>, <skipword2>, ...]\n", argv[0]);
        exit(1);
    }

    // input file
    FILE *filePtr = fopen(argv[1], "r");
    if (filePtr == NULL) {
        fclose(filePtr);
        fileError();
    }

    // array of words size
    int arraySize = atoi(argv[2]);
    if (arraySize <= 0) { // non positive / non integer value
        // free memory
        fclose(filePtr);
        arraySizeError();
    }

    // word type
    char *wordType = argv[3];

    // sort type
    char *sortType;
    if (argc == 4) {
        sortType = "ASC";
    }
    else if (strcmp(argv[4], "DESC") == 0) {
        sortType = "DESC";
    }
    else {
        sortType = "ASC";
    }

    // array of skip words
    char *skipWords[100];
    int nbSkipWords = 0;
    if (argc > 5) {
        for (int i = 5; i < argc; i++) {
            skipWords[nbSkipWords++] = argv[i];
        }
    }

    // word array
    char **wordArray = malloc(arraySize * sizeof(char *));

    // amount of valid words added to array
    int nbWords = readFile(filePtr, wordArray, arraySize, wordType, skipWords, nbSkipWords, sortType);
    // output
    printWordArray((const char **) wordArray, nbWords);

    // free memory
    fclose(filePtr);
    free(wordArray);
    for (int i = 0; i < nbWords; i++) {
        free(wordArray[i]);
    }

    return 0;
}