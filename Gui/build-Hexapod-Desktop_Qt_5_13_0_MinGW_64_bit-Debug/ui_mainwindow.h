/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.13.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionEinstellungn_exportieren;
    QAction *actionEinstellungn_importieren;
    QAction *actionBeenden;
    QAction *actionStatusleiste_anzeigen;
    QAction *actionVollbildmodus;
    QAction *actionTerminal_anzeigen;
    QAction *actionAktuelles_Profil_Bearbeiten;
    QAction *actionProfile_Bearbeiten;
    QAction *actionSprache_Umschalten;
    QAction *actionKurzbefehle_festlegen;
    QAction *actionHexapod_Einrichtung;
    QAction *actionHilfe;
    QAction *actionInfo;
    QAction *actionStandardprofil;
    QWidget *centralwidget;
    QMenuBar *menubar;
    QMenu *menuDatei;
    QMenu *menuAnsicht;
    QMenu *menuEinstellungen;
    QMenu *menuProfile_wechseln;
    QMenu *menuHilfe;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1280, 960);
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(MainWindow->sizePolicy().hasHeightForWidth());
        MainWindow->setSizePolicy(sizePolicy);
        actionEinstellungn_exportieren = new QAction(MainWindow);
        actionEinstellungn_exportieren->setObjectName(QString::fromUtf8("actionEinstellungn_exportieren"));
        actionEinstellungn_importieren = new QAction(MainWindow);
        actionEinstellungn_importieren->setObjectName(QString::fromUtf8("actionEinstellungn_importieren"));
        actionBeenden = new QAction(MainWindow);
        actionBeenden->setObjectName(QString::fromUtf8("actionBeenden"));
        actionStatusleiste_anzeigen = new QAction(MainWindow);
        actionStatusleiste_anzeigen->setObjectName(QString::fromUtf8("actionStatusleiste_anzeigen"));
        actionStatusleiste_anzeigen->setCheckable(true);
        actionVollbildmodus = new QAction(MainWindow);
        actionVollbildmodus->setObjectName(QString::fromUtf8("actionVollbildmodus"));
        actionVollbildmodus->setCheckable(true);
        actionTerminal_anzeigen = new QAction(MainWindow);
        actionTerminal_anzeigen->setObjectName(QString::fromUtf8("actionTerminal_anzeigen"));
        actionTerminal_anzeigen->setCheckable(true);
        actionAktuelles_Profil_Bearbeiten = new QAction(MainWindow);
        actionAktuelles_Profil_Bearbeiten->setObjectName(QString::fromUtf8("actionAktuelles_Profil_Bearbeiten"));
        actionProfile_Bearbeiten = new QAction(MainWindow);
        actionProfile_Bearbeiten->setObjectName(QString::fromUtf8("actionProfile_Bearbeiten"));
        actionSprache_Umschalten = new QAction(MainWindow);
        actionSprache_Umschalten->setObjectName(QString::fromUtf8("actionSprache_Umschalten"));
        actionKurzbefehle_festlegen = new QAction(MainWindow);
        actionKurzbefehle_festlegen->setObjectName(QString::fromUtf8("actionKurzbefehle_festlegen"));
        actionHexapod_Einrichtung = new QAction(MainWindow);
        actionHexapod_Einrichtung->setObjectName(QString::fromUtf8("actionHexapod_Einrichtung"));
        actionHilfe = new QAction(MainWindow);
        actionHilfe->setObjectName(QString::fromUtf8("actionHilfe"));
        actionInfo = new QAction(MainWindow);
        actionInfo->setObjectName(QString::fromUtf8("actionInfo"));
        actionStandardprofil = new QAction(MainWindow);
        actionStandardprofil->setObjectName(QString::fromUtf8("actionStandardprofil"));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1280, 29));
        menuDatei = new QMenu(menubar);
        menuDatei->setObjectName(QString::fromUtf8("menuDatei"));
        menuAnsicht = new QMenu(menubar);
        menuAnsicht->setObjectName(QString::fromUtf8("menuAnsicht"));
        menuEinstellungen = new QMenu(menubar);
        menuEinstellungen->setObjectName(QString::fromUtf8("menuEinstellungen"));
        menuProfile_wechseln = new QMenu(menuEinstellungen);
        menuProfile_wechseln->setObjectName(QString::fromUtf8("menuProfile_wechseln"));
        menuHilfe = new QMenu(menubar);
        menuHilfe->setObjectName(QString::fromUtf8("menuHilfe"));
        MainWindow->setMenuBar(menubar);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName(QString::fromUtf8("statusbar"));
        MainWindow->setStatusBar(statusbar);

        menubar->addAction(menuDatei->menuAction());
        menubar->addAction(menuAnsicht->menuAction());
        menubar->addAction(menuEinstellungen->menuAction());
        menubar->addAction(menuHilfe->menuAction());
        menuDatei->addAction(actionEinstellungn_exportieren);
        menuDatei->addAction(actionEinstellungn_importieren);
        menuDatei->addSeparator();
        menuDatei->addAction(actionBeenden);
        menuAnsicht->addAction(actionStatusleiste_anzeigen);
        menuAnsicht->addAction(actionVollbildmodus);
        menuAnsicht->addAction(actionTerminal_anzeigen);
        menuEinstellungen->addAction(actionAktuelles_Profil_Bearbeiten);
        menuEinstellungen->addAction(menuProfile_wechseln->menuAction());
        menuEinstellungen->addAction(actionProfile_Bearbeiten);
        menuEinstellungen->addSeparator();
        menuEinstellungen->addAction(actionSprache_Umschalten);
        menuEinstellungen->addAction(actionKurzbefehle_festlegen);
        menuEinstellungen->addSeparator();
        menuEinstellungen->addAction(actionHexapod_Einrichtung);
        menuProfile_wechseln->addAction(actionStandardprofil);
        menuHilfe->addAction(actionHilfe);
        menuHilfe->addSeparator();
        menuHilfe->addAction(actionInfo);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        actionEinstellungn_exportieren->setText(QCoreApplication::translate("MainWindow", "Einstellungn exportieren", nullptr));
        actionEinstellungn_importieren->setText(QCoreApplication::translate("MainWindow", "Einstellungn importieren", nullptr));
        actionBeenden->setText(QCoreApplication::translate("MainWindow", "Beenden", nullptr));
