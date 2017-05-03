CC=gcc
CFLAGS=-Wall

all: main

main: main.c list.c
	$(CC) $(CFLAGS) -o $@ $^

min: min.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -rf main
