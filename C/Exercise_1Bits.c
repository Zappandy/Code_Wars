#include <stddef.h>  // size_t
#include <stdlib.h>  // atoi
size_t countBits(unsigned value);

int main(int argc, const char* argv[])
{
        if (argc == 2)
	{
		countBits(atoi(argv[1]));		
	}
}

size_t countBits(unsigned value)
{
	unsigned bin_dig;
	long count = 0;  // declared long because function returns an unsigned long long
	while (value > 0)
	{
		bin_dig = value % 2;
		value /= 2;
		if (bin_dig == 1)
		{
			count++;
		}
	}
	return count;
}
