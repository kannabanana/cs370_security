/*
 *#SR Kanna
#CS444 - Spring 2016
#4/12/2016

#Concurrency 2 description: This is the dining philospher's problem. There are five philosphers and five forks, where they can only eat and think. In order to eat, both forks must be used by the philospher. Deadlock or starvation must not occur. Furthermore, one philosopher must be eating at all times. Each philosopher alternates between thinking, waiting for a fork, eating and releasing the fork. Eating can last between 2-9s. Thinking varies between 1-20s.

######################################

#Table
#P = Philosopher
#F = Fork

#           f5
#         P5   P1
#	f4       f1
#      P4        P2
#       f3     f2
#          P3

######################################


*/

public class Eat {

	//array of forks and philosophers
	public Chopstick chopsticks[];	
	public Philosopher philosophers[];

	public Eat(){

		chopsticks = new Chopstick[5];
		philosophers = new Philosopher[5];

		System.out.printf("In the beginning: \n\n");

		//there are five philosophers
		for (int i=0; i<5; ++i){
			/* 
			   int pid;
			   if (i < ((i+4)%5)){
			   pid = i;
			   } else {
			   pid = ((i+4)%5);
			   }
			   */
			//i = 0 = 4 pid = 0,0

			//else i= 1 = 0 pid = 1,0
			//else i = 2 - 1 pid = 2,1
			//else i = 3 - 2 pid = 3,2
			//else i = 4 - 3 pid = 4,3

			//assign chopsticks to philosophers so that one philosopher ends up with two chopsticks
			int phil_id = 0;
			if(i != 0)
				phil_id = i;
			else
				phil_id = 0+1;

			Chopstick chopstick = new Chopstick( i, phil_id);

			chopsticks[i] = chopstick;
			System.out.printf("Philosopher %s, has Chopstick number %s\n", phil_id, i);
		}


		System.out.printf("\n\n");

		//start the threads after a new philospher is made
		for (int i=0;i<5;++i){
			philosophers[i] = new Philosopher(i, chopsticks[i], chopsticks[(i+1)%5]);
			philosophers[i].start();
		}
	}


	public static void main(String[] args){
		//start it all
		new Eat();
	}
}
