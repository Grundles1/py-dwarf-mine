all: hello

hello: hello.c
	gcc -g -o $@ $<

hello.dwarf.info: hello.dSYM
	gobjdump -Wi hello.dSYM/Contents/Resources/DWARF/hello > $@



%.o: %.c
	gcc -g -o $@ $<
%.dSYM: %.c
	gcc -g -o $@ $<
clean:
	-@rm hello *.o *.dSYM *.dump