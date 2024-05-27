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

void processInputWordType(const char *inputWordType, char *whitespace, char *charToDiscard) {

    char alpha[] = "ALPHA";
    char alphanum[] = "ALPHANUM";
    char all[] = "ALL";

    if (strcmp(inputWordType, alpha) == 0) {
        strcpy(whitespace, "%[^ 123456789!@#$%^&*(){}[]|\\\t\n\v\r,]");
        strcpy(charToDiscard, "%*[ 123456789!@#$%^&*(){}[]|\\\t\n\v\r,]");
    } else if (strcmp(inputWordType, alphanum) == 0) {
        strcpy(whitespace, "%[^ !@#$%^&*(){}[]|\\\t\n\v\r,]");
        strcpy(charToDiscard, "%*[ !@#$%^&*(){}[]|\\\t\n\v\r,]");
    } else if (strcmp(inputWordType, all) == 0) {
        strcpy(whitespace, "%[^ , \t\n\v\r]");
        strcpy(charToDiscard, "%*[ , \t\n\v\r]");
    } else {
        printf("Invalid word type: %s", inputWordType);
        exit(2);
    }

}