//import java.util.Random;		//random function generator

//class for philosophers a subclass of threads
public class Philosopher extends Thread {

    public int identity;	//name
    public Chopstick L;		//left chopstick
    public Chopstick R;		//right chopstick


    //constructor
    public Philosopher(int x, Chopstick lc, Chopstick rc){
        this.L = lc;
        this.R = rc;
	this.identity = x; 
   }


    public void run(){
	int min_t = 2000;
	int max_t = 9000;
	int randomNum=0;
	//infinite while loop
  while (true){
	System.out.printf("Philosopher %s is thinking\n", identity);

//	Random r = new Random();
//	int th = r.nextInt(max_t = min_t +1)+min_t;         
//	th = th*1000;
      //  Thread.sleep((long) ((int)(Math.random() * 9000)+2000));
      //       Thread.sleep((long) (Math.random() * 5000));
// 	sleepFun()
	thinking();
  
        L.getStick(identity);		//get the chopsticks
        R.getStick(identity);

        eat();
        System.out.printf("Philosopher %s has finished eating\r\n", identity);
        L.setDirty(true);		//put donw forks
        R.setDirty(true);
    }

    }

    public void thinking(){
	try{
          Thread.sleep((long) (Math.random() * 9000)+2000);
   	}
	catch(InterruptedException e){
            e.printStackTrace(); 	
	}

   }

    public void eat(){
        try {
            L.lock_chop();		//must lock and unlock before use
            R.lock_chop();
            System.out.printf("Philosopher %s is eating\n", identity);
            Thread.sleep((long) (Math.random() * 20000)+1000);
            L.unlock_chop();
            R.unlock_chop();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}
