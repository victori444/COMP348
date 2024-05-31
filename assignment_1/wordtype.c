//
// Created by Victoria Hoang on 2024-05-22.
//

#include "wordtype.h"
#include <string.h>
#include "output.h"

void processInputWordType(const char *inputWordType, char *whitespace, char *charToDiscard) {

    char alpha[] = "ALPHA";
    char alphanum[] = "ALPHANUM";
    char all[] = "ALL";

    if (strcmp(inputWordType, alpha) == 0) {
        strcpy(whitespace, "%[^ 123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \\t\\n\\r\\x0b\\x0c]");
        strcpy(charToDiscard, "%*[ 123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \\t\\n\\r\\x0b\\x0c]");
    } else if (strcmp(inputWordType, alphanum) == 0) {
        strcpy(whitespace, "%[^ !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \\t\\n\\r\\x0b\\x0c]");
        strcpy(charToDiscard, "%*[ !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ \\t\\n\\r\\x0b\\x0c]");
    } else if (strcmp(inputWordType, all) == 0) {
        strcpy(whitespace, "%[^ ,\'\"\t\n\v\r]");
        strcpy(charToDiscard, "%*[ ,\'\"\t\n\v\r]");
    } else {
        wordTypeError();
    }

}