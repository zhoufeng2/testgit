#ifndef MY_THREAD_H_
#define MY_THREAD_H_

#include "CDefaultRunnable.h"

class CThread;

class MyThread : public CDefaultRunnable
{

public:
	MyThread(int threadCount);
	~MyThread();
	void run(CThread *thread, void *arg);
	
};

#endif /*MY_THREAD_H_*/