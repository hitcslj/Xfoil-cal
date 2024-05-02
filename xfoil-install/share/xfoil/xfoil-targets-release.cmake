#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "xfoil" for configuration "Release"
set_property(TARGET xfoil APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(xfoil PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/bin/xfoil-6.97"
  )

list(APPEND _IMPORT_CHECK_TARGETS xfoil )
list(APPEND _IMPORT_CHECK_FILES_FOR_xfoil "${_IMPORT_PREFIX}/bin/xfoil-6.97" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
