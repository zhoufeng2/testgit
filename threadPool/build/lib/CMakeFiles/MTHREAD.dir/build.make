# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/zhoufeng2/threadPool

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/zhoufeng2/threadPool/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/MTHREAD.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/MTHREAD.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/MTHREAD.dir/flags.make

lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o: lib/CMakeFiles/MTHREAD.dir/flags.make
lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o: ../src/CDefaultRunnable.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/zhoufeng2/threadPool/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o -c /home/zhoufeng2/threadPool/src/CDefaultRunnable.cpp

lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.i"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/zhoufeng2/threadPool/src/CDefaultRunnable.cpp > CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.i

lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.s"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/zhoufeng2/threadPool/src/CDefaultRunnable.cpp -o CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.s

lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.requires:
.PHONY : lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.requires

lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.provides: lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.requires
	$(MAKE) -f lib/CMakeFiles/MTHREAD.dir/build.make lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.provides.build
.PHONY : lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.provides

lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.provides.build: lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o

lib/CMakeFiles/MTHREAD.dir/__/CThread.o: lib/CMakeFiles/MTHREAD.dir/flags.make
lib/CMakeFiles/MTHREAD.dir/__/CThread.o: ../src/CThread.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/zhoufeng2/threadPool/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/MTHREAD.dir/__/CThread.o"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/MTHREAD.dir/__/CThread.o -c /home/zhoufeng2/threadPool/src/CThread.cpp

lib/CMakeFiles/MTHREAD.dir/__/CThread.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MTHREAD.dir/__/CThread.i"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/zhoufeng2/threadPool/src/CThread.cpp > CMakeFiles/MTHREAD.dir/__/CThread.i

lib/CMakeFiles/MTHREAD.dir/__/CThread.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MTHREAD.dir/__/CThread.s"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/zhoufeng2/threadPool/src/CThread.cpp -o CMakeFiles/MTHREAD.dir/__/CThread.s

lib/CMakeFiles/MTHREAD.dir/__/CThread.o.requires:
.PHONY : lib/CMakeFiles/MTHREAD.dir/__/CThread.o.requires

lib/CMakeFiles/MTHREAD.dir/__/CThread.o.provides: lib/CMakeFiles/MTHREAD.dir/__/CThread.o.requires
	$(MAKE) -f lib/CMakeFiles/MTHREAD.dir/build.make lib/CMakeFiles/MTHREAD.dir/__/CThread.o.provides.build
.PHONY : lib/CMakeFiles/MTHREAD.dir/__/CThread.o.provides

lib/CMakeFiles/MTHREAD.dir/__/CThread.o.provides.build: lib/CMakeFiles/MTHREAD.dir/__/CThread.o

lib/CMakeFiles/MTHREAD.dir/__/MyThread.o: lib/CMakeFiles/MTHREAD.dir/flags.make
lib/CMakeFiles/MTHREAD.dir/__/MyThread.o: ../src/MyThread.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /home/zhoufeng2/threadPool/build/CMakeFiles $(CMAKE_PROGRESS_3)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/MTHREAD.dir/__/MyThread.o"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/MTHREAD.dir/__/MyThread.o -c /home/zhoufeng2/threadPool/src/MyThread.cpp

lib/CMakeFiles/MTHREAD.dir/__/MyThread.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/MTHREAD.dir/__/MyThread.i"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/zhoufeng2/threadPool/src/MyThread.cpp > CMakeFiles/MTHREAD.dir/__/MyThread.i

lib/CMakeFiles/MTHREAD.dir/__/MyThread.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/MTHREAD.dir/__/MyThread.s"
	cd /home/zhoufeng2/threadPool/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/zhoufeng2/threadPool/src/MyThread.cpp -o CMakeFiles/MTHREAD.dir/__/MyThread.s

lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.requires:
.PHONY : lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.requires

lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.provides: lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.requires
	$(MAKE) -f lib/CMakeFiles/MTHREAD.dir/build.make lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.provides.build
.PHONY : lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.provides

lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.provides.build: lib/CMakeFiles/MTHREAD.dir/__/MyThread.o

# Object files for target MTHREAD
MTHREAD_OBJECTS = \
"CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o" \
"CMakeFiles/MTHREAD.dir/__/CThread.o" \
"CMakeFiles/MTHREAD.dir/__/MyThread.o"

# External object files for target MTHREAD
MTHREAD_EXTERNAL_OBJECTS =

lib/libMTHREAD.a: lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o
lib/libMTHREAD.a: lib/CMakeFiles/MTHREAD.dir/__/CThread.o
lib/libMTHREAD.a: lib/CMakeFiles/MTHREAD.dir/__/MyThread.o
lib/libMTHREAD.a: lib/CMakeFiles/MTHREAD.dir/build.make
lib/libMTHREAD.a: lib/CMakeFiles/MTHREAD.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX static library libMTHREAD.a"
	cd /home/zhoufeng2/threadPool/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/MTHREAD.dir/cmake_clean_target.cmake
	cd /home/zhoufeng2/threadPool/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/MTHREAD.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/MTHREAD.dir/build: lib/libMTHREAD.a
.PHONY : lib/CMakeFiles/MTHREAD.dir/build

lib/CMakeFiles/MTHREAD.dir/requires: lib/CMakeFiles/MTHREAD.dir/__/CDefaultRunnable.o.requires
lib/CMakeFiles/MTHREAD.dir/requires: lib/CMakeFiles/MTHREAD.dir/__/CThread.o.requires
lib/CMakeFiles/MTHREAD.dir/requires: lib/CMakeFiles/MTHREAD.dir/__/MyThread.o.requires
.PHONY : lib/CMakeFiles/MTHREAD.dir/requires

lib/CMakeFiles/MTHREAD.dir/clean:
	cd /home/zhoufeng2/threadPool/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/MTHREAD.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/MTHREAD.dir/clean

lib/CMakeFiles/MTHREAD.dir/depend:
	cd /home/zhoufeng2/threadPool/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/zhoufeng2/threadPool /home/zhoufeng2/threadPool/src/public /home/zhoufeng2/threadPool/build /home/zhoufeng2/threadPool/build/lib /home/zhoufeng2/threadPool/build/lib/CMakeFiles/MTHREAD.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/MTHREAD.dir/depend

