#include<stdio.h>
int main()
{
    int row,integer,column,p;
    printf("Enter an integer: ");
    scanf("%d",&integer);
    for(row=1;row<=((2*integer)-1);row++){
        for(column=1;column<=((2*integer)-1);column++){
                if(column==row || column ==(2*integer-row)){
                    if(column<=integer){
                        printf("%d",(2*column-1));
                    }
                    else if(column>integer && row!=column){
                            p=2*row;
                        printf("%d",p);
                    }
                    else if(row==column){
                        printf("%d",p);
                        p=p-2;
                    }
                }
                else
                    printf(" ");
        }
        printf("\n");
    }
}
