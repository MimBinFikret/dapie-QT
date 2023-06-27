TARGET = dapie
PYTHON_SCRIPT = dapie.py
PYINSTALLER_CMD = pyinstaller
PYINSTALLER_FLAGS = --onefile --noconsole --distpath "." --name=$(TARGET)

all: $(TARGET)

$(TARGET):
	pip3 install -r requirements.txt
	$(PYINSTALLER_CMD) $(PYINSTALLER_FLAGS) $(PYTHON_SCRIPT)

run:
	pip3 install -r requirements.txt
	python3 $(PYTHON_SCRIPT)

runX:
	./dapie

clean:
	rm -rf build/ $(TARGET).spec dapie .swl .swm

.PHONY: clean run
