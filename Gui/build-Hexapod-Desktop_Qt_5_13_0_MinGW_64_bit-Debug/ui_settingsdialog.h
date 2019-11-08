/********************************************************************************
** Form generated from reading UI file 'settingsdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.13.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SETTINGSDIALOG_H
#define UI_SETTINGSDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SettingsDialog
{
public:
    QTabWidget *tabWidget;
    QWidget *tab0;
    QLabel *label;
    QLineEdit *lineEdit;
    QLabel *label_2;
    QLabel *label_3;
    QLineEdit *lineEdit_2;
    QLineEdit *lineEdit_3;
    QLabel *label_4;
    QLineEdit *lineEdit_4;
    QLabel *label_5;
    QWidget *tab1;
    QLabel *label_6;
    QLabel *label_11;
    QLabel *label_12;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_17;
    QLabel *label_18;
    QLabel *label_19;
    QLabel *label_20;
    QLabel *label_21;
    QLabel *label_22;
    QLabel *label_23;
    QLabel *label_24;
    QWidget *tab;
    QLineEdit *lineEdit_5;
    QLabel *label_7;
    QLabel *label_8;
    QLineEdit *lineEdit_6;
    QLabel *label_9;
    QLineEdit *lineEdit_7;
    QLabel *label_10;
    QLineEdit *lineEdit_8;
    QPushButton *pushButton_5;
    QPushButton *pushButton_6;
    QTableWidget *tableWidget;
    QPushButton *pushButton_7;
    QPushButton *pushButton;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QPushButton *pushButton_4;

    void setupUi(QDialog *SettingsDialog)
    {
        if (SettingsDialog->objectName().isEmpty())
            SettingsDialog->setObjectName(QString::fromUtf8("SettingsDialog"));
        SettingsDialog->resize(1024, 768);
        tabWidget = new QTabWidget(SettingsDialog);
        tabWidget->setObjectName(QString::fromUtf8("tabWidget"));
        tabWidget->setGeometry(QRect(10, 60, 1001, 651));
        tab0 = new QWidget();
        tab0->setObjectName(QString::fromUtf8("tab0"));
        label = new QLabel(tab0);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 20, 171, 24));
        label->setTextFormat(Qt::RichText);
        lineEdit = new QLineEdit(tab0);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));
        lineEdit->setGeometry(QRect(130, 110, 211, 32));
        label_2 = new QLabel(tab0);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(30, 110, 91, 24));
        label_3 = new QLabel(tab0);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(30, 210, 91, 24));
        lineEdit_2 = new QLineEdit(tab0);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(130, 210, 211, 32));
        lineEdit_3 = new QLineEdit(tab0);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));
        lineEdit_3->setGeometry(QRect(130, 260, 211, 32));
        label_4 = new QLabel(tab0);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(30, 260, 91, 24));
        lineEdit_4 = new QLineEdit(tab0);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));
        lineEdit_4->setGeometry(QRect(130, 160, 211, 32));
        label_5 = new QLabel(tab0);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(30, 160, 91, 24));
        tabWidget->addTab(tab0, QString());
        tab1 = new QWidget();
        tab1->setObjectName(QString::fromUtf8("tab1"));
        label_6 = new QLabel(tab1);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setGeometry(QRect(20, 10, 471, 71));
        label_11 = new QLabel(tab1);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(30, 90, 88, 169));
        label_11->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerLeftTrigger.png")));
        label_11->setScaledContents(true);
        label_12 = new QLabel(tab1);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setGeometry(QRect(30, 280, 218, 92));
        label_12->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerLeftShoulder.png")));
        label_13 = new QLabel(tab1);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setGeometry(QRect(880, 80, 88, 169));
        label_13->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerRightTrigger.png")));
        label_14 = new QLabel(tab1);
        label_14->setObjectName(QString::fromUtf8("label_14"));
        label_14->setGeometry(QRect(740, 280, 218, 92));
        label_14->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerRightShoulder.png")));
        label_15 = new QLabel(tab1);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        label_15->setGeometry(QRect(430, 100, 138, 138));
        label_15->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerButtonGuide.png")));
        label_16 = new QLabel(tab1);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setGeometry(QRect(310, 100, 83, 79));
        label_16->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerBack.png")));
        label_17 = new QLabel(tab1);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setGeometry(QRect(580, 100, 86, 78));
        label_17->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerStart.png")));
        label_18 = new QLabel(tab1);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setGeometry(QRect(30, 410, 186, 186));
        label_18->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerDPad.png")));
        label_19 = new QLabel(tab1);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setGeometry(QRect(320, 430, 153, 158));
        label_19->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerLeftThumbstick.png")));
        label_20 = new QLabel(tab1);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setGeometry(QRect(540, 430, 153, 160));
        label_20->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerRightThumbstick.png")));
        label_21 = new QLabel(tab1);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setGeometry(QRect(820, 410, 86, 78));
        label_21->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerButtonY.png")));
        label_22 = new QLabel(tab1);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setGeometry(QRect(760, 470, 86, 78));
        label_22->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerButtonX.png")));
        label_23 = new QLabel(tab1);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setGeometry(QRect(820, 530, 86, 78));
        label_23->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerButtonA.png")));
        label_24 = new QLabel(tab1);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setGeometry(QRect(880, 470, 86, 78));
        label_24->setPixmap(QPixmap(QString::fromUtf8(":/data/files/quickGamepad/xboxControllerButtonB.png")));
        tabWidget->addTab(tab1, QString());
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        lineEdit_5 = new QLineEdit(tab);
        lineEdit_5->setObjectName(QString::fromUtf8("lineEdit_5"));
        lineEdit_5->setGeometry(QRect(228, 30, 113, 32));
        label_7 = new QLabel(tab);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setGeometry(QRect(30, 30, 77, 24));
        label_8 = new QLabel(tab);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(30, 80, 77, 24));
        lineEdit_6 = new QLineEdit(tab);
        lineEdit_6->setObjectName(QString::fromUtf8("lineEdit_6"));
        lineEdit_6->setGeometry(QRect(228, 80, 113, 32));
        label_9 = new QLabel(tab);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(30, 130, 121, 24));
        lineEdit_7 = new QLineEdit(tab);
        lineEdit_7->setObjectName(QString::fromUtf8("lineEdit_7"));
        lineEdit_7->setGeometry(QRect(228, 130, 113, 32));
        label_10 = new QLabel(tab);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(30, 180, 91, 24));
        lineEdit_8 = new QLineEdit(tab);
        lineEdit_8->setObjectName(QString::fromUtf8("lineEdit_8"));
        lineEdit_8->setGeometry(QRect(228, 180, 113, 32));
        lineEdit_8->setEchoMode(QLineEdit::Password);
        pushButton_5 = new QPushButton(tab);
        pushButton_5->setObjectName(QString::fromUtf8("pushButton_5"));
        pushButton_5->setGeometry(QRect(30, 240, 111, 33));
        pushButton_6 = new QPushButton(tab);
        pushButton_6->setObjectName(QString::fromUtf8("pushButton_6"));
        pushButton_6->setGeometry(QRect(220, 240, 121, 33));
        tableWidget = new QTableWidget(tab);
        if (tableWidget->columnCount() < 4)
            tableWidget->setColumnCount(4);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        if (tableWidget->rowCount() < 3)
            tableWidget->setRowCount(3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        tableWidget->setVerticalHeaderItem(0, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        tableWidget->setVerticalHeaderItem(1, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        tableWidget->setVerticalHeaderItem(2, __qtablewidgetitem6);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        tableWidget->setItem(0, 0, __qtablewidgetitem7);
        QTableWidgetItem *__qtablewidgetitem8 = new QTableWidgetItem();
        tableWidget->setItem(0, 1, __qtablewidgetitem8);
        QTableWidgetItem *__qtablewidgetitem9 = new QTableWidgetItem();
        tableWidget->setItem(0, 2, __qtablewidgetitem9);
        QTableWidgetItem *__qtablewidgetitem10 = new QTableWidgetItem();
        tableWidget->setItem(0, 3, __qtablewidgetitem10);
        QTableWidgetItem *__qtablewidgetitem11 = new QTableWidgetItem();
        tableWidget->setItem(1, 0, __qtablewidgetitem11);
        QTableWidgetItem *__qtablewidgetitem12 = new QTableWidgetItem();
        tableWidget->setItem(1, 1, __qtablewidgetitem12);
        QTableWidgetItem *__qtablewidgetitem13 = new QTableWidgetItem();
        tableWidget->setItem(1, 2, __qtablewidgetitem13);
        QTableWidgetItem *__qtablewidgetitem14 = new QTableWidgetItem();
        tableWidget->setItem(1, 3, __qtablewidgetitem14);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));
        tableWidget->setGeometry(QRect(360, 30, 421, 321));
        pushButton_7 = new QPushButton(tab);
        pushButton_7->setObjectName(QString::fromUtf8("pushButton_7"));
        pushButton_7->setGeometry(QRect(360, 370, 103, 33));
        tabWidget->addTab(tab, QString());
        pushButton = new QPushButton(SettingsDialog);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setGeometry(QRect(10, 720, 141, 33));
        pushButton_2 = new QPushButton(SettingsDialog);
        pushButton_2->setObjectName(QString::fromUtf8("pushButton_2"));
        pushButton_2->setGeometry(QRect(690, 720, 103, 33));
        pushButton_3 = new QPushButton(SettingsDialog);
        pushButton_3->setObjectName(QString::fromUtf8("pushButton_3"));
        pushButton_3->setGeometry(QRect(800, 720, 103, 33));
        pushButton_4 = new QPushButton(SettingsDialog);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));
        pushButton_4->setGeometry(QRect(910, 720, 103, 33));

        retranslateUi(SettingsDialog);

        tabWidget->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(SettingsDialog);
    } // setupUi

    void retranslateUi(QDialog *SettingsDialog)
    {
        SettingsDialog->setWindowTitle(QCoreApplication::translate("SettingsDialog", "Dialog", nullptr));
        label->setText(QCoreApplication::translate("SettingsDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Pfad zu Bibliotheken</span></p></body></html>", nullptr));
        lineEdit->setText(QCoreApplication::translate("SettingsDialog", "/usr/share/bin/pygame", nullptr));
        label_2->setText(QCoreApplication::translate("SettingsDialog", "PyGame:", nullptr));
        label_3->setText(QCoreApplication::translate("SettingsDialog", "Foo:", nullptr));
        lineEdit_2->setText(QCoreApplication::translate("SettingsDialog", "/usr/share/bin/foo", nullptr));
        lineEdit_3->setText(QCoreApplication::translate("SettingsDialog", "/usr/share/bin/foo", nullptr));
        label_4->setText(QCoreApplication::translate("SettingsDialog", "Bar:", nullptr));
        lineEdit_4->setText(QCoreApplication::translate("SettingsDialog", "/usr/share/bin/zeromq", nullptr));
        label_5->setText(QCoreApplication::translate("SettingsDialog", "zeroMQ:", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab0), QCoreApplication::translate("SettingsDialog", "Lokale Einstellungen", nullptr));
        label_6->setText(QCoreApplication::translate("SettingsDialog", "<html><head/><body><p>Fancy Shit from QtGamepad Demos here!</p><p>Configure Controller<br/>Setup controller keymap<br/>test controller keys</p></body></html>", nullptr));
        label_11->setText(QString());
        label_12->setText(QString());
        label_13->setText(QString());
        label_14->setText(QString());
        label_15->setText(QString());
        label_16->setText(QString());
        label_17->setText(QString());
        label_18->setText(QString());
        label_19->setText(QString());
        label_20->setText(QString());
        label_21->setText(QString());
        label_22->setText(QString());
        label_23->setText(QString());
        label_24->setText(QString());
        tabWidget->setTabText(tabWidget->indexOf(tab1), QCoreApplication::translate("SettingsDialog", "Controller Einstellungen", nullptr));
        lineEdit_5->setText(QCoreApplication::translate("SettingsDialog", "MyRobot", nullptr));
        label_7->setText(QCoreApplication::translate("SettingsDialog", "Name", nullptr));
        label_8->setText(QCoreApplication::translate("SettingsDialog", "IP", nullptr));
        lineEdit_6->setText(QCoreApplication::translate("SettingsDialog", "192.168.0.1", nullptr));
        label_9->setText(QCoreApplication::translate("SettingsDialog", "Benutzername", nullptr));
        lineEdit_7->setText(QCoreApplication::translate("SettingsDialog", "root", nullptr));
        label_10->setText(QCoreApplication::translate("SettingsDialog", "Passwort", nullptr));
        lineEdit_8->setText(QCoreApplication::translate("SettingsDialog", "MyRobot", nullptr));
        pushButton_5->setText(QCoreApplication::translate("SettingsDialog", "Hinzuf\303\274gen", nullptr));
        pushButton_6->setText(QCoreApplication::translate("SettingsDialog", "Zur\303\274cksetzen", nullptr));
        QTableWidgetItem *___qtablewidgetitem = tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QCoreApplication::translate("SettingsDialog", "Name", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QCoreApplication::translate("SettingsDialog", "IP", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = tableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QCoreApplication::translate("SettingsDialog", "Benutzername", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = tableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QCoreApplication::translate("SettingsDialog", "Passwort \303\244ndern", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = tableWidget->verticalHeaderItem(0);
        ___qtablewidgetitem4->setText(QCoreApplication::translate("SettingsDialog", "1", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = tableWidget->verticalHeaderItem(1);
        ___qtablewidgetitem5->setText(QCoreApplication::translate("SettingsDialog", "2", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = tableWidget->verticalHeaderItem(2);
        ___qtablewidgetitem6->setText(QCoreApplication::translate("SettingsDialog", "3", nullptr));

        const bool __sortingEnabled = tableWidget->isSortingEnabled();
        tableWidget->setSortingEnabled(false);
        QTableWidgetItem *___qtablewidgetitem7 = tableWidget->item(0, 0);
        ___qtablewidgetitem7->setText(QCoreApplication::translate("SettingsDialog", "MyRobot", nullptr));
        QTableWidgetItem *___qtablewidgetitem8 = tableWidget->item(0, 1);
        ___qtablewidgetitem8->setText(QCoreApplication::translate("SettingsDialog", "192.168.0.1", nullptr));
        QTableWidgetItem *___qtablewidgetitem9 = tableWidget->item(0, 2);
        ___qtablewidgetitem9->setText(QCoreApplication::translate("SettingsDialog", "root", nullptr));
        tableWidget->setSortingEnabled(__sortingEnabled);

        pushButton_7->setText(QCoreApplication::translate("SettingsDialog", "L\303\266schen", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QCoreApplication::translate("SettingsDialog", "Roboter", nullptr));
        pushButton->setText(QCoreApplication::translate("SettingsDialog", "Voreinstellungen", nullptr));
        pushButton_2->setText(QCoreApplication::translate("SettingsDialog", "OK", nullptr));
        pushButton_3->setText(QCoreApplication::translate("SettingsDialog", "Anwenden", nullptr));
        pushButton_4->setText(QCoreApplication::translate("SettingsDialog", "Abbrechen", nullptr));
    } // retranslateUi

};

namespace Ui {
    class SettingsDialog: public Ui_SettingsDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SETTINGSDIALOG_H
