# cmake-dictionary

A dictionary of CMake words for CSpell

<https://cspell.org/docs/dictionaries/custom-dictionaries>

## Extraction Status

From <https://cmake.org/cmake/help/latest/>

Definition of done — I have extracted CMake words from the documentation to see what is not covered by the en_us dictionary.

### Command-Line Tools

- [x] [cmake(1)](https://cmake.org/cmake/help/latest/manual/cmake.1.html)
- [x] [ctest(1)](https://cmake.org/cmake/help/latest/manual/ctest.1.html)
- [x] [cpack(1)](https://cmake.org/cmake/help/latest/manual/cpack.1.html)

### Interactive Dialogs

- [x] [cmake-gui(1)](https://cmake.org/cmake/help/latest/manual/cmake-gui.1.html)
- [x] [ccmake(1)](https://cmake.org/cmake/help/latest/manual/ccmake.1.html)

### Reference Manuals

- [x] [cmake-buildsystem(7)](https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html)
- [x] [cmake-commands(7)](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html)
  - [ ] add_compile_definitions
  - [ ] add_compile_options
  - [ ] add_custom_command
  - [ ] add_custom_target
  - [ ] add_definitions
  - [ ] add_dependencies
  - [ ] add_executable
  - [ ] add_library
  - [ ] add_link_options
  - [ ] add_subdirectory
  - [ ] add_test
  - [ ] aux_source_directory
  - [ ] block
  - [ ] break
  - [ ] build_command
  - [ ] cmake_diagnostic
  - [ ] cmake_file_api
  - [ ] cmake_host_system_information
  - [ ] cmake_instrumentation
  - [ ] cmake_language
  - [ ] cmake_minimum_required
  - [ ] cmake_parse_arguments
  - [ ] cmake_path
  - [ ] cmake_pkg_config
  - [ ] cmake_policy
  - [ ] configure_file
  - [ ] continue
  - [ ] create_test_sourcelist
  - [ ] ctest_build
  - [ ] ctest_configure
  - [ ] ctest_coverage
  - [ ] ctest_empty_binary_directory
  - [ ] ctest_memcheck
  - [ ] ctest_read_custom_files
  - [ ] ctest_run_script
  - [ ] ctest_sleep
  - [ ] ctest_start
  - [ ] ctest_submit
  - [ ] ctest_test
  - [ ] ctest_update
  - [ ] ctest_upload
  - [ ] define_property
  - [ ] discover_tests
  - [ ] else
  - [ ] elseif
  - [ ] enable_language
  - [ ] enable_testing
  - [ ] endblock
  - [ ] endforeach
  - [ ] endfunction
  - [ ] endif
  - [ ] endmacro
  - [ ] endwhile
  - [ ] execute_process
  - [ ] export
  - [ ] file
  - [ ] find_file
  - [ ] find_library
  - [ ] find_package
  - [ ] find_path
  - [ ] find_program
  - [ ] fltk_wrap_ui
  - [ ] foreach
  - [ ] function
  - [ ] get_cmake_property
  - [ ] get_directory_property
  - [ ] get_filename_component
  - [ ] get_property
  - [ ] get_source_file_property
  - [ ] get_target_property
  - [ ] get_test_property
  - [ ] if
  - [ ] include
  - [ ] include_directories
  - [ ] include_external_msproject
  - [ ] include_guard
  - [ ] include_regular_expression
  - [ ] install
  - [ ] link_directories
  - [ ] link_libraries
  - [ ] list
  - [ ] load_cache
  - [ ] macro
  - [ ] mark_as_advanced
  - [ ] math
  - [ ] message
  - [ ] option
  - [ ] project
  - [ ] remove_definitions
  - [ ] return
  - [ ] separate_arguments
  - [ ] set
  - [ ] set_directory_properties
  - [ ] set_property
  - [ ] set_source_files_properties
  - [ ] set_target_properties
  - [ ] set_tests_properties
  - [ ] site_name
  - [ ] source_group
  - [ ] string
  - [ ] target_compile_definitions
  - [ ] target_compile_features
  - [ ] target_compile_options
  - [ ] target_include_directories
  - [ ] target_link_directories
  - [ ] target_link_libraries
  - [ ] target_link_options
  - [ ] target_precompile_headers
  - [ ] target_sources
  - [ ] try_compile
  - [ ] try_run
  - [ ] unset
  - [ ] variable_watch
  - [ ] while
  - [ ] build_name (deprecated command)
  - [ ] exec_program (deprecated command)
  - [ ] export_library_dependencies (deprecated command)
  - [ ] install_files (deprecated command)
  - [ ] install_programs (deprecated command)
  - [ ] install_targets (deprecated command)
  - [ ] load_command (deprecated command)
  - [ ] make_directory (deprecated command)
  - [ ] output_required_files (deprecated command)
  - [ ] qt_wrap_cpp (deprecated command)
  - [ ] qt_wrap_ui (deprecated command)
  - [ ] remove (deprecated command)
  - [ ] subdir_depends (deprecated command)
  - [ ] subdirs (deprecated command)
  - [ ] use_mangled_mesa (deprecated command)
  - [ ] utility_source (deprecated command)
  - [ ] variable_requires (deprecated command)
  - [ ] write_file (deprecated command)
- [x] [cmake-compile-features(7)](https://cmake.org/cmake/help/latest/manual/cmake-compile-features.7.html)
- [x] [cmake-configure-log(7)](https://cmake.org/cmake/help/latest/manual/cmake-configure-log.7.html)
- [x] [cmake-cxxmodules(7)](https://cmake.org/cmake/help/latest/manual/cmake-cxxmodules.7.html)
- [x] [cmake-developer(7)](https://cmake.org/cmake/help/latest/manual/cmake-developer.7.html)
- [x] [cmake-diagnostics(7)](https://cmake.org/cmake/help/latest/manual/cmake-diagnostics.7.html)
- [x] [cmake-env-variables(7)](https://cmake.org/cmake/help/latest/manual/cmake-env-variables.7.html)
  - [ ] Check all environment variables for keyword values
- [x] [cmake-file-api(7)](https://cmake.org/cmake/help/latest/manual/cmake-file-api.7.html)
- [ ] [cmake-generator-expressions(7)](https://cmake.org/cmake/help/latest/manual/cmake-generator-expressions.7.html)
- [x] [cmake-generators(7)](https://cmake.org/cmake/help/latest/manual/cmake-generators.7.html)
- [ ] [cmake-instrumentation(7)](https://cmake.org/cmake/help/latest/manual/cmake-instrumentation.7.html)
- [x] [cmake-language(7)](https://cmake.org/cmake/help/latest/manual/cmake-language.7.html)
- [x] [cmake-modules(7)](https://cmake.org/cmake/help/latest/manual/cmake-modules.7.html)
  - [ ] Check all modules for variables, commands, and targets.
- [x] [cmake-packages(7)](https://cmake.org/cmake/help/latest/manual/cmake-packages.7.html)
- [x] [cmake-policies(7)](https://cmake.org/cmake/help/latest/manual/cmake-policies.7.html)
- [ ] [cmake-presets(7)](https://cmake.org/cmake/help/latest/manual/cmake-presets.7.html)
- [x] [cmake-properties(7)](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html)
  - [ ] Check all properties for keyword values
- [x] [cmake-qt(7)](https://cmake.org/cmake/help/latest/manual/cmake-qt.7.html)
- [x] [cmake-server(7)](https://cmake.org/cmake/help/latest/manual/cmake-server.7.html)
- [x] [cmake-toolchains(7)](https://cmake.org/cmake/help/latest/manual/cmake-toolchains.7.html)
- [x] [cmake-variables(7)](https://cmake.org/cmake/help/latest/manual/cmake-variables.7.html)
  - [ ] Check all variables for keyword values
- [x] [cpack-generators(7)](https://cmake.org/cmake/help/latest/manual/cpack-generators.7.html)
  - [ ] CPack AppImage Generator
  - [ ] CPack Archive Generator
  - [ ] CPack Bundle Generator
  - [ ] CPack Cygwin Generator
  - [ ] CPack DEB Generator
  - [ ] CPack DragNDrop Generator
  - [ ] CPack External Generator
  - [ ] CPack FreeBSD Generator
  - [ ] CPack Inno Setup Generator
  - [ ] CPack IFW Generator
  - [ ] CPack NSIS Generator
  - [ ] CPack NuGet Generator
  - [ ] CPack PackageMaker Generator
  - [ ] CPack productbuild Generator
  - [ ] CPack RPM Generator
  - [ ] CPack WIX Generator

### Guides

- CMake Tutorial
- User Interaction Guide
- Using Dependencies Guide
- Importing and Exporting Guide
- IDE Integration Guide

### Release Notes

- CMake Release Notes
