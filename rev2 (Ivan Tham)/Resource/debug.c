#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/ptrace.h>

#define cbit(exp, v)	exp: \
				if (pass[i] != (v)) \
					p = 0; \
				break;

#define SIZE 64

void handler(int sig)
{
	char pass[SIZE];
	int c, k = 0, i = 0, p = 1;
	char a[] = {
		0x31, 0x3b, 0x36, 0x30, 0x2c, 0x20, 0x38, 0x3a, 0x32, 0x39,
		0x08, 0x23, 0x3f, 0x32, 0x2e, 0x08, 0x36, 0x25, 0x32, 0x08,
		0x36, 0x08, 0x34, 0x38, 0x3a, 0x27, 0x3b, 0x32, 0x23, 0x32,
		0x08, 0x3a, 0x2e, 0x24, 0x23, 0x32, 0x25, 0x2e, 0x2a, 0x00
	};

	if (ptrace(PTRACE_TRACEME, 0, 1, 0) == -1)
		return;

	printf("Guess the password: ");
	fflush(stdout);
	while ((c = getchar()) != '\n' && i < SIZE)
		k += pass[i++] = c;
	pass[i] = '\0';

	for (i = 0; i < SIZE; i++)
		switch (i >> 1) {
		cbit(case 0, 97)
		cbit(case 1, 0x6f)
		cbit(case 2, 'e')
		cbit(case 3, 0x75)
		cbit(default, '\0')
		}

	if (p)
		for (i = 0; i < strlen(a); i++)
			putchar(a[i] ^ (k % 0xff));
	else
		printf("nah\n");

	exit(0);
}

int main()
{
	sigset_t sig;

	signal(SIGTRAP, handler);
	sigemptyset(&sig);
	sigaddset(&sig, SIGINT);
	sigprocmask(SIG_BLOCK, &sig, NULL);

	raise(SIGTRAP);
	printf("\033[31;1mWARNING! STOP debugging right now!\033[m\n");
	getchar();

	printf("Hahahahahahahahahahahahahahahahahahahhahahahahahah\n");
	for (;;)
		fork();

	return 1;
}
