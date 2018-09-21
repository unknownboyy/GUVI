#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int gcd(int a, int b) 
{  
    if (a == 0 || b == 0) 
       return 0;  
    if (a == b) 
        return a;
    if (a > b) 
        return gcd(a-b, b); 
    return gcd(a, b-a); 
} 
int main() {
int p,x,q,y;
cin>>p>>x>>q>>y;
int zz=gcd(p,q);
if(x==y) cout<<x;
else if(abs(x-y)%zz!=0){
  cout<<-1<<endl;
}else{
  long long int a[1000000]={0};
  for(long long int i=1;i<1000000;i++){
          long long int xx=x+(p*i);
          long long int yy=y+(q*i);
          if(a[xx]==1 || a[yy]==1){
            if(a[xx]==1)
            cout<<xx<<endl;
            else cout<<yy<<endl;
            break;
          }
          a[xx]++; a[yy]++;
  }
}

return 0;}