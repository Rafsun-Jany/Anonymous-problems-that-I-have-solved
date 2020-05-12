#include<stdio.h>

int main()
{
    int x,number;
    printf("Enter a number that you want to reverse: ");
    scanf("%d",&x);
    print_digits_reversed(x);
}

void print_digits_reversed(int x)
{
    static remainder,sum;
    if(x!=0){
        remainder = x%10 ;
        sum = sum*10 + remainder;
        //printf("%d",remainder);
        x = x/10;
        print_digits_reversed(x);

    }
    else
        printf("%d",sum);
}
