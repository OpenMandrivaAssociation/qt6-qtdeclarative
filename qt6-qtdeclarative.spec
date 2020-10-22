%define beta beta1
#define snapshot 20200627
%define major 6

%define libqml %mklibname Qt%{major}Qml %{major}
%define devqml %mklibname -d Qt%{major}Qml
%define devqmldebug %mklibname -d Qt%{major}QmlDebug
%define libqmlmodels %mklibname Qt%{major}QmlModels %{major}
%define devqmlmodels %mklibname -d Qt%{major}QmlModels
%define libqmlworkerscript %mklibname Qt%{major}QmlWorkerScript %{major}
%define devqmlworkerscript %mklibname -d Qt%{major}QmlWorkerScript
%define libquick %mklibname Qt%{major}QmlQuick %{major}
%define devquick %mklibname -d Qt%{major}QmlQuick
%define libquickparticles %mklibname Qt%{major}QmlQuickParticles %{major}
%define devquickparticles %mklibname -d Qt%{major}QmlQuickParticles
%define libquickshapes %mklibname Qt%{major}QmlQuickShapes %{major}
%define devquickshapes %mklibname -d Qt%{major}QmlQuickShapes
%define libquicktest %mklibname Qt%{major}QmlQuickTest %{major}
%define devquicktest %mklibname -d Qt%{major}QmlQuickTest
%define libquickwidgets %mklibname Qt%{major}QmlQuickWidgets %{major}
%define devquickwidgets %mklibname -d Qt%{major}QmlQuickWidgets
%define devpacketprotocol %mklibname -d Qt%{major}PacketProtocol
%define devqmldebug %mklibname -d Qt%{major}QmlDebug
%define devqmldevtools %mklibname -d Qt%{major}QmlDevTools

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtdeclarative
Version:	6.0.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtdeclarative.git
Source:		qtdeclarative-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtdeclarative-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Version %{major} of the Qt Quick framework
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qt6-cmake
BuildRequires:	%{_lib}Qt%{major}Concurrent-devel
BuildRequires:	%{_lib}Qt%{major}Core-devel
BuildRequires:	%{_lib}Qt%{major}Gui-devel
BuildRequires:	%{_lib}Qt%{major}Widgets-devel
BuildRequires:	%{_lib}Qt%{major}Network-devel
BuildRequires:	%{_lib}Qt%{major}OpenGL-devel
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}Test-devel
BuildRequires:	qt6-qtbase-tools
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(vulkan)
License:	LGPLv3/GPLv3/GPLv2

%description
Version %{major} of the Qt Quick framework

%package -n %{libqml}
Summary:	Qt %{major} Qml library
Group:		System/Libraries

%description -n %{libqml}
Qt %{major} Qml library

%files -n %{libqml}
%{_libdir}/libQt%{major}Qml.so.%{major}*
%{_qtdir}/lib/libQt%{major}Qml.so.%{major}*

%package -n %{devqml}
Summary:	Development files for the Qt %{major} Qml library
Group:		Development/KDE and Qt
Requires:	%{libqml} = %{EVRD}

%description -n %{devqml}
Development files for the Qt %{major} Qml library

%files -n %{devqml}
%{_libdir}/libQt%{major}Qml.so
%{_qtdir}/qml/QtQml
%{_libdir}/cmake/Qt%{major}Qml
%{_qtdir}/modules/Qml.json
%{_qtdir}/lib/libQt%{major}Qml.prl
%{_qtdir}/lib/libQt%{major}Qml.so
%{_qtdir}/include/QtQml
%{_qtdir}/lib/cmake/Qt%{major}Qml

%{_libdir}/cmake/Qt%{major}BuildInternals
%{_qtdir}/lib/cmake/Qt%{major}BuildInternals

%{_libdir}/cmake/Qt%{major}QmlTools

