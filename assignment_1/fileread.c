//
// Created by Victoria Hoang on 2024-05-22.
//

#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include "fileread.h"

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

int readFile(FILE *filePtr, char **words, char *wordType, char *skipWords[], int nbSkipWords) {
    // input: pointer to array of size n & array size n
    // output: array of size n containing pointers to strings

    char buffer[1000];
    int nbWords = 0;



    while (fscanf(filePtr, ))

    while (fgets(buffer, sizeof(buffer), filePtr)) {
        char *token;
        if (strcmp(wordType, "ALL") == 0) {
            token = strtok(buffer, "\t\n\v\f\r,");
        } else if (strcmp(wordType, "ALPHA") == 0) {
            for (char *i = buffer; *i; i++) {
                if (!isalpha(*i)) *i = ' ';
            }
            token = strtok(buffer, "\t\n\v\f\r,");
        } else if (strcmp(wordType, "ALPHANUM") == 0) {
            for (char *i = buffer; *i; i++) {
                if (!isalnum(*i)) *i = ' ';
            }
            token = strtok(buffer, "\t\n\v\f\r,");
        }

        while (token) {
            addToArray(token, words, &nbWords, skipWords, nbSkipWords);
            if (strcmp(wordType, "ALL") == 0) {
                token = strtok(NULL, " \t\n\v\f\r,");
            } else {
                token = strtok(NULL, " \t\n\v\f\r");
            }
        }
    }
    fclose(filePtr);
    return nbWords;

}
