#include<stdio.h>
#include<malloc.h>
struct node{
int data;
struct node *next;
};
void main(){
void sort(struct node *);
int num;
FILE *fp1=fopen("./in","rb");
FILE *fp2=fopen("./out","wb");
struct node *head=(struct node *)malloc(sizeof(struct node));
struct node *temp=NULL,*p=head;
head->data=0;
head->next=NULL;
while(fscanf(fp1,"%d",&num)!=EOF){
head->data++;
temp=(struct node *)malloc(sizeof(struct node));
temp->data=num;
temp->next=NULL;
p->next=temp;
p=temp;
}
p=head;
for(num=0;num<=head->data;num++,p=p->next)printf("%d\n",p->data);
sort(head);
p=head;
for(num=0;num<=head->data;num++,p=p->next)printf("%d\n",p->data);
p=head->next;
while(p!=NULL){
fprintf(fp2,"%d\n",p->data);
p=p->next;
}
fclose(fp1);
fclose(fp2);
}
void sort(struct node *head){
int num=head->data,i,temp;
struct node *p=head->next;
for(i=0;i<num;i++){
while(p->next!=NULL){
if(p->data>p->next->data){
temp=p->data;
p->data=p->next->data;
p->next->data=temp;
}
p=p->next;
}
p=head->next;
}
}