%{_qtdir}/lib/cmake/Qt%{major}QmlTools
%{_qtdir}/lib/metatypes/qt%{major}labsanimationplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}labsmodelsplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qml_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlfolderlistmodelplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmllocalstorageplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlmodels_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlsettingsplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmltestplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlwavefrontmeshplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlworkerscript_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qquicklayoutsplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quick_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quickparticles_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quickshapes_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quicktest_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}sharedimageplugin_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_qml.pri
%{_qtdir}/mkspecs/modules/qt_lib_qml_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmldebug_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlmodels.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_quick.pri
%{_qtdir}/mkspecs/modules/qt_lib_quick_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_quickparticles_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_quickshapes_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_quicktest.pri
%{_qtdir}/mkspecs/modules/qt_lib_quicktest_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_quickwidgets.pri
%{_qtdir}/mkspecs/modules/qt_lib_quickwidgets_private.pri
%{_qtdir}/mkspecs/modules/qt_plugin_labsanimationplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_labsmodelsplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_modelsplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_particlesplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_debugger.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_inspector.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_local.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_messages.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_native.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_nativedebugger.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_preview.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_profiler.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_quickprofiler.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_server.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmldbg_tcp.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmlfolderlistmodelplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmllocalstorageplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmlplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmlsettingsplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmlshapesplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmltestplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qmlwavefrontmeshplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qquicklayoutsplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_qtquick2plugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_sharedimageplugin.pri
%{_qtdir}/mkspecs/modules/qt_plugin_workerscriptplugin.pri
%{_qtdir}/plugins/qmltooling/libqmldbg_debugger.so
%{_qtdir}/plugins/qmltooling/libqmldbg_inspector.so
%{_qtdir}/plugins/qmltooling/libqmldbg_local.so
%{_qtdir}/plugins/qmltooling/libqmldbg_messages.so
%{_qtdir}/plugins/qmltooling/libqmldbg_native.so
%{_qtdir}/plugins/qmltooling/libqmldbg_nativedebugger.so
%{_qtdir}/plugins/qmltooling/libqmldbg_preview.so
%{_qtdir}/plugins/qmltooling/libqmldbg_profiler.so
%{_qtdir}/plugins/qmltooling/libqmldbg_quickprofiler.so
%{_qtdir}/plugins/qmltooling/libqmldbg_server.so
%{_qtdir}/plugins/qmltooling/libqmldbg_tcp.so
%{_qtdir}/qml/Qt/labs/animation
%{_qtdir}/qml/Qt/labs/folderlistmodel
%{_qtdir}/qml/Qt/labs/qmlmodels
%{_qtdir}/qml/Qt/labs/settings
%{_qtdir}/qml/Qt/labs/sharedimage
%{_qtdir}/qml/Qt/labs/wavefrontmesh
%{_qtdir}/qml/Qt/test/qtestroot
%{_qtdir}/qml/QtTest
%{_qtdir}/qml/builtins.qmltypes

%{_libdir}/cmake/Qt6QmlCompiler
%{_libdir}/cmake/Qt6QmlImportScanner
%{_libdir}/libQt6QmlCompiler.a
%{_qtdir}/include/QtQmlCompiler
%{_qtdir}/lib/cmake/Qt6QmlCompiler
%{_qtdir}/lib/cmake/Qt6QmlImportScanner
%{_qtdir}/lib/libQt6QmlCompiler.a
%{_qtdir}/lib/libQt6QmlCompiler.prl
%{_qtdir}/mkspecs/features/qmlcache.prf
%{_qtdir}/mkspecs/features/qmltypes.prf
%{_qtdir}/mkspecs/features/qtquickcompiler.prf
%{_qtdir}/mkspecs/modules/qt_lib_qmlcompiler_private.pri
%{_qtdir}/modules/QmlCompiler.json

%package -n %{devqmldebug}
Summary:	Development files for the Qt %{major} Qml Debug library
Group:		Development/KDE and Qt

%description -n %{devqmldebug}
Development files for the Qt %{major} Qml Debug library

%files -n %{devqmldebug}
%{_libdir}/libQt%{major}QmlDebug.a
%{_libdir}/cmake/Qt%{major}QmlDebug
%{_qtdir}/modules/QmlDebug.json
%{_qtdir}/lib/libQt%{major}QmlDebug.prl
%{_qtdir}/lib/libQt%{major}QmlDebug.a
%{_qtdir}/include/QtQmlDebug
%{_qtdir}/lib/cmake/Qt%{major}QmlDebug

