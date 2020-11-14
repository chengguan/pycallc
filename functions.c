/*
	Build instruction:
		cc -fPIC -shared -o functions.so functions.c
		
	Source: https://www.journaldev.com/31907/calling-c-functions-from-python
*/

#include <stdio.h>

int square(int i) 
{
	return i * i;
}

int print_string(int a , char *pBuf)
{
	sprintf(pBuf, "%d is printed.", a);

	return a;
}