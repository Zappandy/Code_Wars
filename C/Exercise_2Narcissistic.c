#include <math.h> // power  must include -lm flag when compiling with either clang or gcc
#include <stdio.h> // atoi itoa
#include <stdlib.h> // atoi itoa
#include <stdbool.h>
bool narcissistic(int num);
int num_dig(int num);


int main(int argc, const char* argv[])
{
	if (argc == 2)
	{
		narcissistic(atoi(argv[1])); // exercise's input is an int
	}
}

bool narcissistic(int num)
{
	int total = 0;
	int len = num_dig(num);
	int nar_num = num;
	do
        {
		total = total + pow((nar_num % 10), len);
        	nar_num /= 10;
        }
        while (nar_num > 0);
	if (total == num)
	{
		return true;
	}
	else
	{
		return false;
	}
}

int num_dig(int num)
{
	int len = 0;
	do
	{
		len++;
		num /= 10;
	}
	while (num > 0);
	return len;
}
