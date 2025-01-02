%define major 3.0
%define libname %mklibname ogre-next
%define devname %mklibname -d ogre-next

Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre-next
Version:	3.0.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.ogre3d.org/
Source0:	https://github.com/OGRECave/ogre-next/archive/v%{version}/%{name}-%{version}.tar.gz
#Source1:        https://github.com/ocornut/imgui/archive/%{imgui_short_ver}/imgui-%{imgui_ver}.tar.gz

BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	boost-devel
BuildRequires:	freeimage-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  swig
BuildRequires:	pkgconfig(cppunit)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
# Disable, until mono is not instalable in Cooker
#BuildRequires:  pkgconfig(mono)
BuildRequires:	pkgconfig(OIS)
BuildRequires:  pkgconfig(OpenEXR)
BuildRequires:  pkgconfig(python)
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xcb)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	pkgconfig(tinyxml)
BuildRequires:  pkgconfig(pugixml)
BuildRequires:	doxygen
BuildConflicts:	cg-devel

Requires: %{libname} = %{EVRD}
Provides: ogre-next = %{EVRD}

%description
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

%package -n %{libname}
Summary:        Shared library for %{name}

%description -n %{libname}
This package contains the shared library files.

%package -n %{devname}
Summary:        Development files for %{name}
Requires:	%{libname} = %{EVRD}
Requires:	%{name} = %{EVRD}
Provides:	ogre-next-devel = %{EVRD}

%description -n %{devname}
This package contains development files for %{name}.


%prep
%autosetup -p1

%cmake \
        -DOGRE_BUILD_DOCS:BOOL=OFF \
        -DOGRE_BUILD_DEPENDENCIES=FALSE \
        -DOGRE_BUILD_PLUGIN_CG:BOOL=OFF \
        -DOGRE_INSTALL_SAMPLES:BOOL=ON \
        -DOGRE_INSTALL_SAMPLES_SOURCE:BOOL=ON \
        -DOGRE_CONFIG_MEMTRACK_RELEASE:BOOL=OFF \
	-DOGRE_BUILD_COMPONENT_OVERLAY:BOOL=ON \
	-DOGRE_BUILD_COMPONENT_OVERLAY_IMGUI:BOOL=OFf \
	-DOGRE_BUILD_COMPONENT_CSHARP:BOOL=OFF \
	-DOGRE_BUILD_COMPONENT_JAVA:BOOL=OFF \
	-DOGRE_NODELESS_POSITIONING:BOOL=ON \
	-DOGRE_RESOURCEMANAGER_STRICT=0 \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/OgreCmgenToCubemap
%{_bindir}/OgreMeshTool
%{_datadir}/OGRE/

%finel -n sample
%{_bindir}/Sample_*

%files -n %{libname}
%{_libdir}/OGRE/Plugin_ParticleFX.so.%{major}
%{_libdir}/OGRE/RenderSystem_GL3Plus.so.%{major}
%{_libdir}/OGRE/RenderSystem_NULL.so.%{major}

%{_libdir}/libOgreAtmosphere.so.%{major}
%{_libdir}/libOgreHlmsPbs.so.%{major}
%{_libdir}/libOgreHlmsUnlit.so.%{major}
%{_libdir}/libOgreMain.so.%{major}
%{_libdir}/libOgreMeshLodGenerator.so.%{major}
%{_libdir}/libOgreOverlay.so.%{major}
%{_libdir}/libOgreSceneFormat.so.%{major}

%files -n %{devname}
%{_libdir}/OGRE/Plugin_ParticleFX.so
%{_libdir}/OGRE/RenderSystem_GL3Plus.so
%{_libdir}/OGRE/RenderSystem_NULL.so

%{_libdir}/libOgreAtmosphere.so
%{_libdir}/libOgreHlmsPbs.so
%{_libdir}/libOgreHlmsUnlit.so
%{_libdir}/libOgreMain.so
%{_libdir}/libOgreMeshLodGenerator.so
%{_libdir}/libOgreOverlay.so
%{_libdir}/libOgreSceneFormat.so

%{_libdir}/pkgconfig/OGRE-Hlms.pc
%{_libdir}/pkgconfig/OGRE-MeshLodGenerator.pc
%{_libdir}/pkgconfig/OGRE-Overlay.pc
%{_libdir}/pkgconfig/OGRE.pc

%{_libdir}/OGRE/cmake/FindOGRE.cmake
%{_libdir}/OGRE/cmake/FindPkgMacros.cmake
%{_libdir}/OGRE/cmake/FindRapidjson.cmake
%{_libdir}/OGRE/cmake/FindRemotery.cmake
%{_libdir}/OGRE/cmake/FindSDL2.cmake
%{_libdir}/OGRE/cmake/MacroLogFeature.cmake
%{_libdir}/OGRE/cmake/OgreAddTargets.cmake
%{_libdir}/OGRE/cmake/OgreConfigTargets.cmake
%{_libdir}/OGRE/cmake/OgreFindFrameworks.cmake
%{_libdir}/OGRE/cmake/OgreGetVersion.cmake
%{_libdir}/OGRE/cmake/PrecompiledHeader.cmake
%{_libdir}/OGRE/cmake/PreprocessorUtils.cmake

%{_includedir}/OGRE/
