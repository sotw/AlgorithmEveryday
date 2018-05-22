#include <sstream>
#include <algorithm>
#include <iostream>
#include <cstring>

#define SIZE 1000000
#define UL unsigned long

using namespace std;

UL cache[SIZE];

int init(){
   memset(cache,0,sizeof(cache));
   return 0;
}

UL treeNplusOne(UL n){
   if((n % 2)==1)
      return 3*n+1;
   else
      return n/2;
}

UL circleLength(UL k){
   int length = 0;
   if(k == 1)
      return 1;
   if((k < SIZE) && cache[int(k)] != 0)
      return cache[k];
   length = 1 + circleLength(treeNplusOne(k));
   if(k < SIZE)
      cache[int(k)]=length;
   return length;
}


int main(){
   /*
   string line;
   while(getline(cin, line)){
      
   }
   */
   init();
   unsigned long a = 0;
   unsigned long b = 0;
   while(cin>>a>>b){
      UL _min = min(a,b);
      UL _max = max(a,b);
      UL clmax=1;
      int idx = 0;
      for(idx = _min;idx<=_max;idx++){
         clmax=(max(clmax,circleLength(idx)));
      }
      cout<<a<<" "<<b<<" "<<clmax<<endl;
   }
   return 0;
}
