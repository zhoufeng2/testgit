#include "CDefaultRunnable.h"
#include <stdio.h>

CDefaultRunnable::CDefaultRunnable(int threadCount)
{
	m_stop = false;
	m_threadCount = threadCount;
	m_thread = NULL;
}

CDefaultRunnable::~CDefaultRunnable()
{
	if (m_thread) {
		delete[] m_thread;
		m_thread = NULL;
	}
}

void CDefaultRunnable::setThreadCount(int threadCount)
{
    if (NULL != m_thread) {
    	printf("%s\n","the process is already running");
    	return;
    }
    m_threadCount = threadCount;
}

int CDefaultRunnable::start() 
{
    if (NULL != m_thread || m_threadCount < 1) {
        printf("%s\n", "start failure");
        return 0;
    }

    m_thread = new CThread[m_threadCount];
    if (NULL == m_thread) {
        printf("%s\n", "create m_thread failed");
        return 0;
    }

    int count = 0;
    for(; count < m_threadCount; count++) {
        if (!m_thread[count].start(this, &count)) {
            return count;
        }
    }
    return count;
}

void CDefaultRunnable::stop()
{
	m_stop = true;
}

void CDefaultRunnable::wait()
{
	if (NULL != m_thread) {
        for (int i = 0; i < m_threadCount; ++i) {
            m_thread[i].join();
        }
	}
}