%package -n %{libqmlmodels}
Summary:	Qt %{major} Qml Models library
Group:		System/Libraries

%description -n %{libqmlmodels}
Qt %{major} Qml library

%files -n %{libqmlmodels}
%{_libdir}/libQt%{major}QmlModels.so.%{major}*
%{_qtdir}/lib/libQt%{major}QmlModels.so.%{major}*

%package -n %{devqmlmodels}
Summary:	Development files for the Qt %{major} Qml Models library
Group:		Development/KDE and Qt
Requires:	%{libqmlmodels} = %{EVRD}

%description -n %{devqmlmodels}
Development files for the Qt %{major} Qml Models library

%files -n %{devqmlmodels}
%{_libdir}/libQt%{major}QmlModels.so
%{_libdir}/cmake/Qt%{major}QmlModels
%{_qtdir}/modules/QmlModels.json
%{_qtdir}/lib/libQt%{major}QmlModels.prl
%{_qtdir}/lib/libQt%{major}QmlModels.so
%{_qtdir}/include/QtQmlModels
%{_qtdir}/lib/cmake/Qt%{major}QmlModels

%package -n %{libqmlworkerscript}
Summary:	Qt %{major} Qml Worker Script library
Group:		System/Libraries

%description -n %{libqmlworkerscript}
Qt %{major} Qml Worker Script library

%files -n %{libqmlworkerscript}
%{_libdir}/libQt%{major}QmlWorkerScript.so.%{major}*
%{_qtdir}/lib/libQt%{major}QmlWorkerScript.so.%{major}*

%package -n %{devqmlworkerscript}
Summary:	Development files for the Qt %{major} Qml Worker Script library
Group:		Development/KDE and Qt
Requires:	%{libqmlworkerscript} = %{EVRD}

%description -n %{devqmlworkerscript}
Development files for the Qt %{major} Qml Worker Script library

%files -n %{devqmlworkerscript}
%{_libdir}/libQt%{major}QmlWorkerScript.so
%{_libdir}/cmake/Qt%{major}QmlWorkerScript
%{_qtdir}/modules/QmlWorkerScript.json
%{_qtdir}/lib/libQt%{major}QmlWorkerScript.prl
%{_qtdir}/lib/libQt%{major}QmlWorkerScript.so
%{_qtdir}/include/QtQmlWorkerScript
%{_qtdir}/lib/cmake/Qt%{major}QmlWorkerScript

%package -n %{libquick}
Summary:	Qt %{major} Qt Quick library
Group:		System/Libraries

%description -n %{libquick}
Qt %{major} Qt Quick library

%files -n %{libquick}
%{_libdir}/libQt%{major}Quick.so.%{major}*
%{_qtdir}/lib/libQt%{major}Quick.so.%{major}*

%package -n %{devquick}
Summary:	Development files for the Qt %{major} Qt Quick library
Group:		Development/KDE and Qt
Requires:	%{libquick} = %{EVRD}

%description -n %{devquick}
Development files for the Qt %{major} Qt Quick library

%files -n %{devquick}
%{_libdir}/libQt%{major}Quick.so
%{_qtdir}/qml/QtQuick
%{_libdir}/cmake/Qt%{major}Quick
%{_qtdir}/modules/Quick.json
%{_qtdir}/lib/libQt%{major}Quick.prl
%{_qtdir}/lib/libQt%{major}Quick.so
%{_qtdir}/include/QtQuick
%{_qtdir}/lib/cmake/Qt%{major}Quick

%package -n %{libquickparticles}
Summary:	Qt %{major} Qt Quick Particles library
Group:		System/Libraries

%description -n %{libquickparticles}
Qt %{major} Qt Quick Patricles library

%files -n %{libquickparticles}
%{_libdir}/libQt%{major}QuickParticles.so.%{major}*
%{_qtdir}/lib/libQt%{major}QuickParticles.so.%{major}*

%package -n %{devquickparticles}
Summary:	Development files for the Qt %{major} Qt Quick Particles library
Group:		Development/KDE and Qt
Requires:	%{libquickparticles} = %{EVRD}

