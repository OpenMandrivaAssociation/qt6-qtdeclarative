%define beta rc
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
%define liblabsanimation %mklibname Qt%{major}LabsAnimation %{major}
%define devlabsanimation %mklibname -d Qt%{major}LabsAnimation
%define liblabsfolderlistmodel %mklibname Qt%{major}LabsFolderListModel %{major}
%define devlabsfolderlistmodel %mklibname -d Qt%{major}LabsFolderListModel
%define liblabsqmlmodels %mklibname Qt%{major}LabsQmlModels %{major}
%define devlabsqmlmodels %mklibname -d Qt%{major}LabsQmlModels
%define liblabssettings %mklibname Qt%{major}LabsSettings %{major}
%define devlabssettings %mklibname -d Qt%{major}LabsSettings
%define liblabssharedimage %mklibname Qt%{major}LabsSharedImage %{major}
%define devlabssharedimage %mklibname -d Qt%{major}LabsSharedImage
%define liblabswavefrontmesh %mklibname Qt%{major}LabsWaveFrontMesh %{major}
%define devlabswavefrontmesh %mklibname -d Qt%{major}LabsWaveFrontMesh
%define devqmldom %mklibname -d Qt%{major}QmlDom
%define libqmllocalstorage %mklibname Qt%{major}QmlLocalStorage %{major}
%define devqmllocalstorage %mklibname -d Qt%{major}QmlLocalStorage
%define libquicklayouts %mklibname Qt%{major}QuickLayouts %{major}
%define devquicklayouts %mklibname -d Qt%{major}QuickLayouts

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtdeclarative
Version:	6.1.0
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
BuildRequires:	%{_lib}Qt%{major}OpenGLWidgets-devel
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}Test-devel
BuildRequires:	qt6-qtbase-tools
BuildRequires:	qmake-qt6
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
%{_qtdir}/lib/metatypes/qt%{major}qml_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlmodels_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlworkerscript_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quick_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quickparticles_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quickshapes_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}quicktest_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}chartsplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qtimeexampleplugin_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}textballoonplugin_relwithdebinfo_metatypes.json
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
%{_qtdir}/mkspecs/modules/qt_lib_quickwidgets.pri
%{_qtdir}/mkspecs/modules/qt_lib_quickwidgets_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmltest.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmltest_private.pri
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
%{_qtdir}/lib/metatypes/qt6quicktooling_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt6quickwindow_relwithdebinfo_metatypes.json

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
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DQT_FEATURE_dynamicgl:BOOL=ON \
	-DQT_FEATURE_use_lld_linker:BOOL=ON \
	-DQT_FEATURE_xcb_native_painting:BOOL=ON \
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

%package -n %{liblabsanimation}
Summary:	Qt %{major} animation library
Group:		System/Libraries

%description -n %{liblabsanimation}
Qt %{major} animation library

%files -n %{liblabsanimation}
%{_libdir}/libQt6LabsAnimation.so.%{major}*
%{_libdir}/qt6/lib/libQt6LabsAnimation.so.%{major}*

%package -n %{devlabsanimation}
Summary:	Development files for the Qt %{major} animation library
Group:		Development/KDE and Qt
Requires:	%{liblabsanimation} = %{EVRD}

%description -n %{devlabsanimation}
Development files for the Qt %{major} animation library

%files -n %{devlabsanimation}
%{_libdir}/cmake/Qt6LabsAnimation
%{_libdir}/libQt6LabsAnimation.so
%{_libdir}/qt6/include/QtLabsAnimation
%{_libdir}/qt6/lib/cmake/Qt6LabsAnimation
%{_libdir}/qt6/lib/libQt6LabsAnimation.prl
%{_libdir}/qt6/lib/libQt6LabsAnimation.so
%{_libdir}/qt6/lib/metatypes/qt6labsanimation_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_labsanimation.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_labsanimation_private.pri
%{_libdir}/qt6/modules/LabsAnimation.json

%package -n %{liblabsfolderlistmodel}
Summary:	Qt %{major} folder list model library
Group:		System/Libraries

%description -n %{liblabsfolderlistmodel}
Qt %{major} folder list model library

%files -n %{liblabsfolderlistmodel}
%{_libdir}/libQt6LabsFolderListModel.so.%{major}*
%{_libdir}/qt6/lib/libQt6LabsFolderListModel.so.%{major}*

%package -n %{devlabsfolderlistmodel}
Summary:	Development files for the Qt %{major} folder list model library
Group:		Development/KDE and Qt
Requires:	%{liblabsfolderlistmodel} = %{EVRD}

%description -n %{devlabsfolderlistmodel}
Development files for the Qt %{major} folder list model library

