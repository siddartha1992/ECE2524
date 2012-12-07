#include "Process.h" //includes the header file Process.h

/* Initialize the process, create input/output pipes */
Process:: Process(const std::vector<std::string> &args)
{
	if(args.size() < 1){ //invalid argument size
		perror("Invalid argument size");
		throw ("Invalid argument size");
	}
	if(pipe(readpipe) == -1){ //error creating the read pipe
		perror("error creating the read pipe");
		throw ("error creating the read pipe");
	}
	if(pipe(writepipe) == -1){ //error creating the write pipe
		perror("error creating the write pipe");
		throw ("error creating the write pipe");
	}

	m_pid = fork(); //fork a child process

	if(m_pid < 0){ //if any problem creating a  child
		perror("error creating the fork");
		throw ("error creating the fork");
	}

	else if(m_pid == 0){ //if child process
		close(writepipe[1]); //close the write end of the parent
		close(readpipe[0]); //close the read end of the parent
		
		if((dup2(readpipe[1],1))==-1){  //attach the write end of the pipe to the child write end
			close(readpipe[1]); //close the right end of the child write
			perror("error on readpipe[1] of dup2");
			throw ("error on readpiple[1] of dup2");
		}
		close(readpipe[1]); 
	
		if((dup2(writepipe[0],0)) == -1){ //attach the read end of the pipe to the child read end 
			close(writepipe[0]);
			perror("error on writepipe[0] of dup2");
			throw ("error on writepipe[0] of dup2");
		}
		close(writepipe[0]); //close the read end of the child
		
		std::vector<const char*> cargs; //pass the arguments
		std::transform(args.begin(), args.end(), std::back_inserter(cargs), [](const std::string s){return s.c_str();});
		cargs.push_back(NULL); // exec expects a NULL terminated array

		if(execv(cargs[0], const_cast<char**>(&cargs[0])) ==-1){ //execute the command ./consumer
			perror("error running the generator program");
			exit(-1);
		}
	}
	else{ //if parent processes
		close(readpipe[1]); //close the childs write
		close(writepipe[0]);//close the childs read
		m_pread = fdopen(readpipe[0], "r"); //open the file
		cout << "Parent ["<<pid()-1<<"] Process constructor"<<endl; //display the parent process number
	}

}

/* Close any open file streams or file descriptors,
       insure that the child has terminated */
Process::~Process(){
	fclose(m_pread); //close the file
	close(writepipe[1]); //close all the pipes
	close(readpipe[0]);
	int status;
	
	if(waitpid(m_pid, &status, 0) == -1){ //wait till the process terminates
		perror ("error terminating process");
		throw ("error terminating process");
	}

	kill(m_pid, SIGTERM); //kill the process
}

/* write a string to the child process */
void Process::write(const std::string& cur_str){
	if((::write(writepipe[1], cur_str.c_str(), cur_str.length()))==-1){//writes the string to the child process
		perror("error writing to pipe");
		throw ("error writing to pipe");	//fails throwns an exception
	}
	
}

/* read a full line from child process, 
       if no line is available, block until one becomes available */
std::string Process::readline(){
	size_t temp_size; //create temporary variables
	char* temp = NULL;
	string line;
	if((getline(&temp, &temp_size, m_pread)) == -1){ //read a line from child process if fails throw an error
		perror ("error reading line");
		throw ("error reading line");
	}
	line = temp; //returns the line which is stored as a buffer
	return line;
}


