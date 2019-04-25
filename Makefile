DATASET_ROOT_PATH=/home/ubuntu/datasets/CD2014/
DATASET_PATH=$(DATASET_ROOT_PATH)/dataset
RESULTS_PATH=$(DATASET_ROOT_PATH)/results

COMPARATOR_SRC=cpp_code/Comparator.cpp \
			   cpp_code/mainComparator.cpp \
			   cpp_code/makefile \
			   cpp_code/Method.h  \
			   cpp_code/VideoFolder.cpp \
			   cpp_code/YourMethod.cpp \
			   cpp_code/Comparator.h \
			   cpp_code/main.cpp \
			   cpp_code/Method.cpp \
			   cpp_code/types.h \
			   cpp_code/VideoFolder.h \
			   cpp_code/YourMethod.h
OUTPUT=./exe/comparator

.PHONY: all run
all: $(OUTPUT)

run: $(OUTPUT)
	python3 processFolder.py  $(DATASET_PATH) $(RESULTS_PATH)


$(OUTPUT): $(COMPARATOR_SRC)
	make -C cpp_code comparator
	mv cpp_code/comparator exe/


