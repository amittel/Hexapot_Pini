/********************************************************************************
** Form generated from reading UI file 'settingsdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SETTINGSDIALOG_H
#define UI_SETTINGSDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SettingsDialog
{
public:
    QTabWidget *tabWidget;
    QWidget *tab0;
    QLabel *label;
    QGroupBox *netGroupBox;
    QWidget *layoutWidget;
    QVBoxLayout *lineEditGroup;
    QLineEdit *lineEdit_4;
    QLineEdit *lineEdit_2;
    QLineEdit *lineEdit_3;
    QWidget *layoutWidget1;
    QVBoxLayout *netRadioButtons;
    QRadioButton *radioButton_1;
    QRadioButton *radioButton_2;
    QRadioButton *radioButton_3;
    QGroupBox *gamepadGroupBox;
    QWidget *layoutWidget2;
    QVBoxLayout *verticalLayout;
    QLineEdit *lineEdit_1;
    QLineEdit *lineEdit_9;
    QWidget *layoutWidget3;
    QVBoxLayout *verticalLayout_3;
    QRadioButton *radioButton;
    QRadioButton *radioButton_4;
    QWidget *tab1;
    QPushButton *pushButton_8;
    QPushButton *pushButton_9;
    QPushButton *pushButton_10;
    QPushButton *pushButton_11;
    QPushButton *pushButton_12;
    QPushButton *pushButton_13;
    QPushButton *pushButton_14;
    QPushButton *pushButton_15;
    QPushButton *pushButton_16;
    QPushButton *pushButton_17;
    QPushButton *pushButton_18;
    QPushButton *pushButton_19;
    QPushButton *pushButton_20;
    QPushButton *pushButton_21;
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
        QFont font;
        font.setFamily(QString::fromUtf8("academicons"));
        tabWidget->setFont(font);
        tab0 = new QWidget();
        tab0->setObjectName(QString::fromUtf8("tab0"));
        label = new QLabel(tab0);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 20, 171, 24));
        label->setTextFormat(Qt::RichText);
        netGroupBox = new QGroupBox(tab0);
        netGroupBox->setObjectName(QString::fromUtf8("netGroupBox"));
        netGroupBox->setGeometry(QRect(10, 260, 481, 231));
        netGroupBox->setCheckable(false);
        layoutWidget = new QWidget(netGroupBox);
        layoutWidget->setObjectName(QString::fromUtf8("layoutWidget"));
        layoutWidget->setGeometry(QRect(200, 50, 261, 161));
        lineEditGroup = new QVBoxLayout(layoutWidget);
        lineEditGroup->setObjectName(QString::fromUtf8("lineEditGroup"));
        lineEditGroup->setContentsMargins(0, 0, 0, 0);
        lineEdit_4 = new QLineEdit(layoutWidget);
        lineEdit_4->setObjectName(QString::fromUtf8("lineEdit_4"));

        lineEditGroup->addWidget(lineEdit_4);

        lineEdit_2 = new QLineEdit(layoutWidget);
        lineEdit_2->setObjectName(QString::fromUtf8("lineEdit_2"));

        lineEditGroup->addWidget(lineEdit_2);

        lineEdit_3 = new QLineEdit(layoutWidget);
        lineEdit_3->setObjectName(QString::fromUtf8("lineEdit_3"));

        lineEditGroup->addWidget(lineEdit_3);

        layoutWidget1 = new QWidget(netGroupBox);
        layoutWidget1->setObjectName(QString::fromUtf8("layoutWidget1"));
        layoutWidget1->setGeometry(QRect(10, 50, 171, 161));
        netRadioButtons = new QVBoxLayout(layoutWidget1);
        netRadioButtons->setObjectName(QString::fromUtf8("netRadioButtons"));
        netRadioButtons->setContentsMargins(0, 0, 0, 0);
        radioButton_1 = new QRadioButton(layoutWidget1);
        radioButton_1->setObjectName(QString::fromUtf8("radioButton_1"));
        radioButton_1->setChecked(true);

        netRadioButtons->addWidget(radioButton_1);

        radioButton_2 = new QRadioButton(layoutWidget1);
        radioButton_2->setObjectName(QString::fromUtf8("radioButton_2"));

        netRadioButtons->addWidget(radioButton_2);

        radioButton_3 = new QRadioButton(layoutWidget1);
        radioButton_3->setObjectName(QString::fromUtf8("radioButton_3"));

        netRadioButtons->addWidget(radioButton_3);

        gamepadGroupBox = new QGroupBox(tab0);
        gamepadGroupBox->setObjectName(QString::fromUtf8("gamepadGroupBox"));
        gamepadGroupBox->setGeometry(QRect(10, 50, 481, 191));
        gamepadGroupBox->setCheckable(false);
        layoutWidget2 = new QWidget(gamepadGroupBox);
        layoutWidget2->setObjectName(QString::fromUtf8("layoutWidget2"));
        layoutWidget2->setGeometry(QRect(200, 50, 261, 121));
        verticalLayout = new QVBoxLayout(layoutWidget2);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        lineEdit_1 = new QLineEdit(layoutWidget2);
        lineEdit_1->setObjectName(QString::fromUtf8("lineEdit_1"));

        verticalLayout->addWidget(lineEdit_1);

        lineEdit_9 = new QLineEdit(layoutWidget2);
        lineEdit_9->setObjectName(QString::fromUtf8("lineEdit_9"));

        verticalLayout->addWidget(lineEdit_9);

        layoutWidget3 = new QWidget(gamepadGroupBox);
        layoutWidget3->setObjectName(QString::fromUtf8("layoutWidget3"));
        layoutWidget3->setGeometry(QRect(10, 50, 181, 121));
        verticalLayout_3 = new QVBoxLayout(layoutWidget3);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        radioButton = new QRadioButton(layoutWidget3);
        radioButton->setObjectName(QString::fromUtf8("radioButton"));
        radioButton->setChecked(true);

        verticalLayout_3->addWidget(radioButton);

        radioButton_4 = new QRadioButton(layoutWidget3);
        radioButton_4->setObjectName(QString::fromUtf8("radioButton_4"));

        verticalLayout_3->addWidget(radioButton_4);

        tabWidget->addTab(tab0, QString());
        tab1 = new QWidget();
        tab1->setObjectName(QString::fromUtf8("tab1"));
        pushButton_8 = new QPushButton(tab1);
        pushButton_8->setObjectName(QString::fromUtf8("pushButton_8"));
        pushButton_8->setGeometry(QRect(430, 100, 141, 141));
        pushButton_8->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerButtonGuide.png);"));
        pushButton_8->setFlat(true);
        pushButton_9 = new QPushButton(tab1);
        pushButton_9->setObjectName(QString::fromUtf8("pushButton_9"));
        pushButton_9->setGeometry(QRect(540, 430, 151, 161));
        pushButton_9->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerRightThumbstick.png);"));
        pushButton_9->setFlat(true);
        pushButton_10 = new QPushButton(tab1);
        pushButton_10->setObjectName(QString::fromUtf8("pushButton_10"));
        pushButton_10->setGeometry(QRect(320, 430, 154, 161));
        pushButton_10->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerLeftThumbstick.png);"));
        pushButton_10->setFlat(true);
        pushButton_11 = new QPushButton(tab1);
        pushButton_11->setObjectName(QString::fromUtf8("pushButton_11"));
        pushButton_11->setGeometry(QRect(30, 410, 189, 189));
        pushButton_11->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerDPad.png);"));
        pushButton_11->setFlat(true);
        pushButton_12 = new QPushButton(tab1);
        pushButton_12->setObjectName(QString::fromUtf8("pushButton_12"));
        pushButton_12->setGeometry(QRect(30, 90, 91, 171));
        pushButton_12->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerLeftTrigger.png);"));
        pushButton_12->setFlat(true);
        pushButton_13 = new QPushButton(tab1);
        pushButton_13->setObjectName(QString::fromUtf8("pushButton_13"));
        pushButton_13->setGeometry(QRect(580, 100, 86, 81));
        pushButton_13->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerStart.png);"));
        pushButton_13->setFlat(true);
        pushButton_14 = new QPushButton(tab1);
        pushButton_14->setObjectName(QString::fromUtf8("pushButton_14"));
        pushButton_14->setGeometry(QRect(310, 100, 84, 81));
        pushButton_14->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerBack.png);"));
        pushButton_14->setFlat(true);
        pushButton_15 = new QPushButton(tab1);
        pushButton_15->setObjectName(QString::fromUtf8("pushButton_15"));
        pushButton_15->setGeometry(QRect(880, 80, 91, 171));
        pushButton_15->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerRightTrigger.png);"));
        pushButton_15->setFlat(true);
        pushButton_16 = new QPushButton(tab1);
        pushButton_16->setObjectName(QString::fromUtf8("pushButton_16"));
        pushButton_16->setGeometry(QRect(30, 280, 221, 91));
        pushButton_16->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerLeftShoulder.png);"));
        pushButton_16->setFlat(true);
        pushButton_17 = new QPushButton(tab1);
        pushButton_17->setObjectName(QString::fromUtf8("pushButton_17"));
        pushButton_17->setGeometry(QRect(740, 280, 221, 91));
        pushButton_17->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerRightShoulder.png);"));
        pushButton_17->setFlat(true);
        pushButton_18 = new QPushButton(tab1);
        pushButton_18->setObjectName(QString::fromUtf8("pushButton_18"));
        pushButton_18->setGeometry(QRect(820, 400, 81, 81));
        pushButton_18->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerButtonY.png);"));
        pushButton_18->setFlat(true);
        pushButton_19 = new QPushButton(tab1);
        pushButton_19->setObjectName(QString::fromUtf8("pushButton_19"));
        pushButton_19->setGeometry(QRect(750, 460, 81, 81));
        pushButton_19->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerButtonX.png);"));
        pushButton_19->setFlat(true);
        pushButton_20 = new QPushButton(tab1);
        pushButton_20->setObjectName(QString::fromUtf8("pushButton_20"));
        pushButton_20->setGeometry(QRect(820, 520, 81, 81));
        pushButton_20->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerButtonA.png);"));
        pushButton_20->setFlat(true);
        pushButton_21 = new QPushButton(tab1);
        pushButton_21->setObjectName(QString::fromUtf8("pushButton_21"));
        pushButton_21->setGeometry(QRect(890, 460, 81, 81));
        pushButton_21->setStyleSheet(QString::fromUtf8("background-image: url(:/data/files/quickGamepad/xboxControllerButtonB.png);"));
        pushButton_21->setFlat(true);
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
        tableWidget->setGeometry(QRect(360, 30, 631, 321));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tableWidget->sizePolicy().hasHeightForWidth());
        tableWidget->setSizePolicy(sizePolicy);
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
        SettingsDialog->setWindowTitle(QApplication::translate("SettingsDialog", "Hexapod Einstellungen", nullptr));
        label->setText(QApplication::translate("SettingsDialog", "<html><head/><body><p><span style=\" font-weight:600;\">Pfad zu Bibliotheken</span></p></body></html>", nullptr));
        netGroupBox->setTitle(QApplication::translate("SettingsDialog", "Netzwerk", nullptr));
        lineEdit_4->setText(QApplication::translate("SettingsDialog", "/path/to/app/directory/subdir", nullptr));
        lineEdit_2->setText(QApplication::translate("SettingsDialog", "/usr/bin/netcat", nullptr));
        lineEdit_3->setText(QApplication::translate("SettingsDialog", "/usr/share/bin/zeromq", nullptr));
        radioButton_1->setText(QApplication::translate("SettingsDialog", "Hexapod Nativ", nullptr));
        radioButton_2->setText(QApplication::translate("SettingsDialog", "Linux Nativ", nullptr));
        radioButton_3->setText(QApplication::translate("SettingsDialog", "zeroMQ", nullptr));
        gamepadGroupBox->setTitle(QApplication::translate("SettingsDialog", "Game Controller", nullptr));
        lineEdit_1->setText(QApplication::translate("SettingsDialog", "/path/to/app/directory/subdir", nullptr));
        lineEdit_9->setText(QApplication::translate("SettingsDialog", "/usr/share/bin/pygame", nullptr));
        radioButton->setText(QApplication::translate("SettingsDialog", "Hexapod Nativ", nullptr));
        radioButton_4->setText(QApplication::translate("SettingsDialog", "PyGame", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab0), QApplication::translate("SettingsDialog", "Lokale Einstellungen", nullptr));
        pushButton_8->setText(QString());
        pushButton_9->setText(QString());
        pushButton_10->setText(QString());
        pushButton_11->setText(QString());
        pushButton_12->setText(QString());
        pushButton_13->setText(QString());
        pushButton_14->setText(QString());
        pushButton_15->setText(QString());
        pushButton_16->setText(QString());
        pushButton_17->setText(QString());
        pushButton_18->setText(QString());
        pushButton_19->setText(QString());
        pushButton_20->setText(QString());
        pushButton_21->setText(QString());
        tabWidget->setTabText(tabWidget->indexOf(tab1), QApplication::translate("SettingsDialog", "Controller Einstellungen", nullptr));
        lineEdit_5->setText(QApplication::translate("SettingsDialog", "MyRobot", nullptr));
        label_7->setText(QApplication::translate("SettingsDialog", "Name", nullptr));
        label_8->setText(QApplication::translate("SettingsDialog", "IP", nullptr));
        lineEdit_6->setText(QApplication::translate("SettingsDialog", "192.168.0.1", nullptr));
        label_9->setText(QApplication::translate("SettingsDialog", "Benutzername", nullptr));
        lineEdit_7->setText(QApplication::translate("SettingsDialog", "root", nullptr));
        label_10->setText(QApplication::translate("SettingsDialog", "Passwort", nullptr));
        lineEdit_8->setText(QApplication::translate("SettingsDialog", "MyRobot", nullptr));
        pushButton_5->setText(QApplication::translate("SettingsDialog", "Hinzuf\303\274gen", nullptr));
        pushButton_6->setText(QApplication::translate("SettingsDialog", "Zur\303\274cksetzen", nullptr));
        QTableWidgetItem *___qtablewidgetitem = tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("SettingsDialog", "Name", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("SettingsDialog", "IP", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = tableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("SettingsDialog", "Benutzername", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = tableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("SettingsDialog", "Passwort \303\244ndern", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = tableWidget->verticalHeaderItem(0);
        ___qtablewidgetitem4->setText(QApplication::translate("SettingsDialog", "1", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = tableWidget->verticalHeaderItem(1);
        ___qtablewidgetitem5->setText(QApplication::translate("SettingsDialog", "2", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = tableWidget->verticalHeaderItem(2);
        ___qtablewidgetitem6->setText(QApplication::translate("SettingsDialog", "3", nullptr));

        const bool __sortingEnabled = tableWidget->isSortingEnabled();
        tableWidget->setSortingEnabled(false);
        QTableWidgetItem *___qtablewidgetitem7 = tableWidget->item(0, 0);
        ___qtablewidgetitem7->setText(QApplication::translate("SettingsDialog", "MyRobot", nullptr));
        QTableWidgetItem *___qtablewidgetitem8 = tableWidget->item(0, 1);
        ___qtablewidgetitem8->setText(QApplication::translate("SettingsDialog", "192.168.0.1", nullptr));
        QTableWidgetItem *___qtablewidgetitem9 = tableWidget->item(0, 2);
        ___qtablewidgetitem9->setText(QApplication::translate("SettingsDialog", "root", nullptr));
        tableWidget->setSortingEnabled(__sortingEnabled);

        pushButton_7->setText(QApplication::translate("SettingsDialog", "L\303\266schen", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(tab), QApplication::translate("SettingsDialog", "Roboter", nullptr));
        pushButton->setText(QApplication::translate("SettingsDialog", "Voreinstellungen", nullptr));
        pushButton_2->setText(QApplication::translate("SettingsDialog", "OK", nullptr));
        pushButton_3->setText(QApplication::translate("SettingsDialog", "Anwenden", nullptr));
        pushButton_4->setText(QApplication::translate("SettingsDialog", "Abbrechen", nullptr));
    } // retranslateUi

};

namespace Ui {
    class SettingsDialog: public Ui_SettingsDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SETTINGSDIALOG_H
