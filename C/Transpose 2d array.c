#include<stdio.h>
#define ROWS 100
#define COLUMNS 100
int main()
{
    int A[ROWS][COLUMNS], rows,columns,i,j,transpose[ROWS][COLUMNS];
    printf("Enter the number of rows and columns: ");
    scanf("%d %d",&rows,&columns);

    for(i=0;i<rows;i++){
        for(j=0;j<columns;j++){
            printf("Enter the elements in the matrix where row=%d and column=%d: ",i,j);
            scanf("%d",&A[i][j]);
        }
    }
    //printf("Enter the column number for which you want the summation: ");
    //scanf("%d",&n);

    for(i=0;i<rows;i++){
        for(j=0;j<columns;j++){
                transpose[j][i] = A[i][j];
        }
    }
    printf("\n\n");
    for(i=0;i<columns;i++){
        for(j=0;j<rows;j++){
            printf("The element in the matrix where row=%d and column=%d is: %d\n",i,j,transpose[i][j]);

        }
    }

}
