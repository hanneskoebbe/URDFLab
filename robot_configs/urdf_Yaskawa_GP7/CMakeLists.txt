cmake_minimum_required(VERSION 3.5)
project(urdf_Yaskawa_GP7)


find_package(ament_cmake REQUIRED)


install(DIRECTORY "urdf" "meshes"
    DESTINATION share/${PROJECT_NAME}
)


ament_package()