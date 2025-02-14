cmake_minimum_required(VERSION 3.18)
# 1.create a Project
set(PROJECT_NAME "ACMSIMC")
PROJECT(${PROJECT_NAME})
# set(PROJECT_BINARY_DIR ${CMAKE_CURRENT_SOURCE_DIR}/build/bin)
# 2. add subdirectory and include directory
# add_subdirectory(dll)
# add_subdirectory(lib)
# include_directories(${PROJECT_SOURCE_DIR}/dll/inc)
# include_directories(${PROJECT_SOURCE_DIR}/lib/inc)
# include_directories(${PROJECT_SOURCE_DIR}/)
# 2. to get all source files
# aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/ ACMSIMC_src)
# aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/*.c ACMSIMC_src)
# aux_source_directory(${CMAKE_CURRENT_SOURCE_DIR}/*.h ACMSIMC_inc)
set(INC_DIR ${CMAKE_CURRENT_SOURCE_DIR})
set(SRC_DIR ${CMAKE_CURRENT_SOURCE_DIR})
file(GLOB ACMSIMC_src "${CMAKE_CURRENT_SOURCE_DIR}/*.c")
file(GLOB ACMSIMC_inc "${CMAKE_CURRENT_SOURCE_DIR}/*.h")

# 3. create a executable file
# add_executable(${PROJECT_NAME} ${ACMSIMC_src})
add_executable(${PROJECT_NAME} ${ACMSIMC_src} ${ACMSIMC_inc})
# 4. Set Project Properties

# SET_TARGET_PROPERTIES(${PROJECT_NAME} PROPERTIES
# 										RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR})
# # 4. Set Project Properties
# target_include_directories(${PROJECT_NAME} PUBLIC 
# 											${PROJECT_SOURCE_DIR}/dll/inc)
# target_link_libraries(${PROJECT_NAME} PUBLIC 
# 										C_001_dll)
# target_include_directories(${PROJECT_NAME} PUBLIC 
# 											${PROJECT_SOURCE_DIR}/lib/inc)
# target_link_libraries(${PROJECT_NAME} PUBLIC 
# 											C_001_lib)

# message(STATUS "PROJECT_SOURCE_DIR This is SOURCE dir " ${PROJECT_SOURCE_DIR})
# message(STATUS "CMAKE_CURRENT_SOURCE_DIR This is SOURCE dir " ${CMAKE_CURRENT_SOURCE_DIR})
# 5. link library, include directory
