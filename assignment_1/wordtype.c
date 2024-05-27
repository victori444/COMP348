//
// Created by Victoria Hoang on 2024-05-22.
//

#include "wordtype.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/* if wordtype = ALPHA -> word = [a-z] & [A-Z] => isalpha(char)
 * if wordtype = ALPHANUM -> word = [a-z] & [A-Z] & numbers => isalnum(char)
 * if wordtype = ALL -> non-whitespace (blank, tab, null, newline) & non-commas => char == ' ' / ',' / '\t' / '\n'
 * */

int processInputWordType(const char *word, const char *inputWordType) {

    char alpha[] = "ALPHA";
    char alphanum[] = "ALPHANUM";
    char all[] = "ALL";

    if (strcmp(inputWordType, alpha) == 0) {
        for (int i = 0; word[i] != '\0'; ++i) {
            if (!isalpha(word[i])) {
                return 0;
            }
        }
        return 1;
    } else if (strcmp(inputWordType, alphanum) == 0) {
        for (int i = 0; word[i] != '\0'; ++i) {
            if (!isalnum(word[i])) {
                return 0;
            }
        }
        return 1;
    } else if (strcmp(inputWordType, all) == 0) {
        return 1;
    } else {
        printf("Invalid word type: %s", inputWordType);
        exit(2);
    }

}