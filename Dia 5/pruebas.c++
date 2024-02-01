using namespace std;

int n,t,h,Max,Min;

int Coin[55];

int gcd(int a,int b)

{

    if(b==0)return a;

    else return gcd(b,a%b);

}

int lcm(int a,int b)

{

    return a/gcd(a,b)b;

}

void dfs(int H,int num,int cur)

{

    if(num==4)

    {

        int tmp=h/HH;

        if(tmp==h)

        {

            Max=Min=tmp;

        }

        else

        {

            if(Max==-1Max<tmp)

                Max=tmp;

            if(Min==-1Min>tmp+H)

                Min=tmp+H;

        }

        return;

    }

    if(cur==n)return;

    dfs(H,num,cur+1);

    int l;

    if(H==0)l=Coin[cur];

    else l=lcm(H,Coin[cur]);

    dfs(l,num+1,cur+1);

}

int main()

{

    while(cin>>n>>t)

    { 

        if(n==0&&t==0)break;

        for(int i=0;i<n;++i)

        {

            cin>>Coin[i];

        }

        for(int i=0;i<t;++i) 

        {

            cin>>h;

            Max=-1;Min=-1;

            dfs(0,0,0);

            cout<<Max<<" "<<Min<<endl;

        }

    }

    return 0;

}