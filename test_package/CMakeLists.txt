project(winpcap-test CXX)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

file(GLOB ${CMAKE_CURRENT_SOURCE_DIR}/*.c)

add_executable(${CMAKE_PROJECT_NAME} ${SOURCE_FILES})
target_link_libraries(${CMAKE_PROJECT_NAME} ${CONAN_LIBS})

enable_testing()
add_test(NAME test-all
         WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
         COMMAND ${CMAKE_PROJECT_NAME})
