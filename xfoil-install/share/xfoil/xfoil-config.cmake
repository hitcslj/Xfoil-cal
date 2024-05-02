#############################################################################
#
#  XFOIL
#
#  Copyright (C) 2000 Mark Drela
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#############################################################################


####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was xfoil-config.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../" ABSOLUTE)

####################################################################################

set(XFOIL_VERSION_MAJOR "6")
set(XFOIL_VERSION_MINOR "97")
set(XFOIL_VERSION "6.97")

set(XFOIL_FOUND TRUE)
set(XFOIL_EXECUTABLE "${PACKAGE_PREFIX_DIR}/bin/xfoil-6.97")

include("${CMAKE_CURRENT_LIST_DIR}/xfoil-targets.cmake")
