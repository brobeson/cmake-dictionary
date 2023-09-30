# cmake-dictionary

A dictionary of CMake words for CSpell

<https://cspell.org/docs/dictionaries-custom/>

## Corner Cases

- [ ] Compiler arguments:
  - [ ] `-DSOME_MACRO`: preprocessor definitions
  - [ ] `-Werror`: warnings
  - [ ] `-fsanitizer`: other features
  - These need to be case sensitive.

## Manual Sections

CMake vocabulary pulled from these section of the reference documentation.
Include words not part of the CMake language to account for things like user documentation (example terminal commands), and JSON files like presets.

- [x] cmake(1)
- [x] ctest(1)
- [x] cpack(1)
- [x] cmake-gui(1)
- [x] ccmake(1)
- [ ] cmake-buildsystem(7)
- [x] cmake-commands(7)
  - [x] add_compile_definitions
  - [x] add_compile_options
  - [x] add_custom_command
  - [x] add_custom_target
  - [x] add_definitions
  - [x] add_dependencies
  - [x] add_executable
  - [x] add_library
  - [x] add_link_options
  - [x] add_subdirectory
  - [x] add_test
  - [x] aux_source_directory
  - [x] block
  - [x] break
  - [x] build_command
  - [x] cmake_file_api
  - [x] cmake_host_system_information
  - [x] cmake_language
  - [x] cmake_minimum_required
  - [x] cmake_parse_arguments
  - [x] cmake_path
  - [x] cmake_policy
  - [x] configure_file
  - [x] continue
  - [x] create_test_sourcelist
  - [x] ctest_build
  - [x] ctest_configure
  - [x] ctest_coverage
  - [x] ctest_empty_binary_directory
  - [x] ctest_memcheck
  - [x] ctest_read_custom_files
  - [x] ctest_run_script
  - [x] ctest_sleep
  - [x] ctest_start
  - [x] ctest_submit
  - [x] ctest_test
  - [x] ctest_update
  - [x] ctest_upload
  - [x] define_property
  - [x] else
  - [x] elseif
  - [x] enable_language
  - [x] enable_testing
  - [x] endblock
  - [x] endforeach
  - [x] endfunction
  - [x] endif
  - [x] endmacro
  - [x] endwhile
  - [x] execute_process
  - [x] export
  - [x] file
  - [x] find_file
  - [x] find_library
  - [x] find_package
  - [x] find_path
  - [x] find_program
  - [x] fltk_wrap_ui
  - [x] foreach
  - [x] function
  - [x] get_cmake_property
  - [x] get_directory_property
  - [x] get_filename_component
  - [x] get_property
  - [x] get_source_file_property
  - [x] get_target_property
  - [x] get_test_property
  - [x] if
  - [x] include
  - [x] include_directories
  - [x] include_external_msproject
  - [x] include_guard
  - [x] include_regular_expression
  - [x] install
  - [x] link_directories
  - [x] link_libraries
  - [x] list
  - [x] load_cache
  - [x] macro
  - [x] mark_as_advanced
  - [x] math
  - [x] message
  - [x] option
  - [x] project
  - [x] remove_definitions
  - [x] return
  - [x] separate_arguments
  - [x] set
  - [x] set_directory_properties
  - [x] set_property
  - [x] set_source_files_properties
  - [x] set_target_properties
  - [x] set_tests_properties
  - [x] site_name
  - [x] source_group
  - [x] string
  - [x] target_compile_definitions
  - [x] target_compile_features
  - [x] target_compile_options
  - [x] target_include_directories
  - [x] target_link_directories
  - [x] target_link_libraries
  - [x] target_link_options
  - [x] target_precompile_headers
  - [x] target_sources
  - [x] try_compile
  - [x] try_run
  - [x] unset
  - [x] variable_watch
  - [x] while
