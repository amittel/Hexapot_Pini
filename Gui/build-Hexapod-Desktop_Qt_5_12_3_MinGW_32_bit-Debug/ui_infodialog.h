/********************************************************************************
** Form generated from reading UI file 'infodialog.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_INFODIALOG_H
#define UI_INFODIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QLabel>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_InfoDialog
{
public:
    QLabel *label_logo;
    QLabel *label_appname;
    QTabWidget *tabWidget;
    QWidget *tab0;
    QLabel *label;
    QWidget *tab1;
    QLabel *label_2;
    QWidget *tab2;
    QTextBrowser *textBrowser;
    QWidget *tab3;
    QLabel *label_3;
    QPushButton *pushButton;

    void setupUi(QDialog *InfoDialog)
    {
        if (InfoDialog->objectName().isEmpty())
            InfoDialog->setObjectName(QString::fromUtf8("InfoDialog"));
        InfoDialog->resize(600, 480);
        label_logo = new QLabel(InfoDialog);
        label_logo->setObjectName(QString::fromUtf8("label_logo"));
        label_logo->setGeometry(QRect(10, 10, 71, 71));
        label_logo->setPixmap(QPixmap(QString::fromUtf8(":/data/files/Decepticons-Logo.png")));
        label_logo->setScaledContents(true);
        label_appname = new QLabel(InfoDialog);
        label_appname->setObjectName(QString::fromUtf8("label_appname"));
        label_appname->setGeometry(QRect(90, 20, 461, 51));
        tabWidget = new QTabWidget(InfoDialog);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(10, 90, 581, 341));
        tab0 = new QWidget();
        tab0->setObjectName(QString::fromUtf8("tab0"));
        label = new QLabel(tab0);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(30, 60, 541, 201));
        tabWidget->addTab(tab0, QString());
        tab1 = new QWidget();
        tab1->setObjectName(QString::fromUtf8("tab1"));
        label_2 = new QLabel(tab1);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(40, 10, 301, 131));
        tabWidget->addTab(tab1, QString());
        tab2 = new QWidget();
        tab2->setObjectName(QString::fromUtf8("tab2"));
        textBrowser = new QTextBrowser(tab2);
        textBrowser->setObjectName(QString::fromUtf8("textBrowser"));
        textBrowser->setGeometry(QRect(10, 10, 561, 281));
        tabWidget->addTab(tab2, QString());
        tab3 = new QWidget();
        tab3->setObjectName(QString::fromUtf8("tab3"));
        label_3 = new QLabel(tab3);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(10, 20, 561, 271));
        tabWidget->addTab(tab3, QString());
        pushButton = new QPushButton(InfoDialog);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(490, 440, 103, 33));

        retranslateUi(InfoDialog);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(InfoDialog);
    } // setupUi

    void retranslateUi(QDialog *InfoDialog)
    {
        InfoDialog->setWindowTitle(QApplication::translate("InfoDialog", "\303\234ber Hexapod Steuerungssoftware", nullptr));
        label_logo->setText(QString());
        label_appname->setText(QApplication::translate("InfoDialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Hexapod Steuerungssoftware - Team Blau<br/></span>Version 1.0</p></body></html>", nullptr));
        label->setText(QApplication::translate("InfoDialog", "<html><head/><body><p>Hexapod Steuerungssoftware<br/></p><p>Copyright \302\251 2019-2020 Team Blau<br/></p><p><a href=\"https://www.fh-bielefeld.de/ium/presse/aktuelles/hexapod-walking-challenge\"><span style=\" text-decoration: underline; color:#2980b9;\">https://www.fh-bielefeld.de/ium/presse/aktuelles/<br/>hexapod-walking-challenge</span></a></p><p>Liezenz: Link zum Lizenz-Dialog</p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab0), QApplication::translate("InfoDialog", "\303\234ber", nullptr));
        label_2->setText(QApplication::translate("InfoDialog", "<html><head/><body><p><span style=\" font-family:'sans-serif'; color:#222222; background-color:#ffffff;\">\342\200\242 </span>KDE Frameworks 5.55.0<br/><span style=\" font-family:'sans-serif'; color:#222222; background-color:#ffffff;\">\342\200\242 </span>Qt 5.13 (kompiliert gegen 5.13)<br/><span style=\" font-family:'sans-serif'; color:#222222; background-color:#ffffff;\">\342\200\242 </span>Das <span style=\" font-style:italic;\">xcb</span> Fenstersystem</p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab1), QApplication::translate("InfoDialog", "Bibliotheken", nullptr));
        textBrowser->setHtml(QApplication::translate("InfoDialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Bitte verwenden Sie </span><a href=\"https://github.com/amittel/Hexapot_Pini/issues\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">https://github.com/amittel/Hexapot_Pini/issues</span></a><span style=\" font-family:'Noto Sans';\"> f\303\274r Problemberichte.<br /><br />Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a>"
                        "</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt"
                        "@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" "
                        "font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" mar"
                        "gin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-l"
                        "eft:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; co"
                        "lor:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a h"
                        "ref=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br />Chefentwickler<br /></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" font-family:'Noto Sans'; text-decoration: underline; color:#2980b9;\">E-Mail</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\""
                        "><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Noto Sans';\"><br /></p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab2), QApplication::translate("InfoDialog", "Autoren", nullptr));
        label_3->setText(QApplication::translate("InfoDialog", "<html><head/><body><p><span style=\" font-family:'Noto Sans';\">Arnulf Mittelst\303\244dt<br/>Chefentwickler<br/></span><a href=\"mailto:arnulf.mittelstaedt@fh-bielefeld.de\"><span style=\" text-decoration: underline; color:#2980b9;\">E-Mail</span></a><br/></p><p>KDE wird dank der Arbeit von Teams in aller Welt in viele<br/>Sprachen \303\274bersetzt.<br/><br/>Allgemeine Informationen zur \303\234bersetzug finden Sie unter<br/><a href=\"https://l10n.kde.org/\"><span style=\" text-decoration: underline; color:#2980b9;\">https://l10n.kde.org/</span></a><br/>Informationen zur deutschen \303\234bersetzung unter <a href=\"https://community.kde.org/KDE_Localization/de\"><span style=\" text-decoration: underline; color:#2980b9;\">https://<br/>community.kde.org/KDE_Localization/de</span></a></p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab3), QApplication::translate("InfoDialog", "\303\234bersertzung", nullptr));
        pushButton->setText(QApplication::translate("InfoDialog", "Schlie\303\237en", nullptr));
    } // retranslateUi

};

namespace Ui {
    class InfoDialog: public Ui_InfoDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_INFODIALOG_H
