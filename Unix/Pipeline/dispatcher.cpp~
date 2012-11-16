#include <unistd.h>
#include <sys/wait.h>
#include <iostream>
#include <cstdlib>
#include <stdio.h>

using namespace std;
//0 = read 1 = write
int main(){
	int pipefd[2]; //creats an array of size 2
	pid_t pid, pid1; //initializes 2 process
	int status, status1;
	pipe(pipefd); //create a pipe
	pid = fork(); //create a child process
	
	if(pid == 0){ //if child process
		dup2(pipefd[1],STDOUT_FILENO); //set the stdout to the write side of the pipe
		close(pipefd[0]); //close the array 
		close(pipefd[1]);
		if(execv("./generator", NULL)<0){ //run the program generator
			perror("Execv generator");
			exit(1);
		}
	}
	
	pid1 = fork(); //create a second child process

	if(pid1 == 0){ //if child process
		dup2(pipefd[0],STDIN_FILENO); //set the stdin to the left side of the pipe
		close(pipefd[1]);
		close(pipefd[0]);
		if(execv("./consumer", NULL)<0){
			perror("Execv consumer");
			exit(1);
		}
	}
	
	close(pipefd[1]); //close the pipes in the main process
	close(pipefd[0]);
	sleep(1); //dealy 1 second
	
	kill(pid,  SIGTERM); //kill the program ./generator
	waitpid(pid,&status, 0); //wait till process terminates
	cerr << "child[" << pid << "] exited with status " << status<< endl; //print termination statement and status
	waitpid(pid1,&status1, 0);
	cerr << "child[" << pid1 << "] exited with status " << status1<< endl;	
	return 0;
 }
   
 
	

	