#if QT_CONFIG(shortcut)
        actionBeenden->setShortcut(QCoreApplication::translate("MainWindow", "Ctrl+Q", nullptr));
#endif // QT_CONFIG(shortcut)
        actionStatusleiste_anzeigen->setText(QCoreApplication::translate("MainWindow", "Statusleiste anzeigen", nullptr));
        actionVollbildmodus->setText(QCoreApplication::translate("MainWindow", "Vollbildmodus", nullptr));
#if QT_CONFIG(shortcut)
        actionVollbildmodus->setShortcut(QCoreApplication::translate("MainWindow", "F11", nullptr));
#endif // QT_CONFIG(shortcut)
        actionTerminal_anzeigen->setText(QCoreApplication::translate("MainWindow", "Terminal anzeigen", nullptr));
        actionAktuelles_Profil_Bearbeiten->setText(QCoreApplication::translate("MainWindow", "Aktuelles Profil Bearbeiten", nullptr));
        actionProfile_Bearbeiten->setText(QCoreApplication::translate("MainWindow", "Profile Bearbeiten", nullptr));
        actionSprache_Umschalten->setText(QCoreApplication::translate("MainWindow", "Sprache Umschalten", nullptr));
        actionKurzbefehle_festlegen->setText(QCoreApplication::translate("MainWindow", "Kurzbefehle festlegen", nullptr));
        actionHexapod_Einrichtung->setText(QCoreApplication::translate("MainWindow", "Programm Einrichtung", nullptr));
        actionHilfe->setText(QCoreApplication::translate("MainWindow", "Hilfe", nullptr));
#if QT_CONFIG(shortcut)
        actionHilfe->setShortcut(QCoreApplication::translate("MainWindow", "F1", nullptr));
#endif // QT_CONFIG(shortcut)
        actionInfo->setText(QCoreApplication::translate("MainWindow", "Info", nullptr));
        actionStandardprofil->setText(QCoreApplication::translate("MainWindow", "Standardprofil", nullptr));
        menuDatei->setTitle(QCoreApplication::translate("MainWindow", "Datei", nullptr));
        menuAnsicht->setTitle(QCoreApplication::translate("MainWindow", "Ansicht", nullptr));
        menuEinstellungen->setTitle(QCoreApplication::translate("MainWindow", "Einstellungen", nullptr));
        menuProfile_wechseln->setTitle(QCoreApplication::translate("MainWindow", "Profile wechseln", nullptr));
        menuHilfe->setTitle(QCoreApplication::translate("MainWindow", "Hilfe", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
