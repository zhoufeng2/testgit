
#ifndef TBSYS_RUNNABLE_H_
#define TBSYS_RUNNABLE_H_

class CThread;

class Runnable 
{

public:
	Runnable() {}
	virtual ~Runnable() {}
	virtual void run(CThread *thread, void *arg) = 0;
};

#endif /*RUNNABLE_H_*/