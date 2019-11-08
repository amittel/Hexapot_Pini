/********************************************************************************
** Form generated from reading UI file 'infodialog.ui'
**
** Created by: Qt User Interface Compiler version 5.13.0
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
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_InfoDialog
{
public:
    QLabel *label_logo;
    QLabel *label_appname;
    QTabWidget *tabWidget;
    QWidget *tab0;
    QWidget *tab1;
    QWidget *tab2;
    QWidget *tab3;
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
        label_appname->setGeometry(QRect(90, 20, 121, 51));
        tabWidget = new QTabWidget(InfoDialog);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(10, 90, 581, 341));
        tab0 = new QWidget();
        tab0->setObjectName(QString::fromUtf8("tab0"));
        tabWidget->addTab(tab0, QString());
        tab1 = new QWidget();
        tab1->setObjectName(QString::fromUtf8("tab1"));
        tabWidget->addTab(tab1, QString());
        tab2 = new QWidget();
        tab2->setObjectName(QString::fromUtf8("tab2"));
        tabWidget->addTab(tab2, QString());
        tab3 = new QWidget();
        tab3->setObjectName(QString::fromUtf8("tab3"));
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
        InfoDialog->setWindowTitle(QCoreApplication::translate("InfoDialog", "Dialog", nullptr));
        label_logo->setText(QString());
        label_appname->setText(QCoreApplication::translate("InfoDialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Hexapod<br/></span>Version 1.0</p></body></html>", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab0), QCoreApplication::translate("InfoDialog", "\303\234ber", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab1), QCoreApplication::translate("InfoDialog", "Bibliotheken", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab2), QCoreApplication::translate("InfoDialog", "Autoren", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab3), QCoreApplication::translate("InfoDialog", "\303\234bersertzung", nullptr));
        pushButton->setText(QCoreApplication::translate("InfoDialog", "Schlie\303\237en", nullptr));
    } // retranslateUi

};

namespace Ui {
    class InfoDialog: public Ui_InfoDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_INFODIALOG_H
