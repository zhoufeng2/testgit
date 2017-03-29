
#ifndef TBSYS_THREAD_H_
#define TBSYS_THREAD_H_

#include <linux/unistd.h>
#include <pthread.h>
#include "Runnable.h"


class CThread
{
public:
	CThread();
	~CThread() {}

	bool start(Runnable *r, void *args);
	void join();
	Runnable *getRunnable();
	void *getArgs();
	int getpid();

    static void *hook(void *arg);

private:
	static pid_t gettid();

private:
	pthread_t m_tid;
	int m_pid;
	Runnable *m_runnable;
	void *m_args;
	
};

#endif /*THREAD_H_*/