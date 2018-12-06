#include <stdio.h>

#define HAVE_REMOTE
#include "pcap.h"

int main()
{
	char errbuf[PCAP_ERRBUF_SIZE+1];
	char source[PCAP_ERRBUF_SIZE+1];
	
	fprintf(stdout,"\nSuccessfully exercised types from WinPCAP library.\n");
	return 0;
}


