#define beta rc2
#define snapshot 20200627
%define major 6

%define libqml %mklibname Qt%{major}Qml %{major}
%define devqml %mklibname -d Qt%{major}Qml
%define libqmlmodels %mklibname Qt%{major}QmlModels %{major}
%define devqmlmodels %mklibname -d Qt%{major}QmlModels
%define libqmlworkerscript %mklibname Qt%{major}QmlWorkerScript %{major}
%define devqmlworkerscript %mklibname -d Qt%{major}QmlWorkerScript
%define liblabsfolderlistmodel %mklibname Qt%{major}LabsFolderListModel %{major}
%define devlabsfolderlistmodel %mklibname -d Qt%{major}LabsFolderListModel
%define liblabsqmlmodels %mklibname Qt%{major}LabsQmlModels %{major}
%define devlabsqmlmodels %mklibname -d Qt%{major}LabsQmlModels
%define liblabssettings %mklibname Qt%{major}LabsSettings %{major}
%define devlabssettings %mklibname -d Qt%{major}LabsSettings
%define libqmlcore %mklibname Qt%{major}QmlCore %{major}
%define devqmlcore %mklibname -d Qt%{major}QmlCore
%define libqmllocalstorage %mklibname Qt%{major}QmlLocalStorage %{major}
%define devqmllocalstorage %mklibname -d Qt%{major}QmlLocalStorage
%define libqmlxmllistmodel %mklibname Qt%{major}QmlXmlListModel %{major}
%define devqmlxmllistmodel %mklibname -d Qt%{major}QmlXmlListModel

%define _qtdir %{_libdir}/qt%{major}

Name:		qt6-qtdeclarative
Version:	6.2.1
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
BuildRequires:	qt%{major}-cmake
BuildRequires:	%{_lib}Qt%{major}Concurrent-devel
BuildRequires:	%{_lib}Qt%{major}Core-devel
BuildRequires:	%{_lib}Qt%{major}Gui-devel
BuildRequires:	%{_lib}Qt%{major}Widgets-devel
BuildRequires:	%{_lib}Qt%{major}Network-devel
BuildRequires:	%{_lib}Qt%{major}OpenGL-devel
BuildRequires:	%{_lib}Qt%{major}OpenGLWidgets-devel
BuildRequires:	%{_lib}Qt%{major}Sql-devel
BuildRequires:	%{_lib}Qt%{major}Test-devel
BuildRequires:	qt%{major}-qtbase-tools
BuildRequires:	qmake-qt%{major}
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	rpm-provreq-qml
License:	LGPLv3/GPLv3/GPLv2

%description
Version %{major} of the Qt Quick framework

