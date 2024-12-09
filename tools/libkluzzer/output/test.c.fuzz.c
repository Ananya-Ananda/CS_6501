#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 16

void process_input(const char *input) {
    char buffer[BUFFER_SIZE];
    strcpy(buffer, input);
    printf("Processed input: %s\n", buffer);
}

int __FuzzMe() {
    char test_input[] = "Test string exceeding buffer size!";
    process_input(test_input);
    return 0;
}
void __fuzzer_save_ctx() {
}
void __fuzzer_restore_ctx() {
}