%files -n %{devlabsfolderlistmodel}
%{_libdir}/cmake/Qt6LabsFolderListModel
%{_libdir}/libQt6LabsFolderListModel.so
%{_libdir}/qt6/include/QtLabsFolderListModel
%{_libdir}/qt6/lib/cmake/Qt6LabsFolderListModel
%{_libdir}/qt6/lib/libQt6LabsFolderListModel.prl
%{_libdir}/qt6/lib/libQt6LabsFolderListModel.so
%{_libdir}/qt6/lib/metatypes/qt6labsfolderlistmodel_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_labsfolderlistmodel.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_labsfolderlistmodel_private.pri
%{_libdir}/qt6/modules/LabsFolderListModel.json

%package -n %{liblabsqmlmodels}
Summary:	Qt %{major} QML models library
Group:		System/Libraries

%description -n %{liblabsqmlmodels}
Qt %{major} QML models library

%files -n %{liblabsqmlmodels}
%{_libdir}/libQt6LabsQmlModels.so.%{major}*
%{_libdir}/qt6/lib/libQt6LabsQmlModels.so.%{major}*

%package -n %{devlabsqmlmodels}
Summary:	Development files for the Qt %{major} QML Models library
Group:		Development/KDE and Qt
Requires:	%{liblabsqmlmodels} = %{EVRD}

%description -n %{devlabsqmlmodels}
Development files for the Qt %{major} QML Models library

%files -n %{devlabsqmlmodels}
%{_libdir}/cmake/Qt6LabsQmlModels
%{_libdir}/libQt6LabsQmlModels.so
%{_libdir}/qt6/include/QtLabsQmlModels
%{_libdir}/qt6/lib/cmake/Qt6LabsQmlModels
%{_libdir}/qt6/lib/libQt6LabsQmlModels.prl
%{_libdir}/qt6/lib/libQt6LabsQmlModels.so
%{_libdir}/qt6/lib/metatypes/qt6labsqmlmodels_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_labsqmlmodels.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_labsqmlmodels_private.pri
%{_libdir}/qt6/modules/LabsQmlModels.json

%package -n %{liblabssettings}
Summary:	Qt %{major} Settings library
Group:		System/Libraries

%description -n %{liblabssettings}
Qt %{major} Settings library

%files -n %{liblabssettings}
%{_libdir}/libQt6LabsSettings.so.%{major}*
%{_libdir}/qt6/lib/libQt6LabsSettings.so.%{major}*

%package -n %{devlabssettings}
Summary:	Development files for the Qt %{major} settings library
Group:		Development/KDE and Qt
Requires:	%{liblabssettings} = %{EVRD}

%description -n %{devlabssettings}
Development files for the Qt %{major} settings library

%files -n %{devlabssettings}
%{_libdir}/libQt6LabsSettings.so
%{_libdir}/cmake/Qt6LabsSettings
%{_libdir}/qt6/include/QtLabsSettings
%{_libdir}/qt6/lib/cmake/Qt6LabsSettings
%{_libdir}/qt6/lib/libQt6LabsSettings.prl
%{_libdir}/qt6/lib/libQt6LabsSettings.so
%{_libdir}/qt6/lib/metatypes/qt6labssettings_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_labssettings.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_labssettings_private.pri
%{_libdir}/qt6/modules/LabsSettings.json

%package -n %{liblabssharedimage}
Summary:	Qt %{major} Shared Image library
Group:		System/Libraries

%description -n %{liblabssharedimage}
Qt %{major} Shared Image library

%files -n %{liblabssharedimage}
%{_libdir}/libQt6LabsSharedImage.so.%{major}*
%{_libdir}/qt6/lib/libQt6LabsSharedImage.so.%{major}*

%package -n %{devlabssharedimage}
Summary:	Development files for the Qt %{major} shared image library
Group:		Development/KDE and Qt
Requires:	%{liblabssharedimage} = %{EVRD}

%description -n %{devlabssharedimage}
Development files for the Qt %{major} shared image library

%files -n %{devlabssharedimage}
%{_libdir}/cmake/Qt6LabsSharedImage
%{_libdir}/libQt6LabsSharedImage.so
%{_libdir}/qt6/include/QtLabsSharedImage
%{_libdir}/qt6/lib/cmake/Qt6LabsSharedImage
%{_libdir}/qt6/lib/libQt6LabsSharedImage.prl
%{_libdir}/qt6/lib/libQt6LabsSharedImage.so
%{_libdir}/qt6/lib/metatypes/qt6labssharedimage_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_labssharedimage.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_labssharedimage_private.pri
%{_libdir}/qt6/modules/LabsSharedImage.json

%package -n %{liblabswavefrontmesh}
Summary:	Qt %{major} Wavefront Mesh library
Group:		System/Libraries

%description -n %{liblabswavefrontmesh}
Qt %{major} Wavefront Mesh library

%files -n %{liblabswavefrontmesh}
%{_libdir}/libQt6LabsWavefrontMesh.so.%{major}*
%{_libdir}/qt6/lib/libQt6LabsWavefrontMesh.so.%{major}*

