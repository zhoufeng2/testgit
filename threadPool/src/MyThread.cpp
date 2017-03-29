#include "MyThread.h"
#include <stdio.h>

MyThread::MyThread(int threadCount)
    :CDefaultRunnable(threadCount)
{

}

MyThread::~MyThread()
{

}

void MyThread::run(CThread *thread, void *arg)
{
	int val = *(int*)arg;
    printf("%s %d\n", "MyThread", val);
}