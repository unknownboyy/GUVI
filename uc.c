#include<stdio.h>
int main(){
int n;
int t;
int space=0;

scanf("%d ",&n);
if(n%2==0);
else{
    for(int i=1;i<=n/2;++i){
        t=n-(i-1)*2;
    for(int j=0;j<t;++j){
        printf("*");
        space++;
    }
    space--;
    printf("\n");
    }
    for(int j=0;j<n;++j) {printf("*"); space++;}
    space--;
    printf("\n");
    for(int i=n/2;i>=1;--i){
        t=n-(i-1)*2;
    for(int j=0;j<t;++j){
        printf("*");
        space++;}
        space--;
    printf("\n");
    }


}
return 0;
}
