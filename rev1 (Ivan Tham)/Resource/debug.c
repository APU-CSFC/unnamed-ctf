#include <stdio.h>
#include <unistd.h>
#include <sys/ptrace.h>

#define SIZE 64

int main()
{
	char pass[SIZE];
	int c, i = 0;
	char a[] = { 0x66, 0x6c, 0x61, 0x67, 0x7b, 0x53, 0x65, 0x6d, 0x70, 0x65, 0x72, 0x20, 0x46, 0x69, 0x2c, 0x20, 0x64, 0x75, 0x64, 0x65, 0x2e, 0x7d, 0x00 };
	char k[] = { 0x78, 0x65, 0x6e, 0x6f, 0x6e, 0x00 };

	if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1)
		return 1;

	printf("Guess the password: ");
	fflush(stdout);
	while ((c = getchar()) != '\n' && i < SIZE)
		pass[i++] = c;
	pass[i] = '\0';

	sleep(1);

	for (i = 0; pass[i] != '\0' || k[i] != '\0'; i++)
		if (pass[i] != k[i])
			return 1;

	for (i = 0; a[i] != '\0'; i++)
		putchar(a[i]);

	return 0;
}
