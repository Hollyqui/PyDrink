import java.util.ArrayList;
import java.util.Collections;

// adds drinks consumed by user
public class Addition {
    private double height;
    private double weight;
    private double minute;
    private ArrayList<Double> timeList=new ArrayList<Double>();

    private  double eliminationRate = 0.018;



    // init
    public Addition(double height, double weight, int minute){
        this.height = height;
        this.weight = weight;
        this.minute = minute;
    }

    // find widmark factor
    private double widmark(double weight, double height, boolean gender){
        double temp = weight/Math.pow((height/100d),2); // find BMI
        if(gender){
            return 1.0181 - 0.01213 * temp; // return male widmark factor
        }
        else{
            return 0.9367 - 0.01240 * temp; // return female widmark factor
        }
    }

    // adds the drink
    private double drink(int volume, double percent, int minutes, double halfLife){
        double temp = minutes/halfLife; // find how many halflives passed
        return  (volume/1000d)*(percent/100d)- (volume/1000d)*(percent/100d) * Math.pow(0.5, temp); // find alcohol is absorbed
    }

    // calculated bac based on how much alcohol is in the body at the moment
    private double bacCalculator(double alcohol, double widmarkFactor, double weight){
        // find bac and if it is below zero return 0
        double C= Math.max((100d * alcohol * 0.78974) / (widmarkFactor * weight),0); // 0.78974 = density of alcohol
        return C;
    }


    // creates an array containing the total amount of alcohol absorbed by the body
    public ArrayList<Double> totalConsumed(int volume, double percent, int time, double halfLife, boolean gender){
        ArrayList<Double> tempTimeList=new ArrayList<Double>();
        time = -time;
        while (tempTimeList.size() < 1440 + minute){ // iterates through 24 hours after alcohol intake
            double absoluteConcentration = drink(volume, percent, time, halfLife);
            tempTimeList.add(bacCalculator(absoluteConcentration, widmark(weight,height,gender), weight));
            time++;
        }
        if(timeList.size() == 0){
            timeList = tempTimeList;
        }
        else{       // add lists together
            for (int i = 0; i < timeList.size(); i++) {
                timeList.set(i, timeList.get(i) + tempTimeList.get(i));
            }
        }
        return timeList;
    }

    // creates an array of the amount of blood in the alcohol (based on the 'totalConsumed method'
    public ArrayList<Double> eliminateAlc(ArrayList<Double> timeList){
        ArrayList<Double> eliminationList = new ArrayList<Double>();
        eliminationList.add(0d); // add 0 as starting point
        for (int i = 0; i < timeList.size(); i++) {
            // if there is alcohol in the blood, eleminate one minute worth of alcohol by increasing
            // the value appended in eleminationList, otherwise append the same value (e.g. don't eliminate
            // alcohol since the is none)
            if(timeList.get(i) - eliminationList.get(i)/60*eliminationRate > 0){
                eliminationList.add(eliminationList.get(i)+1);
            }
            else{
                eliminationList.add(eliminationList.get(i));
            }
        }
        eliminationList.remove(0); // remove the inital 0 stored in eliminationList
        for (int i = 0; i < timeList.size(); i++) {
            eliminationList.set(i, eliminationList.get(i)/60*eliminationRate);
            eliminationList.set(i,Math.max(0d, timeList.get(i)-eliminationList.get(i)));
        }
        return eliminationList;
    }

    public double getMaxtBAC(ArrayList<Double> bacList){
        return Collections.max(bacList);
    }

    public int timeUntilSober(ArrayList<Double> bacList, int currentTime){
        for (int i = bacList.size(); i < currentTime; i--){
            if(bacList.get(i)<=0) return i;
        }
    }

    public static void main(String[] args) {
        Addition add = new Addition(170, 60, 800);
        ArrayList<Double> a = add.totalConsumed(330, 20, 10, 12, true);
        a = add.eliminateAlc(a);
        for (int i = 0; i < a.size(); i++) {
            System.out.println(a.get(i));
        }
    }

}
