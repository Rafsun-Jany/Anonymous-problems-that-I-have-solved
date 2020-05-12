#include<stdio.h>
int main()
{
    int a=10,b=20,count;
    count = countbits(a,b);
    printf("So the count is: %d",count);

}

int countbits(int a,int b)
{
    int count = 0;
    int last_bit_a,last_bit_b;

    while(a || b){
        last_bit_a = a&1;
        last_bit_b = b&1;
        if(last_bit_a != last_bit_b){
            count++;
        }
        a= a>>1;
        b= b>>1;

    }
    return count;
}
