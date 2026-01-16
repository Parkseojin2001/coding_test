#pragma warning(disable:4996)

#include<stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
	struct Node* next;
	struct Node* prev;
	char ch;
}node;

node*head;
node* tail;

node* order_L(node* q);
node* order_D(node* q);
node* order_B(node* q);
node* order_P(node* q, char c);
void freeNode(node* p);

int main() {
	int M, L;
	char str[100001] = { 0 }, order, ch;
	node* p = NULL;
	head = (node*)malloc(sizeof(node));
	tail = (node*)malloc(sizeof(node));
	head->next = tail;
	tail->prev = head;
	head->prev = NULL;
	tail->next = NULL;
	p = tail;
	scanf("%s", str);
	L = strlen(str);
	for (int i = 0; i < L; i++) {
		p = order_P(p, str[i]);
	}
	scanf("%d", &M);
	for (int i = 0; i < M; i++) {
		getchar();
		scanf("%c", &order);
		if (order == 'L') {
			p = order_L(p);
		}
		else if (order == 'D') {
			p = order_D(p);
		}
		else if (order == 'B') {
			p = order_B(p);
		}
		else {
			getchar();
			scanf("%c", &ch);
			p = order_P(p, ch);
		}
	}
	p = head->next;
	while (p != tail) {
		printf("%c", p->ch);
		p = p->next;
	}
	p = head->next;
	freeNode(p);
	free(head);
	free(tail);
	return 0;
}

node* order_L(node* q) {
	node* temp;
	if (q == head->next) {
		return q;
	}
	else {
		temp = q->prev;
		return temp;
	}
}
node* order_D(node* q) {
	node* temp;
	if (q == tail) {
		return q;
	}
	else {
		temp = q->next;
		return temp;
	}
}
node* order_B(node* q) {
	node* temp;
	if (q == head->next) {
		return q;
	}
	else {
		temp = q->prev;
		temp->prev->next = temp->next;
		temp->next->prev = temp->prev;
		free(temp);
		return q;
	}
}
node* order_P(node* q, char c) {
	node* p;
	p = (node*)malloc(sizeof(node));
	p->ch = c;
	p->prev = q->prev;
	p->next = q;
	q->prev->next = p;
	q->prev = p;
	return q;
}
void freeNode(node* p) {
    node *temp = p;
	while (temp != tail) {
        p = p->next;
        free(temp);
        temp = p;
	}
}