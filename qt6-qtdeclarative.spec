#define beta rc

Name:		qt6-qtdeclarative
Version:	6.10.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtdeclarative.git
Source:		qtdeclarative-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		https://download.qt.io/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtdeclarative-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
# This is a workaround for the disk cache breaking Plasma badly.
# See e.g. https://www.reddit.com/r/kde/comments/18n3bfb/comment/keja252/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
Patch0:		qtdeclarative-disable-disk-cache.patch
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
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
#BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6LanguageServerPrivate)
#BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6JsonRpcPrivate)
BuildRequires:	cmake(Qt6ShaderTools) = %{version}
# for AssetsDownloader
BuildRequires:	cmake(Qt6ExamplesAssetDownloaderPrivate)
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
%dir %{_qtdir}/plugins/qmltooling \
%dir %{_qtdir}/qml/Qt \
%dir %{_qtdir}/qml/Qt/labs \
%{_qtdir}/qml/Qt/labs/animation \
%{_qtdir}/qml/Qt/labs/folderlistmodel \
%{_qtdir}/qml/Qt/labs/platform \
%{_qtdir}/qml/Qt/labs/qmlmodels \
%{_qtdir}/qml/Qt/labs/settings \
%{_qtdir}/qml/Qt/labs/sharedimage \
%{_qtdir}/qml/Qt/labs/wavefrontmesh \
%{_qtdir}/qml/QtTest \
%{_qtdir}/qml/QmlTime

%define extra_devel_files_Qml \
%{_qtdir}/include/QtQuick \
%{_qtdir}/include/QtQuickTemplates2 \
%{_qtdir}/lib/cmake/Qt%{qtmajor}BuildInternals/* \
%{_qtdir}/lib/cmake/Qt%{qtmajor}QmlDebugPrivate \
%{_qtdir}/plugins/qmltooling/libqmldbg_debugger.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_inspector.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_local.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_messages.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_native.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_nativedebugger.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_preview.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_profiler.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_quickprofiler.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_server.so \
%{_qtdir}/plugins/qmltooling/libqmldbg_tcp.so \
%{_qtdir}/modules/QmlDebugPrivate.json \
%{_qtdir}/lib/cmake/Qt%{qtmajor}QmlImportScanner \
%{_qtdir}/mkspecs/features/qtquickcompiler.prf \
%{_qtdir}/mkspecs/features/qmlcache.prf \
%{_qtdir}/mkspecs/features/qmltypes.prf \
%{_qtdir}/mkspecs/modules/qt_lib_qmlintegration.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmltest.pri \
%{_qtdir}/mkspecs/modules/qt_lib_qmltest_private.pri \
%{_qtdir}/lib/cmake/Qt6QmlIntegration \
%{_qtdir}/bin/qmltc \
%{_qtdir}/include/QtQmlIntegration \
%{_qtdir}/modules/QmlIntegration.json \
%{_libdir}/pkgconfig/Qt6QmlIntegration.pc \
%{_qtdir}/sbom/*

%define extra_reqprov_Qml \
Requires:	rpm-provreq-qml \
Requires:	%mklibname Qt%{qtmajor}QmlCore

%define extra_devel_reqprov_Qml \
Requires:	%{name} = %{EVRD} \
Requires:	cmake(Qt%{qtmajor}Core) \
Requires:	cmake(Qt%{qtmajor}Network) \

%define extra_files_QmlCore \
%dir %{_qtdir}/qml \
%{_qtdir}/qml/builtins.qmltypes \
%{_qtdir}/qml/QtCore \
%{_qtdir}/qml/QtQuick \
%{_qtdir}/qml/jsroot.qmltypes \
%{_qtdir}/qml/QtQml \
%{_qtdir}/bin/qmlls

%define extra_devel_files_QmlCore \
%{_qtdir}/libexec/qmljsrootgen

%define extra_files_QuickTest \
%{_qtdir}/qml/Qt/test

%define extra_devel_reqprov_Quick \
Requires:	cmake(Qt%{qtmajor}QmlModels) \
Requires:	cmake(Qt%{qtmajor}OpenGL) \
Requires:	cmake(Qt%{qtmajor}Qml)

%define extra_devel_files_QuickTest \
%{_qtdir}/mkspecs/modules/qt_lib_quicktestutilsprivate_private.pri \

%define extra_devel_reqprov_QuickTest \
Requires:	cmake(Qt%{qtmajor}Test)

%define extra_devel_files_QuickControls2 \
%{_qtdir}/mkspecs/modules/qt_lib_quickcontrolstestutilsprivate_private.pri 

%define extra_devel_reqprov_QuickControls2 \
Requires:	cmake(Qt%{qtmajor}QuickTemplates2)

%define extra_files_QmlNetwork \
%{_qtdir}/qml/QtNetwork

# qmltyperegistrar and friends
%define extra_devel_reqprov_QmlCore \
Requires:	%{name} = %{EVRD}

%define extra_devel_files_QmlAssetDownloader \
%{_libdir}/pkgconfig/Qt6QmlAssetDownloader.pc \
%{_qtdir}/qml/Qt/labs/assetdownloader

%define extra_files_LabsSynchronizer \
%{_qtdir}/qml/Qt/labs/synchronizer/

%qt6libs LabsAnimation LabsFolderListModel LabsPlatform LabsQmlModels LabsSettings LabsSharedImage LabsWavefrontMesh Quick QuickControls2 QuickControls2Impl QuickDialogs2 QuickDialogs2QuickImpl QuickDialogs2Utils QuickLayouts QuickParticles QuickShapes QuickTemplates2 QuickTest QuickWidgets QmlWorkerScript Qml QmlCore QmlModels QmlLocalStorage QmlMeta QmlXmlListModel QmlCompiler QuickEffects QmlNetwork QuickControls2BasicStyleImpl QuickControls2FluentWinUI3StyleImpl QuickControls2FusionStyleImpl QuickControls2ImagineStyleImpl QuickControls2MaterialStyleImpl QuickControls2UniversalStyleImpl QuickControls2Basic QuickControls2Fusion QuickControls2Imagine QuickControls2Material QuickControls2Universal QuickVectorImage QuickVectorImageGenerator LabsSynchronizer QuickVectorImageHelpers QuickShapesDesignHelpers
%qt6staticlibs QuickControlsTestUtils QuickTestUtils QmlDebug QmlDom PacketProtocol QmlTypeRegistrar QmlLS QmlToolingSettings QmlFormat QmlAssetDownloader

%package examples
Summary: Example applications for Qt Declarative %{qtmajor}
Group: Development/KDE and Qt

%description examples
Example applications for Qt Declarative %{qtmajor}

%files examples
%{_qtdir}/examples/qml
%{_qtdir}/examples/quick
%{_qtdir}/examples/quickcontrols
%optional %{_qtdir}/examples/quickshapes

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
	-DQT_WILL_INSTALL:BOOL=ON \
	-DBUILD_WITH_PCH:BOOL=OFF

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall
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
# FIXME circular dependency here... QtSvg wants QtQml, but
# QtQml needs QtSvg to build svgtoqml
%optional %{_qtdir}/bin/svgtoqml
%{_qtdir}/libexec/qmlaotstats
%{_qtdir}/libexec/qmlcachegen
%{_qtdir}/libexec/qmlimportscanner
%{_qtdir}/libexec/qmltyperegistrar
%{_qtdir}/plugins/qmlls
%{_qtdir}/plugins/qmllint
%{_qtdir}/qml/QML
