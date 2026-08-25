#define beta rc

Name:		qt6-qtdeclarative
Version:	6.11.2
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}2
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtdeclarative.git
Source:		qtdeclarative-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		https://download.qt.io/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtdeclarative-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
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
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Test)
#BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(Qt6LanguageServerPrivate)
#BuildRequires:	cmake(Qt6Location)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6JsonRpcPrivate)
BuildRequires:	cmake(Qt6ShaderTools) = %{version}
BuildRequires:	qt6-qtbase-tools
BuildRequires:	qmake-qt6
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	rpm-provreq-qml
License:	LGPLv3/GPLv3/GPLv2

%patchlist
# Disabling disk cache slows some things down (but not a lot),
# but seems to make everything a lot more stable (crashes last
# observed by ben with 6.10.0/Plasma 6.5.2)
# #6  0x00007f8e59b6625f _ZN21QmlCacheGeneratedCode57_qt_qml_org_kde_plasma_workspace_calendar_DayDelegate_qml4$_228__invokeEPKN11QQmlPrivate18AOTCompiledContextEPPv (libcalendarplugin.so + 0x7c25f)
qtdeclarative-disable-disk-cache.patch
# Disable the wearable example, because it requires QtPositioning
# (which in turn requires QtDeclarative first)
qtdeclarative-bootstrap.patch

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
%{_qtdir}/plugins/qmltooling/libqmldbg_quickeventreplay.so \
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
Requires:	%mklibname Qt%{qtmajor}QmlCore \
Provides:	cmake(Qt%{qtmajor}QmlIntegrationPrivate) = %{EVRD}

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
%{_qtdir}/bin/qmlls \
%{_qtdir}/bin/qmlcontextpropertydump \
%{_qtdir}/plugins/qmlls

%define extra_devel_files_QmlCore \
%{_qtdir}/libexec/qmljsrootgen

%define extra_files_QuickTest \
%{_qtdir}/qml/Qt/test

%define extra_devel_reqprov_Quick \
Requires:	cmake(Qt%{qtmajor}QmlMeta) \
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

%define extra_files_LabsSynchronizer \
%{_qtdir}/qml/Qt/labs/synchronizer/

%define extra_files_LabsStyleKit \
%{_qtdir}/qml/Qt/labs/StyleKit

