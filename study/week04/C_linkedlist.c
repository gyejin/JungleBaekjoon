#include <stdio.h>
#include <stdlib.h>

struct node
{
    char str[30];
    struct node *next;
};

typedef struct node node;
node *head, *tail;

void make_node(char *tar);
void search();

int main(void)
{
    make_node("수서"); make_node("복정"); make_node("태평"); make_node("모란");
    search();
}

void make_node(char *tar)
{
    node *_new = (node *)malloc(sizeof(node));
    memset(_new, 0, sizeof(node));
    strcpy(_new->str, tar);
    if(tail!=NULL)
    {
        tail->next = _new;
        tail = _new;
    }
    else
    {
        head = tail = _new;
    }
}

void search()
{
    node *cur = head;
    for(;cur!=NULL;cur=cur->next)
        printf("%s\n",cur->str);
}