- [x] cmake-compile-features(7)
- [x] cmake-configure-log(7)
- [x] cmake-developer(7)
- [x] cmake-env-variables(7)
- [ ] cmake-file-api(7)
- [x] cmake-generator-expressions(7)
- [x] cmake-generators(7)
- [x] cmake-language(7)
- [ ] cmake-modules(7)
  - [ ] AndroidTestUtilities
  - [ ] BundleUtilities
  - [ ] CheckCCompilerFlag
  - [ ] CheckCompilerFlag
  - [ ] CheckCSourceCompiles
  - [ ] CheckCSourceRuns
  - [ ] CheckCXXCompilerFlag
  - [ ] CheckCXXSourceCompiles
  - [ ] CheckCXXSourceRuns
  - [ ] CheckCXXSymbolExists
  - [ ] CheckFortranCompilerFlag
  - [ ] CheckFortranFunctionExists
  - [ ] CheckFortranSourceCompiles
  - [ ] CheckFortranSourceRuns
  - [ ] CheckFunctionExists
  - [ ] CheckIncludeFileCXX
  - [ ] CheckIncludeFile
  - [ ] CheckIncludeFiles
  - [ ] CheckIPOSupported
  - [ ] CheckLanguage
  - [ ] CheckLibraryExists
  - [ ] CheckLinkerFlag
  - [ ] CheckOBJCCompilerFlag
  - [ ] CheckOBJCSourceCompiles
  - [ ] CheckOBJCSourceRuns
  - [ ] CheckOBJCXXCompilerFlag
  - [ ] CheckOBJCXXSourceCompiles
  - [ ] CheckOBJCXXSourceRuns
  - [ ] CheckPIESupported
  - [ ] CheckPrototypeDefinition
  - [ ] CheckSourceCompiles
  - [ ] CheckSourceRuns
  - [ ] CheckStructHasMember
  - [ ] CheckSymbolExists
  - [ ] CheckTypeSize
  - [ ] CheckVariableExists
  - [ ] CMakeAddFortranSubdirectory
  - [ ] CMakeBackwardCompatibilityCXX
  - [ ] CMakeDependentOption
  - [ ] CMakeFindDependencyMacro
  - [ ] CMakeFindFrameworks
  - [ ] CMakeFindPackageMode
  - [ ] CMakeGraphVizOptions
  - [ ] CMakePackageConfigHelpers
  - [ ] CMakePrintHelpers
  - [ ] CMakePrintSystemInformation
  - [ ] CMakePushCheckState
  - [ ] CMakeVerifyManifest
  - [ ] CPack
  - [ ] CPackComponent
  - [ ] CPackIFW
  - [ ] CPackIFWConfigureFile
  - [ ] CSharpUtilities
  - [ ] CTest
  - [ ] CTestCoverageCollectGCOV
  - [ ] CTestScriptMode
  - [ ] CTestUseLaunchers
  - [ ] Dart
  - [ ] DeployQt4
  - [ ] ExternalData
  - [ ] ExternalProject
  - [ ] FeatureSummary
  - [ ] FetchContent
  - [ ] FindPackageHandleStandardArgs
  - [ ] FindPackageMessage
  - [ ] FortranCInterface
  - [ ] GenerateExportHeader
  - [ ] GetPrerequisites
  - [ ] GNUInstallDirs
  - [ ] GoogleTest
  - [ ] InstallRequiredSystemLibraries
  - [ ] ProcessorCount
  - [ ] SelectLibraryConfigurations
  - [ ] SquishTestScript
  - [ ] TestBigEndian
  - [ ] TestForANSIForScope
  - [ ] TestForANSIStreamHeaders
  - [ ] TestForSSTREAM
  - [ ] TestForSTDNamespace
  - [ ] UseEcos
  - [ ] UseJava
  - [ ] UseSWIG
  - [ ] UsewxWidgets
  - [ ] FindALSA
  - [ ] FindArmadillo
  - [ ] FindASPELL
  - [ ] FindAVIFile
  - [ ] FindBacktrace
  - [ ] FindBISON
  - [ ] FindBLAS
  - [ ] FindBoost
  - [ ] FindBullet
  - [ ] FindBZip2
  - [ ] FindCABLE
  - [ ] FindCoin3D
  - [ ] FindCUDAToolkit
  - [ ] FindCups
  - [ ] FindCURL
  - [ ] FindCurses
  - [ ] FindCVS
  - [ ] FindCxxTest
  - [ ] FindCygwin
  - [ ] FindDart
  - [ ] FindDCMTK
  - [ ] FindDevIL
  - [ ] FindDoxygen
  - [ ] FindEnvModules
  - [ ] FindEXPAT
  - [ ] FindFLEX
  - [ ] FindFLTK
  - [ ] FindFLTK2
  - [ ] FindFontconfig
  - [ ] FindFreetype
  - [ ] FindGCCXML
  - [ ] FindGDAL
  - [ ] FindGettext
  - [ ] FindGIF
  - [ ] FindGit
  - [ ] FindGLEW
  - [ ] FindGLUT
  - [ ] FindGnuplot
  - [ ] FindGnuTLS
  - [ ] FindGSL
  - [ ] FindGTest
  - [ ] FindGTK
  - [ ] FindGTK2
  - [ ] FindHDF5
  - [ ] FindHg
  - [ ] FindHSPELL
  - [ ] FindHTMLHelp
  - [ ] FindIce
  - [ ] FindIconv
  - [ ] FindIcotool
  - [ ] FindICU
  - [ ] FindImageMagick
  - [ ] FindIntl
  - [ ] FindJasper
  - [ ] FindJava
  - [ ] FindJNI
  - [ ] FindJPEG
  - [ ] FindKDE3
  - [ ] FindKDE4
  - [ ] FindLAPACK
  - [ ] FindLATEX
  - [ ] FindLibArchive
  - [ ] FindLibinput
  - [ ] FindLibLZMA
  - [ ] FindLibXml2
  - [ ] FindLibXslt
  - [ ] FindLTTngUST
  - [ ] FindLua
  - [ ] FindLua50
  - [ ] FindLua51
  - [ ] FindMatlab
  - [ ] FindMFC
  - [ ] FindMotif
  - [ ] FindMPEG
  - [ ] FindMPEG2
  - [ ] FindMPI
  - [ ] FindMsys
  - [ ] FindODBC
  - [ ] FindOpenACC
  - [ ] FindOpenAL
  - [ ] FindOpenCL
  - [ ] FindOpenGL
  - [ ] FindOpenMP
  - [ ] FindOpenSceneGraph
  - [ ] FindOpenSP
  - [ ] FindOpenSSL
  - [ ] FindOpenThreads
  - [ ] Findosg
  - [ ] Findosg_functions
  - [ ] FindosgAnimation
  - [ ] FindosgDB
  - [ ] FindosgFX
  - [ ] FindosgGA
  - [ ] FindosgIntrospection
  - [ ] FindosgManipulator
  - [ ] FindosgParticle
  - [ ] FindosgPresentation
  - [ ] FindosgProducer
  - [ ] FindosgQt
  - [ ] FindosgShadow
  - [ ] FindosgSim
  - [ ] FindosgTerrain
  - [ ] FindosgText
  - [ ] FindosgUtil
  - [ ] FindosgViewer
  - [ ] FindosgVolume
  - [ ] FindosgWidget
  - [ ] FindPatch
  - [ ] FindPerl
  - [ ] FindPerlLibs
  - [ ] FindPHP4
  - [ ] FindPhysFS
  - [ ] FindPike
  - [ ] FindPkgConfig
  - [ ] FindPNG
  - [ ] FindPostgreSQL
  - [ ] FindProducer
  - [ ] FindProtobuf
  - [ ] FindPython
  - [ ] FindPython2
  - [ ] FindPython3
  - [ ] FindQt3
  - [ ] FindQt4
  - [ ] FindQuickTime
  - [ ] FindRTI
  - [ ] FindRuby
  - [ ] FindSDL
  - [ ] FindSDL_image
  - [ ] FindSDL_gfx
  - [ ] FindSDL_mixer
  - [ ] FindSDL_net
  - [ ] FindSDL_sound
  - [ ] FindSDL_ttf
  - [ ] FindSelfPackers
  - [ ] FindSquish
  - [ ] FindSQLite3
  - [ ] FindSubversion
  - [ ] FindSWIG
  - [ ] FindTCL
  - [ ] FindTclsh
  - [ ] FindTclStub
  - [ ] FindThreads
  - [ ] FindTIFF
  - [ ] FindVulkan
  - [ ] FindWget
  - [ ] FindWish
  - [ ] FindwxWidgets
  - [ ] FindX11
  - [ ] FindXalanC
  - [ ] FindXCTest
  - [ ] FindXercesC
  - [ ] FindXMLRPC
  - [ ] FindZLIB
- [x] cmake-packages(7)
- [x] cmake-policies(7)
- [x] cmake-presets(7)
- [x] cmake-properties(7)
- [ ] cmake-qt(7)
- [ ] cmake-server(7)
- [ ] cmake-toolchains(7)
- [x] cmake-variables(7)
- [ ] cpack-generators(7)