%description -n %{devquickparticles}
Development files for the Qt %{major} Qt Quick Particles library

%files -n %{devquickparticles}
%{_libdir}/libQt%{major}QuickParticles.so
%{_libdir}/cmake/Qt%{major}QuickParticles
%{_qtdir}/modules/QuickParticles.json
%{_qtdir}/lib/libQt%{major}QuickParticles.prl
%{_qtdir}/lib/libQt%{major}QuickParticles.so
%{_qtdir}/include/QtQuickParticles
%{_qtdir}/lib/cmake/Qt%{major}QuickParticles

%package -n %{libquickshapes}
Summary:	Qt %{major} Qt Quick Shapes library
Group:		System/Libraries

%description -n %{libquickshapes}
Qt %{major} Qt Quick Shapes library

%files -n %{libquickshapes}
%{_libdir}/libQt%{major}QuickShapes.so.%{major}*
%{_qtdir}/lib/libQt%{major}QuickShapes.so.%{major}*

%package -n %{devquickshapes}
Summary:	Development files for the Qt %{major} Qt Quick Shapes library
Group:		Development/KDE and Qt
Requires:	%{libquickshapes} = %{EVRD}

%description -n %{devquickshapes}
Development files for the Qt %{major} Qt Quick Shapes library

%files -n %{devquickshapes}
%{_libdir}/libQt%{major}QuickShapes.so
%{_libdir}/cmake/Qt%{major}QuickShapes
%{_qtdir}/modules/QuickShapes.json
%{_qtdir}/lib/libQt%{major}QuickShapes.prl
%{_qtdir}/lib/libQt%{major}QuickShapes.so
%{_qtdir}/include/QtQuickShapes
%{_qtdir}/lib/cmake/Qt%{major}QuickShapes

%package -n %{libquicktest}
Summary:	Qt %{major} Qt Quick Test library
Group:		System/Libraries

%description -n %{libquicktest}
Qt %{major} Qt Quick Test library

%files -n %{libquicktest}
%{_libdir}/libQt%{major}QuickTest.so.%{major}*
%{_qtdir}/lib/libQt%{major}QuickTest.so.%{major}*

%package -n %{devquicktest}
Summary:	Development files for the Qt %{major} Qt Quick Test library
Group:		Development/KDE and Qt
Requires:	%{libquicktest} = %{EVRD}

%description -n %{devquicktest}
Development files for the Qt %{major} Qt Quick Test library

%files -n %{devquicktest}
%{_libdir}/libQt%{major}QuickTest.so
%{_libdir}/cmake/Qt%{major}QuickTest
%{_qtdir}/modules/QuickTest.json
%{_qtdir}/lib/libQt%{major}QuickTest.prl
%{_qtdir}/lib/libQt%{major}QuickTest.so
%{_qtdir}/include/QtQuickTest
%{_qtdir}/lib/cmake/Qt%{major}QuickTest

%package -n %{libquickwidgets}
Summary:	Qt %{major} Qt Quick Widgets library
Group:		System/Libraries

%description -n %{libquickwidgets}
Qt %{major} Qt Quick Widgets library

%files -n %{libquickwidgets}
%{_libdir}/libQt%{major}QuickWidgets.so.%{major}*
%{_qtdir}/lib/libQt%{major}QuickWidgets.so.%{major}*

%package -n %{devquickwidgets}
Summary:	Development files for the Qt %{major} Quick Widgets library
Group:		Development/KDE and Qt
Requires:	%{libquickwidgets} = %{EVRD}

%description -n %{devquickwidgets}
Development files for the Qt %{major} Quick Widgets library

%files -n %{devquickwidgets}
%{_libdir}/libQt%{major}QuickWidgets.so
%{_libdir}/cmake/Qt%{major}QuickWidgets
%{_qtdir}/modules/QuickWidgets.json
%{_qtdir}/lib/libQt%{major}QuickWidgets.prl
%{_qtdir}/lib/libQt%{major}QuickWidgets.so
%{_qtdir}/include/QtQuickWidgets
%{_qtdir}/lib/cmake/Qt%{major}QuickWidgets


