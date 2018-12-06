#include <stdio.h>

#define HAVE_REMOTE
#include "pcap.h"

int main()
{
	char errbuf[PCAP_ERRBUF_SIZE+1];
	char source[PCAP_ERRBUF_SIZE+1];
  	/* Create the source string according to the new WinPcap syntax */
	if ( pcap_createsrcstr(	source,			// variable that will keep the source string
							PCAP_SRC_FILE,	// we want to open a file
							NULL,			// remote host
							NULL,			// port on the remote host
							"nofile.pcap",  // name of the file we want to open
							errbuf			// error buffer
							) != 0)
	{
		fprintf(stderr,"\nError creating a source string\n");
		return -1;
	}
	
	fprintf(stdout,"\nSuccessfully exercised types from WinPCAP library.\n");
	return 0;
}