%define libs LabsAnimation LabsSharedImage LabsWavefrontMesh Quick QuickControls2 QuickControls2Impl QuickDialogs2 QuickDialogs2QuickImpl QuickDialogs2Utils QuickLayouts QuickParticles QuickShapes QuickTemplates2 QuickTest QuickWidgets QmlWorkerScript QmlModels
%define staticlibs QuickControlsTestUtils QuickTestUtils QmlDebug PacketProtocol QmlDevTools QmlDom
%{expand:%(for lib in %{libs}; do
	cat <<EOF
%%global lib${lib} %%mklibname Qt%{major}${lib} %{major}
%%global dev${lib} %%mklibname -d Qt%{major}${lib}
%%package -n %%{lib${lib}}
Summary: Qt %{major} ${lib} library
Group: System/Libraries

%%description -n %%{lib${lib}}
Qt %{major} ${lib} library

%%files -n %%{lib${lib}}
%{_qtdir}/lib/libQt%{major}${lib}.so.*
%{_libdir}/libQt%{major}${lib}.so.*

%%package -n %%{dev${lib}}
Summary: Development files for the Qt %{major} ${lib} library
Requires: %%{lib${lib}} = %{EVRD}
Group: Development/KDE and Qt

%%description -n %%{dev${lib}}
Development files for the Qt %{major} ${lib} library

%%files -n %%{dev${lib}}
%{_qtdir}/lib/libQt%{major}${lib}.so
%{_libdir}/libQt%{major}${lib}.so
%{_qtdir}/lib/libQt%{major}${lib}.prl
%{_qtdir}/include/Qt${lib}
%optional %{_qtdir}/modules/${lib}.json
%optional %{_qtdir}/modules/${lib}Private.json
%optional %{_libdir}/cmake/Qt%{major}${lib}
%optional %{_libdir}/cmake/Qt%{major}${lib}Private
%optional %{_qtdir}/lib/metatypes/qt%{major}$(echo ${lib}|tr A-Z a-z)_relwithdebinfo_metatypes.json
%optional %{_qtdir}/lib/metatypes/qt%{major}$(echo ${lib}|tr A-Z a-z)private_relwithdebinfo_metatypes.json
%optional %{_qtdir}/mkspecs/modules/qt_lib_$(echo ${lib}|tr A-Z a-z).pri
%optional %{_qtdir}/mkspecs/modules/qt_lib_$(echo ${lib}|tr A-Z a-z)_private.pri
EOF
done)}
%{expand:%(for lib in %{staticlibs}; do
	cat <<EOF
%%global dev${lib} %%mklibname -d Qt%{major}${lib}
%%package -n %%{dev${lib}}
Summary: Static libraries for the Qt %{major} ${lib} library
Group: Development/KDE and Qt

%%description -n %%{dev${lib}}
Static libraries files for the Qt %{major} ${lib} library

%%files -n %%{dev${lib}}
%{_qtdir}/lib/libQt%{major}${lib}.a
%{_libdir}/libQt%{major}${lib}.a
%{_qtdir}/lib/libQt%{major}${lib}.prl
%optional %{_qtdir}/include/Qt${lib}
%optional %{_qtdir}/modules/${lib}.json
%optional %{_qtdir}/modules/${lib}Private.json
%optional %{_libdir}/cmake/Qt%{major}${lib}
%optional %{_libdir}/cmake/Qt%{major}${lib}Private
%optional %{_qtdir}/lib/metatypes/qt%{major}$(echo ${lib}|tr A-Z a-z)_relwithdebinfo_metatypes.json
%optional %{_qtdir}/lib/metatypes/qt%{major}$(echo ${lib}|tr A-Z a-z)private_relwithdebinfo_metatypes.json
%optional %{_qtdir}/mkspecs/modules/qt_lib_$(echo ${lib}|tr A-Z a-z).pri
%optional %{_qtdir}/mkspecs/modules/qt_lib_$(echo ${lib}|tr A-Z a-z)_private.pri
%optional %{_qtdir}/mkspecs/modules/qt_lib_$(echo ${lib}|tr A-Z a-z)private_private.pri
EOF
done)}

%package -n %{libqml}
Summary:	Qt %{major} Qml library
Group:		System/Libraries

%description -n %{libqml}
Qt %{major} Qml library

%files -n %{libqml}
%{_libdir}/libQt%{major}Qml.so.%{major}*
%{_qtdir}/lib/libQt%{major}Qml.so.%{major}*
%{_qtdir}/plugins/qmltooling
%dir %{_qtdir}/qml/Qt
%dir %{_qtdir}/qml/Qt/labs
%{_qtdir}/qml/Qt/labs/animation
%{_qtdir}/qml/Qt/labs/platform
%{_qtdir}/qml/Qt/labs/sharedimage
%{_qtdir}/qml/Qt/labs/wavefrontmesh
%{_qtdir}/qml/QtTest

%package -n %{devqml}
Summary:	Development files for the Qt %{major} Qml library
Group:		Development/KDE and Qt
Requires:	%{libqml} = %{EVRD}
# Make sure dependencies are generated correctly
Requires:	rpm-provreq-qml

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

%{_qtdir}/include/QtQuick
%{_qtdir}/include/QtQuickTemplates2

%{_libdir}/cmake/Qt%{major}BuildInternals

%{_libdir}/cmake/Qt%{major}QmlTools
%{_libdir}/cmake/Qt%{major}QmlDebugPrivate

