PROJECT(MYTH)
ADD_SUBDIRECTORY(src/public lib)
AUX_SOURCE_DIRECTORY(. DIR_SRC)
ADD_EXECUTABLE(main ${DIR_SRC})
TARGET_LINK_LIBRARIES(main MTHREAD)
