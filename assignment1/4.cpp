#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    float arr[n][n];
    float b[n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
    }
    for(int i=0;i<n;i++){
        cin>>b[i];
    }
    float fact;
    for(int k=0;k<n;k++){
        for(int i=k+1;i<n;i++){
            fact=arr[i][k]/arr[k][k];
            for(int j=k;j<n;j++){
                arr[i][j]=arr[i][j]-fact*arr[k][j];
            }
            b[i]=b[i]-fact*b[k];
        }
    }

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(abs(arr[i][j])<=1.0/10000000.0){
                arr[i][j]=0;
            }
        }
    }
    
    //solving part

    for(int i=0;i<n;i++){
        b[i]=b[i]/arr[i][i];
    }

    float d[n];
    for(int i=0;i<n;i++){
        d[i]=arr[i][i];
    }

    for(int i=0;i<n;i++){
        for(int j=i;j<n;j++){
            arr[i][j]=arr[i][j]/d[i];
        }
    }

    float ans[n];
    ans[n-1]=b[n-1]/arr[n-1][n-1];
    for(int i=n-2;i>=0;i--){
        float sum=0;
        for(int j=i+1;j<n;j++){
            sum=sum+arr[i][j]*ans[j];
        }
        ans[i]=b[i]-sum/arr[i][i];
    }
    cout<<endl;
    cout<<"roots are: ";
    for(int i=0;i<n;i++){
        cout<<ans[i]<<" ";
    }

    return 0;
}