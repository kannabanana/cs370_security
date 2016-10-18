import java.util.concurrent.Semaphore;

//forks = chopsticks
public class Chopstick {

    public Semaphore mutex;
    public boolean dirty_f;
    public int place_holder;
    public int name;
 

	//constructor 
   public Chopstick(int name, int h){
        this.dirty_f = true;
        this.mutex = new Semaphore(1);
        this.place_holder = h;
        this.name = name;  
    }


	//check if something is dirty, pass it to neighbor if it's not, otherwise hold onto it

    public synchronized void getStick(int holderID){
        while(this.place_holder != holderID) {
            try {
                if (this.dirty_f) {
                    try {
                        mutex.acquire();		//lock
                        System.out.printf("%s passes chopstick%s to %s\n", name, place_holder, holderID);
                         this.dirty_f = false;		//it's no longer dirty
                         this.place_holder = holderID;	//set the id to the neighbor's id
                    } catch (InterruptedException e) {		//in case it wasn't
                        e.printStackTrace();		
                    } finally {
                        mutex.release();		//release
                    }
                } else {
                    System.out.printf("%s couldn't pass chopstick%s to %s\n", place_holder, name, holderID);
		    wait();
                }
	
 	//from first try block
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }


	//synchronize threads
    public synchronized void setDirty(boolean set){
        this.dirty_f = set;
        notifyAll();		//wake up all waiting threads
    }


	//lock the chopstick
    public void lock_chop(){
        try {
            mutex.acquire();
        } catch (InterruptedException e) {		//exception is thrown so it must be caught
            e.printStackTrace();
        }
    }


	//unlock the chopstick
    public void unlock_chop(){
  //       try {
          mutex.release();
  // 	 }
//	catch(InterruptedException e)
//	{
//		e.printStackTrace();
//	}
   }


}
