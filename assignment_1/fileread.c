//
// Created by Victoria Hoang on 2024-05-22.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "fileread.h"
#include "wordtype.h"

static int compareAscending(const void* a, const void* b) {
    return strcmp(*(const char**)a, *(const char**)b);
}

static int compareDescending(const void* a, const void* b) {
    return strcmp(*(const char**)b, *(const char**)a);
}

void sort(const char* arr[], int n, char *sortType) {
    if (strcmp(sortType, "DESC") == 0) {
        qsort(arr, n, sizeof(const char*), compareDescending);
    } else {
        qsort(arr, n, sizeof(const char*), compareAscending);
    }
}

int readFile(FILE *filePtr, char **words, int arraySize, char *wordType, char *skipWords[], int nbSkipWords, char *sortType) {
    // input: pointer to array of size n & array size n
    // output: array of size n containing pointers to strings

    int nbWords = 0;
    char buffer[100];
    char whitespace[100];
    char charToDiscard[100];

    processInputWordType(wordType, whitespace, charToDiscard);

    // add to array if not a skipword
    while (fscanf(filePtr, whitespace, buffer) == 1 && nbWords < arraySize) {
        int notSkipWord = 1;
        for (int i = 0; i < nbSkipWords; i++) {
            if (strcmp(buffer, skipWords[i]) == 0) {
                notSkipWord = 0;
                break;
            }
        }
        if (notSkipWord) {
            words[nbWords++] = strdup(buffer);
            if (words[nbWords] == NULL) {
                // strdup failure, free allocated memory
                for (int i = 0; i < nbWords; i++) {
                    free(words[i]);
                }
                fclose(filePtr);
                return nbWords;
            }
        }

        // discard unwanted chars until hit desired char (for next word)
        fscanf(filePtr, charToDiscard, buffer);
    }

    // sort array according to sort type
    sort((const char **) words, nbWords, sortType);

    return nbWords;
}
