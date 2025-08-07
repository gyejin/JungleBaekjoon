#include <stdio.h>

struct Sample {
    char a;  // 1바이트
    short b;
    int c;   // 4바이트
};

int main(){
    struct Sample sp;
    printf("%zu", sizeof(sp));
    
    return 0;
}