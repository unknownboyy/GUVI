#include<stdio.h>
int g(int x){
if(x-1)
return 2*g(x-1) + x;
else
return 0;
}
int main(){

printf("%d",g(5));
}