%package -n %{devpacketprotocol}
Summary:	Development files for the Qt %{major} Packet Protocol library
Group:		Development/KDE and Qt

%description -n %{devpacketprotocol}
Development files for the Qt %{major} Packet Protocol library

%files -n %{devpacketprotocol}
%{_qtdir}/lib/cmake/Qt%{major}PacketProtocol
%{_libdir}/libQt%{major}PacketProtocol.a
%{_qtdir}/include/QtPacketProtocol
%{_libdir}/cmake/Qt%{major}PacketProtocol
%{_qtdir}/lib/libQt%{major}PacketProtocol.a
%{_qtdir}/lib/libQt%{major}PacketProtocol.prl
%{_qtdir}/mkspecs/modules/qt_lib_packetprotocol_private.pri
%{_qtdir}/modules/PacketProtocol.json


%package -n %{devqmldevtools}
Summary:	Development files for the Qt %{major} Qml DevTools library
Group:		Development/KDE and Qt

%description -n %{devqmldevtools}
Development files for the Qt %{major} Qml DevTools library

%files -n %{devqmldevtools}
%{_libdir}/cmake/Qt%{major}QmlDevTools
%{_libdir}/libQt%{major}QmlDevTools.a
%{_qtdir}/lib/cmake/Qt%{major}QmlDevTools
%{_qtdir}/lib/libQt%{major}QmlDevTools.a
%{_qtdir}/lib/libQt%{major}QmlDevTools.prl
%{_qtdir}/modules/QmlDevTools.json
%{_qtdir}/mkspecs/modules/qt_lib_qmldevtools_private.pri

%package examples
Summary: Example applications for Qt Declarative %{major}
Group: Development/KDE and Qt

%description examples
Example applications for Qt Declarative %{major}

%files examples
%{_qtdir}/examples/qml
%{_qtdir}/examples/quick
%{_qtdir}/examples/tst_qmltestexample

%prep
%autosetup -p1 -n qtdeclarative%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DQT_SYNCQT=%{_qtdir}/bin/syncqt.pl \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DBUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DFEATURE_cxx2a:BOOL=ON \
	-DFEATURE_dynamicgl:BOOL=ON \
	-DFEATURE_ftp:BOOL=ON \
	-DFEATURE_opengl_dynamic:BOOL=ON \
	-DFEATURE_use_lld_linker:BOOL=ON \
	-DFEATURE_xcb_native_painting:BOOL=ON \
	-DFEATURE_openssl:BOOL=ON \
	-DFEATURE_openssl_linked:BOOL=ON \
	-DFEATURE_system_sqlite:BOOL=ON \
	-DINPUT_sqlite=system \
	-DQT_WILL_INSTALL:BOOL=ON

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
# Static helper lib without headers -- useless
rm -f %{buildroot}%{_libdir}/qt6/%{_lib}/libpnp_basictools.a
# Put stuff where tools will find it
# We can't do the same for %{_includedir} right now because that would
# clash with qt5 (both would want to have /usr/include/QtCore and friends)
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir}/cmake
for i in %{buildroot}%{_qtdir}/lib/*.so* %{buildroot}%{_qtdir}/lib/*.a; do
	ln -s qt%{major}/lib/$(basename ${i}) %{buildroot}%{_libdir}/
done
for i in %{buildroot}%{_qtdir}/lib/cmake/*; do
	ln -s ../qt%{major}/lib/cmake/$(basename ${i}) %{buildroot}%{_libdir}/cmake/
done

%files
%{_qtdir}/bin/qml
%{_qtdir}/bin/qmlcachegen
%{_qtdir}/bin/qmleasing
%{_qtdir}/bin/qmlformat
%{_qtdir}/bin/qmlimportscanner
%{_qtdir}/bin/qmllint
%{_qtdir}/bin/qmlplugindump
%{_qtdir}/bin/qmlpreview
%{_qtdir}/bin/qmlprofiler
%{_qtdir}/bin/qmlscene
%{_qtdir}/bin/qmltestrunner
%{_qtdir}/bin/qmltime
%{_qtdir}/bin/qmltyperegistrar

