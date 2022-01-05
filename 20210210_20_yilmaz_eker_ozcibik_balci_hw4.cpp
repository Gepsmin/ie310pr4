#include <iostream>
#include <stdlib.h>
#include <math.h>

#define eps 0.0001


using namespace std;


////MIN FUNCTION !!!!!

double func(double x){ //x radyan burda derece olucaksa x*3.14159/180 olmali
    return 10 + (0.01*x) - (0.1*x*x) + (0.8*cos(3*x));      
}


int main(){
    int step=0;

    double x = -3.0;                     // initial point is middle of the search interval
    double a = -4.0, b = -2.036;           // search interval
    cout<<"Initial point: ("<<x<<","<<func(x)<<") and search interval is: ["<<a<<", "<<b<<"]\n";
    while (b-a >= eps){

        cout<<"Step: "<<step;
        cout<<" Search interval is: ["<<a<<", "<<b<<"] \t";

        x = (a+b)/2;
        double funcc = func(x);    // funcc hold that value of the point so that we do not need to calculate func(x) over and over again for the same x 

        if(func(x+eps) <= funcc) 
            a=x;
        else 
            b=x;

        
        cout<<"Point is: (" <<x<< "," <<funcc<< ")\n"; 
        step++;
    }
    cout<<"Algorithm ended\nFinal local optimum point is: "<<x<<" and value of that point is: "<<func(x)<<endl;


    
    
    return  0;
}