CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the Blender version string in multiple ones.
string(REPLACE "." ";" BLENDER_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET BLENDER_VERSION_LIST 0 BLENDER_VERSION_MAJOR)
list(GET BLENDER_VERSION_LIST 1 BLENDER_VERSION_MINOR)
list(GET BLENDER_VERSION_LIST 2 BLENDER_VERSION_PATCH)

# Blender
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    BLENDER_URL blender/blender-${REZ_BUILD_PROJECT_VERSION}-linux64.tar.xz
    https://www.blender.org/download/Blender${BLENDER_VERSION_MAJOR}.${BLENDER_VERSION_MINOR}/blender-${REZ_BUILD_PROJECT_VERSION}-linux64.tar.xz/
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/blender/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install Blender through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_BLENDER
    URL ${BLENDER_URL}
    PREFIX blender
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] Blender-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