%{_qtdir}/lib/metatypes/qt%{major}qml_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlmodels_relwithdebinfo_metatypes.json
%{_qtdir}/lib/metatypes/qt%{major}qmlworkerscript_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_qml.pri
%{_qtdir}/mkspecs/modules/qt_lib_qml_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmltest.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmltest_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlmodels.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlmodels_private.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlworkerscript.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlworkerscript_private.pri
%{_qtdir}/plugins/qmltooling/libqmldbg_debugger.so
%{_qtdir}/plugins/qmltooling/libqmldbg_local.so
%{_qtdir}/plugins/qmltooling/libqmldbg_messages.so
%{_qtdir}/plugins/qmltooling/libqmldbg_native.so
%{_qtdir}/plugins/qmltooling/libqmldbg_nativedebugger.so
%{_qtdir}/plugins/qmltooling/libqmldbg_profiler.so
%{_qtdir}/plugins/qmltooling/libqmldbg_server.so
%{_qtdir}/plugins/qmltooling/libqmldbg_tcp.so
%{_qtdir}/qml/Qt/labs/folderlistmodel
%{_qtdir}/qml/Qt/labs/qmlmodels
%{_qtdir}/qml/Qt/labs/settings
%{_qtdir}/qml/builtins.qmltypes

%{_libdir}/cmake/Qt%{major}QmlCompilerPrivate
%{_qtdir}/modules/QmlCompilerPrivate.json
%{_qtdir}/modules/QmlDebugPrivate.json
%{_libdir}/cmake/Qt%{major}QmlImportScanner
%{_libdir}/libQt%{major}QmlCompiler.a
%{_qtdir}/include/QtQmlCompiler
%{_qtdir}/lib/libQt%{major}QmlCompiler.a
%{_qtdir}/lib/libQt%{major}QmlCompiler.prl
%{_qtdir}/mkspecs/features/qtquickcompiler.prf
%{_qtdir}/mkspecs/features/qmlcache.prf
%{_qtdir}/mkspecs/features/qmltypes.prf
%{_qtdir}/mkspecs/modules/qt_lib_qmlcompiler_private.pri
%{_qtdir}/lib/metatypes/qt%{major}qmlcompilerprivate_relwithdebinfo_metatypes.json

%package examples
Summary: Example applications for Qt Declarative %{major}
Group: Development/KDE and Qt

%description examples
Example applications for Qt Declarative %{major}

%files examples
%{_qtdir}/examples/qml
%{_qtdir}/examples/quick
%{_qtdir}/examples/quickcontrols2
%{_qtdir}/examples/tst_qmltestexample

%package devel
Summary: Metapackage pulling in the development files for %{name} and all subcomponents
Group: Development/KDE and Qt
Requires: %{expand:%(for lib in %{libs}; do echo -n "%%{dev${lib}} = %{EVRD} "; done)}
Requires: %{expand:%(for lib in %{staticlibs}; do echo -n "%%{dev${lib}} = %{EVRD} "; done)}
Requires: %{devqml} = %{EVRD}

%description devel
Metapackage pulling in the development files for %{name} and all subcomponents

