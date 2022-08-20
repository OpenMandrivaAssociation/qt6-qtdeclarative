%define beta beta3

Name:		qt6-qtdeclarative
Version:	6.4.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}2
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtdeclarative.git
Source:		qtdeclarative-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtdeclarative-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Version %{qtmajor} of the Qt Quick framework
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qt6-cmake
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6ShaderTools) = %{version}
BuildRequires:	qt6-qtbase-tools
BuildRequires:	qmake-qt6
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	rpm-provreq-qml
License:	LGPLv3/GPLv3/GPLv2

%description
Version %{qtmajor} of the Qt Quick framework

%define extra_files_Qml \
%{_qtdir}/plugins/qmltooling \
%dir %{_qtdir}/qml/Qt \
%dir %{_qtdir}/qml/Qt/labs \
%{_qtdir}/qml/Qt/labs/animation \
%{_qtdir}/qml/Qt/labs/platform \
%{_qtdir}/qml/Qt/labs/sharedimage \
%{_qtdir}/qml/Qt/labs/wavefrontmesh \
%{_qtdir}/qml/QtTest

%define extra_devel_files_Qml \
%{_qtdir}/include/QtQuick \
%{_qtdir}/include/QtQuickTemplates2 \
%{_qtdir}/lib/cmake/Qt%{qtmajor}BuildInternals/* \
%{_qtdir}/lib/cmake/Qt%{qtmajor}QmlDebugPrivate \
%{_qtdir}/lib/metatypes/qt%{qtmajor}qmlworkerscript_relwithdebinfo_metatypes.json \
%{_qtdir}/plugins/qmltooling/libqmldbg_debugger.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_local.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_messages.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_native.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_nativedebugger.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_profiler.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_server.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_tcp.so \
%{_qtdir}/qml/Qt/labs/folderlistmodel \
%{_qtdir}/qml/Qt/labs/qmlmodels \
%{_qtdir}/qml/Qt/labs/settings \
%{_qtdir}/qml/builtins.qmltypes \
%{_qtdir}/modules/QmlDebugPrivate.json \
%{_qtdir}/lib/cmake/Qt%{qtmajor}QmlImportScanner \
%{_qtdir}/mkspecs/features/qtquickcompiler.prf \
%{_qtdir}/mkspecs/features/qmlcache.prf \
%{_qtdir}/mkspecs/features/qmltypes.prf \
%{_qtdir}/lib/metatypes/qt%{qtmajor}qmlcompilerprivate_relwithdebinfo_metatypes.json \
%{_qtdir}/lib/cmake/Qt6QmlIntegration \
%{_qtdir}/bin/qmltc \
%{_qtdir}/include/QtQmlIntegration \
%{_qtdir}/mkspecs/modules/qt_lib_qmlintegration.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmlintegration_private.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmltest.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmltest_private.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmlworkerscript.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmlworkerscript_private.pri \
%{_qtdir}/mkspecs/modules/qt_lib_quickcontrolstestutilsprivate_private.pri \
%{_qtdir}/mkspecs/modules/qt_lib_quicktestutilsprivate_private.pri \
%{_qtdir}/modules/QmlIntegration.json \
%{_qtdir}/lib/pkgconfig/Qt6QmlIntegration.pc

%define extra_reqprov_Qml \
Requires:	rpm-provreq-qml \
Requires:	%mklibname Qt%{qtmajor}QmlCore

%define extra_devel_reqprov_Qml \
Requires:	%{name} = %{EVRD}

%define extra_files_QmlCore \
%dir %{_qtdir}/qml \
%{_qtdir}/qml/QtCore \
%{_qtdir}/qml/QtQuick \
%{_qtdir}/qml/jsroot.qmltypes \
%{_qtdir}/qml/QtQml

# qmltyperegistrar and friends
%define extra_devel_reqprov_QmlCore \
Requires:	%{name} = %{EVRD}

%qt6libs LabsAnimation LabsFolderListModel LabsQmlModels LabsSettings LabsSharedImage LabsWavefrontMesh Quick QuickControls2 QuickControls2Impl QuickDialogs2 QuickDialogs2QuickImpl QuickDialogs2Utils QuickLayouts QuickParticles QuickShapes QuickTemplates2 QuickTest QuickWidgets QmlWorkerScript Qml QmlCore QmlModels QmlLocalStorage QmlXmlListModel QmlCompiler
%qt6staticlibs QuickControlsTestUtils QuickTestUtils QmlDebug QmlDom PacketProtocol

%package examples
Summary: Example applications for Qt Declarative %{qtmajor}
Group: Development/KDE and Qt

%description examples
Example applications for Qt Declarative %{qtmajor}

%files examples
%{_qtdir}/examples/qml
%{_qtdir}/examples/quick
%{_qtdir}/examples/quickcontrols2
%{_qtdir}/examples/qmltest

%prep
%autosetup -p1 -n qtdeclarative%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DQT_MKSPECS_DIR:FILEPATH=%{_qtdir}/mkspecs \
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
# Seems to be an accidentally installed object file
rm -rf %{buildroot}%{_qtdir}/lib/objects-RelWithDebInfo

%files
%{_qtdir}/bin/qml
%{_qtdir}/bin/qmldom
%{_qtdir}/bin/qmlformat
%{_qtdir}/bin/qmllint
%{_qtdir}/bin/qmlpreview
%{_qtdir}/bin/qmlprofiler
%{_qtdir}/bin/qmleasing
%{_qtdir}/bin/qmlplugindump
%{_qtdir}/bin/qmlscene
%{_qtdir}/bin/qmltestrunner
%{_qtdir}/bin/qmltime
%{_qtdir}/libexec/qmlcachegen
%{_qtdir}/libexec/qmlimportscanner
%{_qtdir}/libexec/qmltyperegistrar
%{_qtdir}/plugins/qmllint
