#include <unistd.h>
#include <stdio.h>
#include "src/MyThread.h"

int main()
{
    MyThread my(10);
    my.start();
    my.wait();
	return 0;
}