%package -n %{devlabswavefrontmesh}
Summary:	Development files for the Qt %{major} wave front mesh library
Group:		Development/KDE and Qt
Requires:	%{liblabswavefrontmesh} = %{EVRD}

%description -n %{devlabswavefrontmesh}
Development files for the Qt %{major} wave front mesh library

%files -n %{devlabswavefrontmesh}
%{_libdir}/cmake/Qt6LabsWavefrontMesh
%{_libdir}/libQt6LabsWavefrontMesh.so
%{_libdir}/qt6/include/QtLabsWavefrontMesh
%{_libdir}/qt6/lib/cmake/Qt6LabsWavefrontMesh
%{_libdir}/qt6/lib/libQt6LabsWavefrontMesh.prl
%{_libdir}/qt6/lib/libQt6LabsWavefrontMesh.so
%{_libdir}/qt6/lib/metatypes/qt6labswavefrontmesh_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_labswavefrontmesh.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_labswavefrontmesh_private.pri
%{_libdir}/qt6/modules/LabsWavefrontMesh.json

%package -n %{devqmldom}
Summary:	Development files for the Qt %{major} QML DOM library
Group:		Development/KDE and Qt

%description -n %{devqmldom}
Development files for the Qt %{major} QML DOM library

%files -n %{devqmldom}
%{_libdir}/libQt6QmlDom.a
%{_libdir}/cmake/Qt6QmlDom
%{_libdir}/qt6/include/QtQmlDom
%{_libdir}/qt6/lib/cmake/Qt6QmlDom
%{_libdir}/qt6/lib/libQt6QmlDom.a
%{_libdir}/qt6/lib/libQt6QmlDom.prl
%{_libdir}/qt6/mkspecs/modules/qt_lib_qmldom_private.pri
%{_libdir}/qt6/modules/QmlDom.json

%package -n %{libqmllocalstorage}
Summary:	Qt %{major} Qml Local Storage library
Group:		System/Libraries

%description -n %{libqmllocalstorage}
Qt %{major} Qml Local Storage library

%files -n %{libqmllocalstorage}
%{_libdir}/libQt6QmlLocalStorage.so.%{major}*
%{_libdir}/qt6/lib/libQt6QmlLocalStorage.so.%{major}*

%package -n %{devqmllocalstorage}
Summary:	Development files for the Qt %{major} QML local storage library
Group:		Development/KDE and Qt
Requires:	%{libqmllocalstorage} = %{EVRD}

%description -n %{devqmllocalstorage}
Development files for the Qt %{major} QML local storage library

%files -n %{devqmllocalstorage}
%{_libdir}/cmake/Qt6QmlLocalStorage
%{_libdir}/libQt6QmlLocalStorage.so
%{_libdir}/qt6/include/QtQmlLocalStorage
%{_libdir}/qt6/lib/cmake/Qt6QmlLocalStorage
%{_libdir}/qt6/lib/libQt6QmlLocalStorage.prl
%{_libdir}/qt6/lib/libQt6QmlLocalStorage.so
%{_libdir}/qt6/lib/metatypes/qt6qmllocalstorage_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_qmllocalstorage.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_qmllocalstorage_private.pri
%{_libdir}/qt6/modules/QmlLocalStorage.json

%package -n %{libquicklayouts}
Summary:	Qt %{major} Qt Quick Layouts library
Group:		System/Libraries

%description -n %{libquicklayouts}
Qt %{major} Qt Quick Layouts library

%files -n %{libquicklayouts}
%{_libdir}/libQt6QuickLayouts.so.%{major}*
%{_libdir}/qt6/lib/libQt6QuickLayouts.so.%{major}*

%package -n %{devquicklayouts}
Summary:	Development files for the Qt %{major} Quick Layouts library
Group:		Development/KDE and Qt
Requires:	%{libquicklayouts} = %{EVRD}

%description -n %{devquicklayouts}
Development files for the Qt %{major} Quick Layouts library

%files -n %{devquicklayouts}
%{_libdir}/cmake/Qt6QuickLayouts
%{_libdir}/libQt6QuickLayouts.so
%{_libdir}/qt6/include/QtQuickLayouts
%{_libdir}/qt6/lib/cmake/Qt6QuickLayouts
%{_libdir}/qt6/lib/libQt6QuickLayouts.prl
%{_libdir}/qt6/lib/libQt6QuickLayouts.so
%{_libdir}/qt6/lib/metatypes/qt6quicklayouts_relwithdebinfo_metatypes.json
%{_libdir}/qt6/mkspecs/modules/qt_lib_quicklayouts.pri
%{_libdir}/qt6/mkspecs/modules/qt_lib_quicklayouts_private.pri
%{_libdir}/qt6/modules/QuickLayouts.json
