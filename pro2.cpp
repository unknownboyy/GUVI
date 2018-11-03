#include<iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    int t;
    cin>>t;
    int arr[100000];
    while(t--){
        int n;
        cin>>n;
        for(int i = 0; i < n; i++)
        {
            cin>>arr[i];
        }
        int min=1000000;
        int min_index=0;
        for(int i = 0; i < n; i++)
        {
            if(arr[i]<min) { min=arr[i]; min_index=i; }
        }
        int times=0;
        for(int i = 0; i < n-1; i++)
        {
            if(arr[i]>arr[i+1]){
                times++;
            }
        }
        if(times<=1) cout<<"YES"<<endl;
        else cout<<"NO"<<endl;
        
    }
    return 0;
}
