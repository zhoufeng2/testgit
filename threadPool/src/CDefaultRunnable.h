
#ifndef TBSYS_DEFAULT_RUNNABLE_H_
#define TBSYS_DEFAULT_RUNNABLE_H_

#include "Runnable.h"
#include "CThread.h";

class CDefaultRunnable : public Runnable 
{
    
public:
	CDefaultRunnable(int threadCount = 1);
	virtual ~CDefaultRunnable();
	void setThreadCount(int threadCount);
	int start();
	void stop();
	void wait();

protected:
	CThread *m_thread;
	int m_threadCount;
	bool m_stop;
};

#endif /*DEFAULT_RUNNABLE_H_*/