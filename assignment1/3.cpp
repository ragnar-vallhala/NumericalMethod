#include<iostream>
using namespace std;

int main(){
    int n;
    cin>>n;
    float arr[n][n];
    float ans[n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>arr[i][j];
        }
    }
    float b[n];
    for(int i=0;i<n;i++){
        cin>>b[i];
    }

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

    cout<<endl<<endl;

    for(int i=0;i<n;i++){
        cout<<b[i]<<" ";
    }

    cout<<endl<<endl;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}