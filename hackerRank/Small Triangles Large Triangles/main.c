#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

struct boxRef
{
    triangle tr;
    double area;
};

typedef struct boxRef boxRef;

void insert_sort(boxRef *arr, int n){
    int i = 0;
    int j = 0;
    int tmp = 0;
    for(i=0;i<n;i++){
        j = i;
        while(j>0 && arr[j-1].area>arr[j].area){
            boxRef tmp = arr[j-1];
            arr[j-1] = arr[j];
            arr[j] = tmp;
            j--;            
        }
    }
}

void sort_by_area(triangle* tr, int n) {
	/**
	* Sort an array a of the length n
	*/
    int i = 0;
    boxRef *ordering = (boxRef *)malloc(sizeof(boxRef)*n);
    for(i = 0;i<n;i++){
        double p = ((double)tr[i].a+(double)tr[i].b+(double)tr[i].c)/2;
        ordering[i].area = sqrt(p*(p-tr[i].a)*(p-tr[i].b)*(p-tr[i].c));
        ordering[i].tr = tr[i];
    }    
    insert_sort(ordering,n);
    i = 0;
    for(i = 0;i<n;i++){
        tr[i] = ordering[i].tr;
    }
    free(ordering);
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = (triangle *)malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
