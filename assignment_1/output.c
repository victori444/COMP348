//
// Created by Victoria Hoang on 2024-05-22.
//

#include <stdio.h>
#include "output.h"

void printWordArray(const char **words, int nbWords) {
    int count = 0;
    for (int i = 0; i < nbWords; i++) {
        if (count == 10) {
            printf("\n");
        }
        printf("%s ", words[i]);
        count++;
    }
}

// Error messages
int fileError() {
    fprintf(stderr, "Error opening file");
    return 1;
}
int arraySizeError() {
    fprintf(stderr, "Error code 1: Invalid array size.");
    return 1;
}
int wordTypeError() {
    fprintf(stderr,"Error code 2: Invalid word type");
    return 2;
}

