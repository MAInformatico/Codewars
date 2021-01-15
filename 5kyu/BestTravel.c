#include <stdlib.h>
void combination(int *result, int t, int temp[], int k, int ls[], int szls, int begin, int index) {
	if(k==0){
	    int aux = 0;
	    for(int i=0;i<index;i++) {
		    aux+=temp[i];
	    }
	    if(*result<aux && aux<=t) *result=aux;
	}
	
	for(int i=begin;i<szls;i++) {
		temp[index]=ls[i];
		combination(result,t,temp,k-1,ls,szls,i+1,index+1);
	}
}

// szls: size of ls
int chooseBestSum(int t, int k, int ls[], int szls) {
    if (k>szls || k<=0) return -1;
    int result = -1;
    int *temp = (int*)calloc(szls,sizeof(int));
    combination(&result,t,temp,k,ls,szls,0,0);
    free(temp);
    temp=NULL;
    return result;
}