%files devel

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
rm -f %{buildroot}%{_qtdir}/%{_lib}/libpnp_basictools.a
# Put stuff where tools will find it
# We can't do the same for %{_includedir} right now because that would
# clash with qt5 (both would want to have /usr/include/QtCore and friends)
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_libdir}/cmake
for i in %{buildroot}%{_qtdir}/lib/*.so* %{buildroot}%{_qtdir}/lib/*.a; do
	ln -s qt%{major}/lib/$(basename ${i}) %{buildroot}%{_libdir}/
done
mv %{buildroot}%{_qtdir}/lib/cmake %{buildroot}%{_libdir}/

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


%package -n %{liblabsfolderlistmodel}
Summary:	Qt %{major} folder list model library
Group:		System/Libraries

%description -n %{liblabsfolderlistmodel}
Qt %{major} folder list model library

%files -n %{liblabsfolderlistmodel}
%{_libdir}/libQt%{major}LabsFolderListModel.so.%{major}*
%{_qtdir}/lib/libQt%{major}LabsFolderListModel.so.%{major}*

%package -n %{devlabsfolderlistmodel}
Summary:	Development files for the Qt %{major} folder list model library
Group:		Development/KDE and Qt
Requires:	%{liblabsfolderlistmodel} = %{EVRD}

%description -n %{devlabsfolderlistmodel}
Development files for the Qt %{major} folder list model library

%files -n %{devlabsfolderlistmodel}
%{_libdir}/cmake/Qt%{major}LabsFolderListModel
%{_libdir}/libQt%{major}LabsFolderListModel.so
%{_qtdir}/include/QtLabsFolderListModel
%{_qtdir}/lib/libQt%{major}LabsFolderListModel.prl
%{_qtdir}/lib/libQt%{major}LabsFolderListModel.so
%{_qtdir}/lib/metatypes/qt%{major}labsfolderlistmodel_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_labsfolderlistmodel.pri
%{_qtdir}/mkspecs/modules/qt_lib_labsfolderlistmodel_private.pri
%{_qtdir}/modules/LabsFolderListModel.json

%package -n %{liblabsqmlmodels}
Summary:	Qt %{major} QML models library
Group:		System/Libraries

%description -n %{liblabsqmlmodels}
Qt %{major} QML models library

%files -n %{liblabsqmlmodels}
%{_libdir}/libQt%{major}LabsQmlModels.so.%{major}*
%{_qtdir}/lib/libQt%{major}LabsQmlModels.so.%{major}*

%package -n %{devlabsqmlmodels}
Summary:	Development files for the Qt %{major} QML Models library
Group:		Development/KDE and Qt
Requires:	%{liblabsqmlmodels} = %{EVRD}

%description -n %{devlabsqmlmodels}
Development files for the Qt %{major} QML Models library

%files -n %{devlabsqmlmodels}
%{_libdir}/cmake/Qt%{major}LabsQmlModels
%{_libdir}/libQt%{major}LabsQmlModels.so
%{_qtdir}/include/QtLabsQmlModels
%{_qtdir}/lib/libQt%{major}LabsQmlModels.prl
%{_qtdir}/lib/libQt%{major}LabsQmlModels.so
%{_qtdir}/lib/metatypes/qt%{major}labsqmlmodels_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_labsqmlmodels.pri
%{_qtdir}/mkspecs/modules/qt_lib_labsqmlmodels_private.pri
%{_qtdir}/modules/LabsQmlModels.json

%package -n %{liblabssettings}
Summary:	Qt %{major} Settings library
Group:		System/Libraries

%description -n %{liblabssettings}
Qt %{major} Settings library

%files -n %{liblabssettings}
%{_libdir}/libQt%{major}LabsSettings.so.%{major}*
%{_qtdir}/lib/libQt%{major}LabsSettings.so.%{major}*

%package -n %{devlabssettings}
Summary:	Development files for the Qt %{major} settings library
Group:		Development/KDE and Qt
Requires:	%{liblabssettings} = %{EVRD}

%description -n %{devlabssettings}
Development files for the Qt %{major} settings library

%files -n %{devlabssettings}
%{_libdir}/libQt%{major}LabsSettings.so
%{_libdir}/cmake/Qt%{major}LabsSettings
%{_qtdir}/include/QtLabsSettings
%{_qtdir}/lib/libQt%{major}LabsSettings.prl
%{_qtdir}/lib/libQt%{major}LabsSettings.so
%{_qtdir}/lib/metatypes/qt%{major}labssettings_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_labssettings.pri
%{_qtdir}/mkspecs/modules/qt_lib_labssettings_private.pri
%{_qtdir}/modules/LabsSettings.json

%define libqmllocalstorage %mklibname Qt%{major}QmlLocalStorage %{major}
%define devqmllocalstorage %mklibname -d Qt%{major}QmlLocalStorage
%define libqmlxmllistmodel %mklibname Qt%{major}QmlXmlListModel %{major}
%define devqmlxmllistmodel %mklibname -d Qt%{major}QmlXmlListModel

%package -n %{libqmlcore}
Summary:	Qt %{major} QML Core library
Group:		System/Libraries

%description -n %{libqmlcore}
Qt %{major} QML Core library

%files -n %{libqmlcore}
%{_libdir}/libQt%{major}QmlCore.so.%{major}*
%{_qtdir}/lib/libQt%{major}QmlCore.so.%{major}*
%dir %{_qtdir}/qml
%{_qtdir}/qml/QtCore
%{_qtdir}/qml/QtQuick
%{_qtdir}/qml/jsroot.qmltypes


%package -n %{devqmlcore}
Summary:	Development files for the Qt %{major} QML Core library
Group:		Development/KDE and Qt
Requires:	%{libqmlcore} = %{EVRD}

%description -n %{devqmlcore}
Development files for the Qt %{major} QML Core library

%files -n %{devqmlcore}
%{_libdir}/cmake/Qt%{major}QmlCore
%{_libdir}/libQt%{major}QmlCore.so
%{_qtdir}/include/QtQmlCore
%{_qtdir}/lib/libQt%{major}QmlCore.prl
%{_qtdir}/lib/libQt%{major}QmlCore.so
%{_qtdir}/modules/QmlCore.json
%{_qtdir}/lib/metatypes/qt%{major}qmlcore_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_qmlcore.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlcore_private.pri

%package -n %{libqmllocalstorage}
Summary:	Qt %{major} QML Local Storage library
Group:		System/Libraries

%description -n %{libqmllocalstorage}
Qt %{major} QML Local Storage library

%files -n %{libqmllocalstorage}
%{_libdir}/libQt%{major}QmlLocalStorage.so.%{major}*
%{_qtdir}/lib/libQt%{major}QmlLocalStorage.so.%{major}*

%package -n %{devqmllocalstorage}
Summary:	Development files for the Qt %{major} QML Local Storage library
Group:		Development/KDE and Qt
Requires:	%{libqmllocalstorage} = %{EVRD}

%description -n %{devqmllocalstorage}
Development files for the Qt %{major} QML Local Storage library

%files -n %{devqmllocalstorage}
%{_libdir}/cmake/Qt%{major}QmlLocalStorage
%{_libdir}/libQt%{major}QmlLocalStorage.so
%{_qtdir}/include/QtQmlLocalStorage
%{_qtdir}/lib/libQt%{major}QmlLocalStorage.prl
%{_qtdir}/lib/libQt%{major}QmlLocalStorage.so
%{_qtdir}/lib/metatypes/qt%{major}qmllocalstorage_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_qmllocalstorage.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmllocalstorage_private.pri
%{_qtdir}/modules/QmlLocalStorage.json

%package -n %{libqmlxmllistmodel}
Summary:	Qt %{major} QML XML List Model library
Group:		System/Libraries

%description -n %{libqmlxmllistmodel}
Qt %{major} QML XML List Model library

%files -n %{libqmlxmllistmodel}
%{_libdir}/libQt%{major}QmlXmlListModel.so.%{major}*
%{_qtdir}/lib/libQt%{major}QmlXmlListModel.so.%{major}*

%package -n %{devqmlxmllistmodel}
Summary:	Development files for the Qt %{major} QML XML List Model library
Group:		Development/KDE and Qt
Requires:	%{libqmlxmllistmodel} = %{EVRD}

%description -n %{devqmlxmllistmodel}
Development files for the Qt %{major} QML XML List Model library

%files -n %{devqmlxmllistmodel}
%{_libdir}/cmake/Qt%{major}QmlXmlListModel
%{_libdir}/libQt%{major}QmlXmlListModel.so
%{_qtdir}/include/QtQmlXmlListModel
%{_qtdir}/lib/libQt%{major}QmlXmlListModel.prl
%{_qtdir}/lib/libQt%{major}QmlXmlListModel.so
%{_qtdir}/lib/metatypes/qt%{major}qmlxmllistmodel_relwithdebinfo_metatypes.json
%{_qtdir}/mkspecs/modules/qt_lib_qmlxmllistmodel.pri
%{_qtdir}/mkspecs/modules/qt_lib_qmlxmllistmodel_private.pri
%{_qtdir}/modules/QmlXmlListModel.json