%define extra_devel_reqprov_PacketProtocol \
Provides: cmake(Qt6PacketProtocolPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QmlDebug \
Provides: cmake(Qt6QmlDebugPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QmlDom \
Provides: cmake(Qt6QmlDomPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QmlFormat \
Provides: cmake(Qt6QmlFormatPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QmlTypeRegistrar \
Provides: cmake(Qt6QmlTypeRegistrarPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QmlToolingSettings \
Provides: cmake(Qt6QmlToolingSettingsPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QuickControls2ImagineStyleImpl \
Provides: cmake(Qt6QuickControls2ImagineStyleImplPrivate) = %{EVRD}

%define extra_devel_reqprov_QuickControlsTestUtils \
Provides: cmake(Qt6QuickControlsTestUtilsPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QuickParticles \
Provides: cmake(Qt6QuickParticlesPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QuickShapesDesignHelpers \
Provides: cmake(Qt6QuickShapesDesignHelpersPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QuickTestUtils \
Provides: cmake(Qt6QuickTestUtilsPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QuickVectorImageGenerator \
Provides: cmake(Qt6QuickVectorImageGeneratorPrivatePrivate) = %{EVRD}

%define extra_devel_reqprov_QmlLS \
Provides: cmake(Qt6QmlLSPrivatePrivate) = %{EVRD}

%qt6libs LabsAnimation LabsFolderListModel LabsPlatform LabsQmlModels LabsSettings LabsSharedImage LabsWavefrontMesh Quick QuickControls2 QuickControls2Impl QuickDialogs2 QuickDialogs2QuickImpl QuickDialogs2Utils QuickLayouts QuickParticles QuickShapes QuickTemplates2 QuickTest QuickWidgets QmlWorkerScript Qml QmlCore QmlModels QmlLocalStorage QmlMeta QmlXmlListModel QmlCompiler QuickEffects QmlNetwork QuickControls2BasicStyleImpl QuickControls2FluentWinUI3StyleImpl QuickControls2FusionStyleImpl QuickControls2ImagineStyleImpl QuickControls2MaterialStyleImpl QuickControls2UniversalStyleImpl QuickControls2Basic QuickControls2Fusion QuickControls2Imagine QuickControls2Material QuickControls2Universal QuickVectorImage QuickVectorImageGenerator LabsSynchronizer QuickVectorImageHelpers QuickShapesDesignHelpers LabsStyleKit LabsStyleKitImpl
%qt6staticlibs QuickControlsTestUtils QuickTestUtils QmlDebug QmlDom PacketProtocol QmlTypeRegistrar QmlLS QmlToolingSettings QmlFormat Qmltc

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

# Out-of-tree so %%pgo can wipe only this dir between passes.
%conf
export CMAKE_BUILD_DIR=_OMV_rpm_build
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
export LD_LIBRARY_PATH="$(pwd)/_OMV_rpm_build/lib:${LD_LIBRARY_PATH}"
export LLVM_PROFILE_FILE="%{_pgo_profile_dir}/qtdeclarative-%%m-%%p.profraw"
%ninja_build -C _OMV_rpm_build

# Training uses in-tree material only (no extra Source, no QT_BUILD_TESTS):
# tests/benchmarks/qml/deltablue (Qt's QML/JS constraint solver),
# tools/qmltime (item creation / loader / layout), examples, and the
# qmlformat/qmllint/qmlcachegen tools. Auto-tests stay off: they are
# huge and do not run reliably uninstalled/headless.
%pgo
set +e
export LLVM_PROFILE_FILE="%{_pgo_profile_dir}/qtdeclarative-%%m-%%p.profraw"

TOP="$PWD"
B="$TOP/_OMV_rpm_build"
QML="$B/bin/qml"
QMLFORMAT="$B/bin/qmlformat"
QMLLINT="$B/bin/qmllint"
QMLTIME="$B/bin/qmltime"
QMLCACHEGEN="$B/libexec/qmlcachegen"
QMLIMPORTSCANNER="$B/libexec/qmlimportscanner"
QMLDOM="$B/bin/qmldom"

if [ ! -x "$QML" ]; then
	echo "PGO: instrumented qml binary missing"
	exit 1
fi

export PATH="$B/bin:$B/libexec:$PATH"
export LD_LIBRARY_PATH="$B/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export QML2_IMPORT_PATH="$B/qml"
export QML_IMPORT_PATH="$B/qml"
export QT_PLUGIN_PATH="$B/plugins:${QT_PLUGIN_PATH:-%{_qtdir}/plugins}"
export QT_QPA_PLATFORM=offscreen
export QT_QUICK_BACKEND=software
export LIBGL_ALWAYS_SOFTWARE=1
# Disk cache is patched off; keep compilation on the hot path.
export QML_DISABLE_DISK_CACHE=1

try() {
	"$@"
	rc=$?
	if [ $rc -ne 0 ]; then
		echo "PGO: skipped (exit $rc): $*"
	fi
	return 0
}

WORKDIR="$TOP/pgo-train"
rm -rf "$WORKDIR"
mkdir -p "$WORKDIR"

# --- QML/JS engine: official DeltaBlue + extra JS (no GUI) ---
cat >"$WORKDIR/pgo-js.qml" <<'EOF'
import QtQml
import "deltablue.js" as DeltaBlue

QtObject {
	function fib(n) {
		if (n < 2)
			return n
		return fib(n - 1) + fib(n - 2)
	}
	function jsHotPath() {
		var acc = 0
		var arr = []
		var obj = {x: 1, y: 2, label: "pgo"}
		for (var i = 0; i < 2000; i++) {
			acc += (i * 3 + 7) %% 97
			arr.push(i)
			obj.x = obj.x + 1
			obj.y = obj.x * 0.5
			obj.label = "n" + i
		}
		arr.sort(function(a, b) { return b - a })
		var s = arr.slice(0, 50).join(",")
		var m = s.split(",").map(function(v) { return Number(v) + 1 })
		for (var k = 0; k < m.length; k++)
			acc += m[k]
		acc += fib(16)
		return acc
	}
	Component.onCompleted: {
		for (var i = 0; i < 8; i++)
			DeltaBlue.deltaBlue()
		for (var j = 0; j < 20; j++)
			jsHotPath()
		Qt.quit()
	}
}
EOF
ln -s "$TOP/tests/benchmarks/qml/deltablue/deltablue.js" "$WORKDIR/deltablue.js"
try timeout -k 2 60 "$QML" -a core "$WORKDIR/pgo-js.qml"

# --- Qt Quick + Controls: create, bind, lay out, animate, destroy ---
cat >"$WORKDIR/pgo-quick.qml" <<'EOF'
import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQml

Window {
	id: root
	width: 800
	height: 600
	visible: true
	title: "PGO"
	property int ticks: 0
	property real phase: 0
	property string label: "init"

	ListModel {
		id: items
		Component.onCompleted: {
			for (var i = 0; i < 120; i++)
				append({name: "Item " + i, value: i, on: (i %% 2) === 0})
		}
	}

	ColumnLayout {
		anchors.fill: parent
		spacing: 6
		RowLayout {
			Repeater {
				model: 8
				Button {
					text: "B" + index
					highlighted: index === (root.ticks %% 8)
					onClicked: root.ticks += 1
				}
			}
		}
		Slider { from: 0; to: 100; value: root.phase; Layout.fillWidth: true }
		ProgressBar { value: (root.ticks %% 100) / 100; Layout.fillWidth: true }
		TextField { text: "tick " + root.ticks + " " + root.label; Layout.fillWidth: true }
		Switch { checked: (root.ticks %% 2) === 0 }
		ComboBox { model: ["a", "b", "c", "d"]; currentIndex: root.ticks %% 4 }
		BusyIndicator { running: root.ticks < 160 }
		ListView {
			Layout.fillWidth: true
			Layout.fillHeight: true
			clip: true
			model: items
			delegate: RowLayout {
				required property string name
				required property int value
				required property bool on
				width: ListView.view.width
				Label { text: name; Layout.preferredWidth: 120 }
				Slider { value: value %% 100; from: 0; to: 100; Layout.fillWidth: true }
				Switch { checked: on }
			}
		}
	}

	Loader {
		id: extra
		sourceComponent: Rectangle {
			width: 40; height: 40
			color: Qt.hsla((root.phase %% 100) / 100, 0.6, 0.5, 1)
			Text { anchors.centerIn: parent; text: root.ticks }
		}
	}

	SequentialAnimation on phase {
		running: true
		loops: Animation.Infinite
		NumberAnimation { to: 100; duration: 400 }
		NumberAnimation { to: 0; duration: 400 }
	}

	Timer {
		interval: 16
		running: true
		repeat: true
		onTriggered: {
			root.ticks++
			root.label = "t" + root.ticks
			if (items.count)
				items.setProperty(root.ticks %% items.count, "value", root.ticks)
			if ((root.ticks %% 15) === 0)
				extra.active = !extra.active
			if (root.ticks >= 160)
				Qt.quit()
		}
	}
}
EOF
try timeout -k 2 30 "$QML" --software "$WORKDIR/pgo-quick.qml"

# --- qmltime: official item-creation / loader / layout microbenchmarks ---
if [ -x "$QMLTIME" ]; then
	find tools/qmltime -name '*.qml' ! -name 'Loaded.qml' | sort | while read -r f; do
		try timeout -k 2 45 "$QMLTIME" -iterations 256 -parent "$f"
	done
fi

# --- Tooling path (qmlcachegen/qmlformat/qmllint used by every QML build) ---
CORPUS="$WORKDIR/corpus.txt"
find examples tests/benchmarks tools/qmltime -name '*.qml' | sort | head -n 250 >"$CORPUS"
if [ -x "$QMLFORMAT" ]; then
	# First 80 files individually so the formatter stays hot
	head -n 80 "$CORPUS" | while read -r f; do
		try "$QMLFORMAT" "$f" >/dev/null
	done
fi
if [ -x "$QMLLINT" ]; then
	head -n 80 "$CORPUS" | while read -r f; do
		try "$QMLLINT" -I "$B/qml" --silent "$f"
	done
fi
if [ -x "$QMLCACHEGEN" ]; then
	i=0
	head -n 40 "$CORPUS" | while read -r f; do
		i=$((i + 1))
		try "$QMLCACHEGEN" --only-bytecode -I "$B/qml" -o "$WORKDIR/c$i.qmlc" "$f"
	done
fi
if [ -x "$QMLDOM" ]; then
	head -n 15 "$CORPUS" | while read -r f; do
		try "$QMLDOM" --dump "$f" >/dev/null
	done
fi
if [ -x "$QMLIMPORTSCANNER" ]; then
	try "$QMLIMPORTSCANNER" -rootPath examples -importPath "$B/qml"
fi

# --- Compiled examples (already built; short offscreen run) ---
find "$B/examples" -type f -executable ! -name '*.so*' ! -path '*/CMakeFiles/*' | sort | while read -r ex; do
	try timeout -k 2 4 "$ex"
done

rm -rf "$WORKDIR"
exit 0

%install
%ninja_install -C _OMV_rpm_build
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
%{_qtdir}/plugins/qmllint
%{_qtdir}/qml/QML
