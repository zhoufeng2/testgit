#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include "CThread.h"

CThread::CThread() 
{
    m_tid = 0;
	m_pid = 0;
}

bool CThread::start(Runnable *r, void *args)
{
    m_runnable = r;
    m_args = args;
    sleep(1);
    return 0 == pthread_create(&m_tid, NULL, CThread::hook, this);
}

void CThread::join()
{
	if (m_tid) {
        pthread_join(m_tid, NULL);
        m_tid = 0;
        m_pid = 0;
	}
}

Runnable *CThread::getRunnable()
{
	return m_runnable;
}

void *CThread::getArgs()
{
	return m_args;
}

int CThread::getpid()
{
	return m_pid;
}

pid_t CThread::gettid()
{
	return syscall(SYS_gettid);
}

void * CThread::hook(void *arg)
{
	CThread *thread = (CThread*) arg;
	thread->m_pid = gettid();
	Runnable *r = thread->getRunnable();
	printf("%d\n", *(int*)thread->getArgs());
	if (r) {
        r->run(thread, thread->getArgs());
	}

	return (void*) NULL;
}
