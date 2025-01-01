Summary:	Object-Oriented Graphics Rendering Engine
Name:		ogre-next
Version:	2.3.3
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		https://www.ogre3d.org/
Source0:	https://github.com/OGRECave/ogre-next/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#Source1:        https://github.com/ocornut/imgui/archive/%{imgui_short_ver}/imgui-%{imgui_ver}.tar.gz

BuildRequires:	cmakeBuildRequires:	ninja
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
BuildRequires:  pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(zziplib)
BuildRequires:	tinyxml-devel
BuildRequires:  pugixml-devel
BuildRequires:	doxygen
BuildConflicts:	cg-devel

%description
OGRE  (Object-Oriented  Graphics  Rendering  Engine)  is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier  and  more
intuitive for developers to produce games and demos utilising 3D hardware.
The class library abstracts all the details  of  using the underlying system
libraries like Direct3D and OpenGL and provides an interface based on world
objects and other intuitive classes.

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
#export CC=gcc
#export CXX=g++
%ninja_build -C build

%install
%ninja_install -C build

%files
