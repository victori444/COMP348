//
// Created by Victoria Hoang on 2024-05-22.
//

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "fileread.h"
#include "wordtype.h"

// separate according to word type (alpha = 1, alphanum = 2, all = 3)
// check if == to skipwords
// add to array length n
// return array size n

int isSkipWord(const char *word, char *skipWords[], int nbSkipWords) {
    for (int i = 0; i < nbSkipWords; ++i) {
        if (strcmp(word, skipWords[i]) == 0) {
            printf("Here");
            return 1;
        }
    }
    return 0;
}

void addToArray(char *word, char **words, int *nbWords, char *skipWords[], int nbSkipWords) {
    if (!isSkipWord(word, skipWords, nbSkipWords)) {
        words[*nbWords] = strdup(word);
        (*nbWords)++;
    }
}

void readFile(FILE *filePtr, char **words, int *nbWords, char *wordType, char *skipWords[], int nbSkipWords) {
    // input: pointer to array of size n & array size n
    // output: array of size n containing pointers to strings

    char buffer[100];
    char whitespace[100];
    char charToDiscard[100];

    processInputWordType(wordType, whitespace, charToDiscard);

    while (fscanf(filePtr, whitespace, buffer) == 1) {
//        printf("%s\n", buffer);
        int notSkipWord = 1;
        for (int i = 0; i < nbSkipWords; i++) {
            if (strcmp(buffer, skipWords[i]) == 0) {
                notSkipWord = 0;
            }
        }
        if (notSkipWord) {
            words[*nbWords++] = buffer;
        }

        // discard unwanted chars until hit desired char (for next word)
        fscanf(filePtr, charToDiscard, buffer);

    }
    fclose(filePtr);

}
