#define beta rc

Name:		qt6-qtdeclarative
Version:	6.10.0
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

%patchlist
# This is a workaround for the disk cache breaking Plasma badly.
# See e.g. https://www.reddit.com/r/kde/comments/18n3bfb/comment/keja252/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
# This is fixed, but let's leave the patch here for reference, this may happen again
# when the on-disk format changes
#qtdeclarative-disable-disk-cache.patch

# From upstream
0002-QmlModels-De-bounce-model-data-if-DelegateModelAcces.patch
0003-QQmlDelegateModel-De-bounce-initialization-of-two-wa.patch
0004-CMake-Work-around-looking-for-Qt-packages-in-in-tree.patch
0005-QtQuick-Don-t-store-a-copy-of-the-model-in-QQuickIte.patch
0006-mac-style-fall-back-to-draw-ProgressBar-manually-on-.patch
0007-QtQuick-Drop-redundant-members-from-QQuickRepeater.patch
0008-QtQml-Don-t-store-redundant-model-data-in-QQmlInstan.patch
0010-Scenegraph-baseline-test-Some-improvements-to-shape-.patch
0012-Fusion-give-TextArea-a-background.patch
0013-qml-compiler-avoid-interface-as-var-parameter-name.patch
0014-qmltyperegistrar-add-line-numbers-to-methods-propert.patch
0016-QQmlDelegateModel-Drop-FINAL-from-some-properties.patch
0017-QtQml-Avoid-double-wrapping-when-converting-to-QVari.patch
0018-Move-qqmlsortfilterproxymodel-private-class-to-a-sep.patch
0022-Gallery-example-Brush-up-the-.cpp-file.patch
0023-tst_QQuickPopup-fadeDimmer-fix-stack-use-after-scope.patch
0024-Unblacklist-tst_QQuickPopup-zOrder-on-macOS.patch
0025-Unblacklist-a-few-tst_QQuickPopup-tests-on-macOS.patch
0026-QmlModels-Test-model-writing-behavior-of-delegates.patch
0027-Release-section-item-when-the-corresponding-view-ite.patch
0028-QtQml-Empty-SimpleArrayData-vacant-space-when-trunca.patch
0030-QtQuick-Simplify-TableView-model-handling.patch
0031-Properly-wire-up-DelegateModel-s-modelChanged-signal.patch
0032-QmlCompiler-Guard-against-disappearing-arrow-functio.patch
0033-QQ4A-Reduce-amount-of-spam-calls-in-tst_signallisten.patch
0034-QQuickTableView-Expose-internal-model-changes-via-th.patch
0035-QmlModels-Signal-list-model-changes-also-via-QQmlTab.patch
0037-CRA-review-src-core.patch
0038-Add-security-header-for-src-qmlformat.patch
0039-Add-security-header-for-src-qmldom.patch
0040-QtQml-Unregister-QML-animation-timer-on-deletion.patch
0041-Add-security-header-for-src-qmlcompiler.patch
0042-Docs-Correct-the-type-of-the-ValueFilter-value-prope.patch
0043-Make-security-header-for-the-qt-labs-folderlistmodel.patch
0044-vectorimage-Add-dependency-on-QtQuick.Shapes.patch
0045-Fix-Android-deployment-of-VectorImage-plugins.patch
0046-Doc-Qt-Qml-Models-Fix-documentation-issues.patch
0047-Mark-security-header-for-the-qt-labs-platform.patch
0048-QML-Preserve-return-type-annotation-for-function-exp.patch
0049-CRA-review-Mark-qmlintegration-as-insignificant.patch
0050-Mark-security-header-for-qt-labs-animation.patch
0051-CRA-review-mark-qml-qmlmeta-subfolder.patch
0052-Add-security-header-for-src-qmlmodels.patch
0053-CRA-review-qml-jsruntime.patch
0054-CRA-review-mark-workerscript-subfolder.patch
0055-Mark-security-criticality-for-most-files-in-qml-pars.patch
0056-Assess-security-levels-for-files-under-qtdeclarative.patch
0057-CRA-review-src-plugins-qmllint-and-src-plugins-qmlls.patch
0058-QmlCompiler-Properly-handle-uncertain-component-stat.patch
0059-CRA-review-src-qmlls.patch
0060-Include-qqmlglobal_p.h-in-tst_qmltyperegistrar.cpp-t.patch
0062-Doc-Add-QML-docs-for-Window-startSystemMove-and-star.patch
0063-Mark-security-header-for-the-qt-labs-synchronizer.patch
0064-qmlformat-Fix-ScriptFormatter-for-blocks-statements-.patch
0065-Give-ownership-to-qml-instead-of-deleting-the-object.patch
0066-QtQml-Fix-initialization-of-non-optional-static-plug.patch
0067-sg-remove-an-unused-variable-in-QSGMaterialShaderPri.patch
0068-QmlCompiler-Don-t-adjust-the-same-conversion-multipl.patch
0069-Mark-security-header-for-the-qt-labs-sharedimage.patch
0070-Skip-tst_QQuickFramebufferObject-if-OpenGL-is-not-av.patch
0071-Mark-security-header-for-the-qt-labs-wavefrontmesh.patch
0073-FluentWinUI3-Fix-text-color-of-RoundButton-for-high-.patch
0074-Synchronizer-Add-a-note-about-using-it-with-singleto.patch
0075-qmllint-Consider-on-bindings-for-required-properties.patch
0077-mac-style-update-Slider-and-RangeSlider.patch
0078-Native-Style-simplify-implementation-of-QQuickNative.patch
0079-Tests-gifs-include-missing-header.patch
0080-Mark-security-header-for-the-qt-labs-settings.patch
0081-Mark-security-header-for-the-qt-labs-models.patch
0082-SearchField-Update-SortFilterProxyModel-in-docs.patch
0083-qml-silence-clang-21-warnings.patch
0084-tests-silence-some-clang-warnings.patch
0088-FileDialog-Comply-with-accessibility-insights-for-Wi.patch
0089-FontDialogContent-Comply-with-accessibility-insights.patch
0090-QQuickStyle-Be-smarter-about-detecting-if-a-theme-is.patch
0091-ColorDialog-Comply-with-accessibility-insights-for-W.patch
0092-Menu-prioritize-parentItem-s-window-as-transient-par.patch
0093-deliverHoverEventRecursive-don-t-crash-if-a-child-di.patch
0094-Replace-nokia.com-logo-URLs-with-something-that-work.patch
0095-qmlformat-fix-incorrect-indent.patch
0096-cmake-use-QT_NAMESPACE-property.patch
0097-Doc-Remove-misleading-example-about-alias-overriding.patch
0098-QQmlJSUtils-resourceFilesFromBuildFolders-port-to-QD.patch
0099-Fix-flaky-tst_QQuickWidget-focusOnClickInProxyWidget.patch
0100-Account-for-safe-margins-in-scenegraph-vulkan-exampl.patch
0101-Initialize-QQuickGradientStop-position-to-zero.patch
0103-Avoid-showing-content-beneath-status-bars-in-wearabl.patch
0104-SpinBox-accept-touch-events.patch
0105-QtQml-Clear-cached-value-type-instances-when-clearin.patch
0106-qmlls.ini-generation-check-parent-build-dir-before-w.patch
0107-Doc-add-links-to-the-QQuickWidget-examples-to-the-su.patch
0109-Revert-QML-generator-optimize-by-sharing-custom-easi.patch
0110-SearchField-Keep-currentIndex-at-1-until-user-explic.patch
0111-qmlformat-format-type-annotations.patch
0112-qmlformat-format-list-type-annotations.patch
0113-qmlformat-format-return-type-annotations.patch
0114-QQuickRhiItem-docs-follow-QRhiWidget-docs-wrt-fixed-.patch
0115-Set-explicit-default-security-level-of-all-files-wit.patch
0116-Doc-Add-links-to-Qt-Academy-courses.patch
0117-Add-some-test-cases-to-test-the-setData-methods-in-Q.patch
0118-Fix-IME-selection-cursor-update.patch
0120-Doc-Add-Qt-Academy-course-links-to-documentation.patch
0121-ScrollView-use-padding-if-no-rightPadding-or-bottomP.patch
0122-Import-QtQuick-in-Imagine-FileDialogDelegate.qml.patch
0123-QtQml-Add-test-for-writing-to-delayed-properties.patch
0124-Doc-Fix-broken-links-in-Qt-Qml.patch
0125-Doc-Fix-API-names-in-Enumeration-key-string-key-valu.patch
0126-Doc-Remove-a-duplicate-item-from-TOC.patch
0127-QQuickPane-disconnect-signals-in-destructor.patch
0128-QmlCompiler-Fix-write-access-to-QVariantMap.patch
0129-Doc-Resolve-documentation-build-warnings.patch
0130-QQuickMacStyle-tweak-NSTextFieldCell-s-drawing.patch
0132-Fusion-Button-RoundButton-bind-icon.color-to-a-palet.patch
0133-QmlCompiler-Expect-singleton-members-to-be-shadowabl.patch
0134-Be-explicit-about-type-conversion-for-QString-args.patch
0135-Assert-that-overlay-isn-t-null.patch
0136-QtQml-Reset-scope-object-call-lookup-if-it-fails.patch
0137-QtQml-Don-t-allocate-empty-arrays-of-ID-values.patch
0138-Tooling-Also-clear-singletons-when-resetting-preview.patch
0139-test-Check-that-VectorImage-is-able-to-load-SVG-file.patch
0140-Docs-fix-missing-SpinBox-control.patch
0141-FluentWinUI3-Fix-ComboBox-size-when-the-model-change.patch
0143-CRA-Review-qmltoolingsettings.patch
0144-Skip-tst_QQuickColorDialogImpl-dialogCanMoveBetweenW.patch
0145-QtQml-Fix-assigning-to-QML-defined-list-properties.patch
0146-QtQml-Fix-resolution-of-aliases-to-local-aliases.patch
0147-QtQml-Support-trailing-comma-in-list-properties.patch
0148-qmltc-Fix-context-assignment.patch
0149-QtQml-Use-QQmlStringConverters-to-create-QColor-from.patch
0150-CMake-Fix-tst_qmlls_modules-installation.patch
0151-software-backend-Fix-clipped-text-styles.patch
0152-testhttpserver-support-upper-case-and-lower-case-hea.patch
0153-XmlHttpRequest-Don-t-treat-content-related-errors-as.patch
0154-MaterialStyle-Fix-early-out-conditions-for-backgroun.patch
0155-Qt.rgba-use-qBound-to-avoid-asserts.patch
0156-doc-fix-qmltypes-description-its-QML-not-JSON.patch
0157-tst_styleimports-make-attachedTypesAvailable-use-bui.patch
0158-QQuickShaderEffectSource-Don-t-cut-off-bottom-row-of.patch
0159-tst_qquickhoverhandler-asProperty-remove-redundant-c.patch
0160-quickcontrols-material-style-postpone-updating-qsgno.patch
0161-MaterialStyle-Fix-reset-behavior-for-foreground-and-.patch
0162-Avoid-duplicate-item-insertion-during-parent-expansi.patch
0163-Value-tpyes-improve-conversion-warnings.patch
0164-CRA-Review-local-storage.patch
0165-Extending-QML-Clarify-the-need-for-qmldir-files-with.patch
0166-CMake-Add-plugin-options-to-qt_generate_deploy_qml_a.patch
0167-ScrollBar-test_flashing-Use-non-interactive-scrollba.patch
0168-IntValidator-docs-Provide-guidance-on-intermediate-r.patch
0169-CanvasImageData-Track-image-data-size-for-gc-purpose.patch
0170-Provide-effective-size-policy-of-Layout-in-its-attac.patch
0171-Fix-writing-undefined-via-QQmlProperty.patch
0172-VectorImage-Fix-offset-transformation-of-use-nodes.patch
0173-Flat-Style-example-Split-CMake-project-into-multiple.patch
0174-qmlhighlighter-get-rid-of-redundant-class.patch
0175-qmlhighlighter-use-more-expressive-class-name.patch
0176-qmlhighlighting-wrap-semantic-highlighting-logic-in-.patch
0177-qmlhighlighting-refactor-for-reusability.patch
0178-style-remove-indentation-in-namespace.patch
0179-TextInput-don-t-clobber-text-cursor-visible-state.patch
0180-Compiler-Actually-read-the-value-of-a-key-passed-to-.patch
0181-Android-skip-test-cases-failing-to-acquire-deadlock-.patch
0182-Native-Style-rework-style-and-focus-window-initializ.patch
0183-QQuickOverlay-translate-touch-events-that-circumvent.patch
0184-Software-Adaptation-Disable-partial-updates-when-fra.patch
0185-Set-default-stack-size-safety-margin-for-VxWorks.patch
0186-Add-QT_QML_DEBUG-compile-definition-to-the-Qt6-Qml-t.patch
0187-Make-QQuickPopupPrivate-handleTouchEvent-use-QEventP.patch
0188-tst_HoverHandler-touchDrag-QCOMPARE-QPoint-QPoint.patch
0189-qmllint-Fix-typo-in-assignmentInCondition-warning.patch
0190-tst_qqmlecmascript-add-data-test-for-date-parsing.patch
0191-qmllint-prefer-enums-over-chained-attached-type.patch
0192-doc-remove-c-in-brief-of-QT_QML_GENERATE_QMLLS_INI_N.patch
0193-V4-Date-Support-more-nonstandard-date-formats.patch
0195-Android-fix-QtQuickView-fields-access-level.patch
0196-Ensure-that-the-right-grid-at-least-have-one-column.patch
0197-Compiler-Avoid-generating-duplicate-settings-names.patch
0198-Doc-use-registerModule-in-Use-a-C-enum-in-JavaScript.patch
0199-Adapt-to-reuse-version-6.patch
0200-Android-update-Qt-Quick-for-Android-examples-to-SDK-.patch
0201-Doc-Fix-formatting-in-the-List-of-JavaScript-functio.patch
0203-doc-Fix-mention-of-DragHandler-in-TapHandler-docs.patch
0204-ProgressBar-ensure-the-groove-resepect-the-width-of-.patch
0205-Slider-RangeSlider-ensure-empty-groove-has-the-corre.patch
0206-Android-don-t-use-quotes-with-QUICK_FOR_ANDROID_TEST.patch
0208-Software-Renderer-Fix-artifacts-with-non-pixel-align.patch
0209-QQmlDelegateModel-Don-t-try-to-destroy-nullptr-objec.patch
0210-QmlModels-Always-produce-valid-context-for-functions.patch
0211-QQmlDebugTranslationService-work-around-GCC-bug-std-.patch
0212-SpinBox-macOS-make-the-stepper-smaller.patch
0213-rendercontrol-test-Skip-when-format-is-not-supported.patch
0214-qmllint-Augment-the-import-warning-for-unspecialized.patch
0215-qmlls-support-relative-import-paths-just-like-qmllin.patch
0216-qmllint-load-different-import-paths-from-setting-fil.patch
0217-Allow-text-edit-to-process-key-events-when-shortcuto.patch
0218-doc-remove-hints-to-QT_QML_GENERATE_QMLLS_INI.patch
0219-qmlformat-Group-pure-formatting-and-tool-behavior-op.patch
0220-QQmlProperty-Handle-reset-for-object-properties-too.patch
0221-Propagate-attached-properties-for-items-within-the-p.patch
0222-qmlls-don-t-warn-about-QT_QML_GENERATE_QMLLS_INI-any.patch
0223-Examples-Stop-using-version-numbers-with-QML-modules.patch
0224-QQmlValueTypeWrapper-Mark-as-dirty-if-gadgetPtr-goes.patch
0226-Doc-Remove-Details-link-from-qmlformat-documentation.patch
0227-QtQml-Adapt-to-restructuring-of-QUnicodeTables.patch
0228-Doc-Revise-File-System-Explorer-example.patch
0229-Doc-Fix-qml-lint-binding-warnings.patch
0231-Dial-test_integerStepping-ensure-we-actually-test-ch.patch
0232-tst_objectcount-tidy-up-code.patch
0233-tst_creationtime-tidy-up-code.patch
0234-Doc-Fix-link-to-QJSEngine-uiLanguage.patch
0235-QQuickTextEdit-a11y-Allow-modifying-text-selection-v.patch
0236-QmlCompiler-Fix-side-effect-detection-for-calls.patch
0237-Doc-Qml-Compiler-Fix-internal-documentation-issues.patch
0238-Rich-text-Limit-size-of-text-object.patch
0239-Increase-robustness-of-img-tag-in-Text-component.patch

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
