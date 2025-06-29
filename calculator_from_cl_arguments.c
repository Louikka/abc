#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    float a = atof( argv[1] );
    float b = atof( argv[3] );

    switch ( *argv[2] ) {

        case '+':
            printf("%g\n", a + b);
        break;

        case '-':
            printf("%g\n", a - b);
        break;

        case '*':
            printf("%g\n", a * b);
        break;

        case '/':
            printf("%g\n", a / b);
        break;

    }

    return 0;
}
