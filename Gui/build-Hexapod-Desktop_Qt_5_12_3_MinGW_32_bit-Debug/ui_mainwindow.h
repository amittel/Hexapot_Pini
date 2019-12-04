/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDial>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSlider>
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
    QGridLayout *mainWindow_gridLayout;
    QGroupBox *gamepadGroup;
    QPushButton *lt_Button;
    QPushButton *startButton;
    QPushButton *rb_Button;
    QPushButton *xboxButton;
    QPushButton *lb_Button;
    QPushButton *x_Button;
    QPushButton *analog_r_Button;
    QPushButton *analog_l_Button;
    QPushButton *rt_Button;
    QPushButton *b_Button;
    QPushButton *a_Button;
    QPushButton *backButton;
    QPushButton *y_Button;
    QPushButton *d_pad_Button;
    QProgressBar *lt_progressBar;
    QProgressBar *rt_progressBar;
    QLabel *devie_name_label;
    QComboBox *comboBox;
    QGroupBox *controlGroup;
    QDial *dial;
    QGroupBox *preset_groupBox;
    QRadioButton *default_radioButton;
    QRadioButton *walking_1_radioButton;
    QRadioButton *walking_2_radioButton;
    QRadioButton *walking_3_radioButton;
    QLabel *kreis;
    QPushButton *arrow_left_Button;
    QPushButton *arrow_left_up_Button;
    QPushButton *arrow_up_Button;
    QPushButton *arrow_right_up_Button;
    QPushButton *arrow_right_Button;
    QPushButton *arrow_down_Button;
    QLabel *leg_height_label;
    QLabel *speed_label;
    QSlider *speed_hSlider;
    QSlider *leg_height_hSlider;
    QGroupBox *fooGroup;
    QGroupBox *raspiGroup;
    QLabel *raspi_name_label;
    QLabel *password_label;
    QLabel *ip_address_label;
    QLabel *username_label;
    QLineEdit *ip_address_line;
    QLineEdit *raspi_name_line;
    QLineEdit *password_line;
    QLineEdit *username_line;
    QPushButton *connectButton;
    QPushButton *disconnectButton;
    QLabel *connection_label;
    QLabel *status_label;
    QLabel *led_Label;
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
        mainWindow_gridLayout = new QGridLayout(centralwidget);
        mainWindow_gridLayout->setObjectName(QString::fromUtf8("mainWindow_gridLayout"));
        gamepadGroup = new QGroupBox(centralwidget);
        gamepadGroup->setObjectName(QString::fromUtf8("gamepadGroup"));
        lt_Button = new QPushButton(gamepadGroup);
        lt_Button->setObjectName(QString::fromUtf8("lt_Button"));
        lt_Button->setGeometry(QRect(30, 40, 51, 101));
        lt_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerLeftTrigger.png);"));
        lt_Button->setFlat(true);
        startButton = new QPushButton(gamepadGroup);
        startButton->setObjectName(QString::fromUtf8("startButton"));
        startButton->setGeometry(QRect(360, 160, 51, 51));
        startButton->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerStart.png);"));
        startButton->setFlat(true);
        rb_Button = new QPushButton(gamepadGroup);
        rb_Button->setObjectName(QString::fromUtf8("rb_Button"));
        rb_Button->setGeometry(QRect(490, 200, 121, 51));
        rb_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerRightShoulder.png);"));
        rb_Button->setFlat(true);
        xboxButton = new QPushButton(gamepadGroup);
        xboxButton->setObjectName(QString::fromUtf8("xboxButton"));
        xboxButton->setGeometry(QRect(260, 150, 81, 81));
        xboxButton->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerButtonGuide.png);"));
        xboxButton->setFlat(true);
        lb_Button = new QPushButton(gamepadGroup);
        lb_Button->setObjectName(QString::fromUtf8("lb_Button"));
        lb_Button->setGeometry(QRect(10, 200, 121, 51));
        lb_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerLeftShoulder.png);"));
        lb_Button->setFlat(true);
        x_Button = new QPushButton(gamepadGroup);
        x_Button->setObjectName(QString::fromUtf8("x_Button"));
        x_Button->setGeometry(QRect(480, 320, 51, 51));
        x_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerButtonX.png);"));
        x_Button->setFlat(true);
        analog_r_Button = new QPushButton(gamepadGroup);
        analog_r_Button->setObjectName(QString::fromUtf8("analog_r_Button"));
        analog_r_Button->setGeometry(QRect(330, 290, 101, 101));
        analog_r_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerRightThumbstick.png);"));
        analog_r_Button->setFlat(true);
        analog_l_Button = new QPushButton(gamepadGroup);
        analog_l_Button->setObjectName(QString::fromUtf8("analog_l_Button"));
        analog_l_Button->setGeometry(QRect(180, 290, 101, 101));
        analog_l_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerLeftThumbstick.png);"));
        analog_l_Button->setFlat(true);
        rt_Button = new QPushButton(gamepadGroup);
        rt_Button->setObjectName(QString::fromUtf8("rt_Button"));
        rt_Button->setGeometry(QRect(550, 40, 51, 111));
        rt_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerRightTrigger.png);"));
        rt_Button->setFlat(true);
        b_Button = new QPushButton(gamepadGroup);
        b_Button->setObjectName(QString::fromUtf8("b_Button"));
        b_Button->setGeometry(QRect(560, 320, 51, 51));
        b_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerButtonB.png);"));
        b_Button->setFlat(true);
        a_Button = new QPushButton(gamepadGroup);
        a_Button->setObjectName(QString::fromUtf8("a_Button"));
        a_Button->setGeometry(QRect(520, 360, 51, 51));
        a_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerButtonA.png);"));
        a_Button->setFlat(true);
        backButton = new QPushButton(gamepadGroup);
        backButton->setObjectName(QString::fromUtf8("backButton"));
        backButton->setGeometry(QRect(200, 160, 51, 51));
        backButton->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerBack.png);"));
        backButton->setFlat(true);
        y_Button = new QPushButton(gamepadGroup);
        y_Button->setObjectName(QString::fromUtf8("y_Button"));
        y_Button->setGeometry(QRect(520, 280, 51, 51));
        y_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerButtonY.png);"));
        y_Button->setFlat(true);
        d_pad_Button = new QPushButton(gamepadGroup);
        d_pad_Button->setObjectName(QString::fromUtf8("d_pad_Button"));
        d_pad_Button->setGeometry(QRect(20, 290, 111, 111));
        d_pad_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/quickGamepad/xboxControllerDPad.png);"));
        d_pad_Button->setFlat(true);
        lt_progressBar = new QProgressBar(gamepadGroup);
        lt_progressBar->setObjectName(QString::fromUtf8("lt_progressBar"));
        lt_progressBar->setGeometry(QRect(10, 160, 118, 26));
        lt_progressBar->setValue(10);
        lt_progressBar->setTextVisible(false);
        rt_progressBar = new QProgressBar(gamepadGroup);
        rt_progressBar->setObjectName(QString::fromUtf8("rt_progressBar"));
        rt_progressBar->setGeometry(QRect(490, 160, 118, 26));
        rt_progressBar->setStyleSheet(QString::fromUtf8(""));
        rt_progressBar->setValue(10);
        rt_progressBar->setTextVisible(false);
        rt_progressBar->setOrientation(Qt::Horizontal);
        rt_progressBar->setInvertedAppearance(true);
        devie_name_label = new QLabel(gamepadGroup);
        devie_name_label->setObjectName(QString::fromUtf8("devie_name_label"));
        devie_name_label->setGeometry(QRect(140, 60, 121, 24));
        comboBox = new QComboBox(gamepadGroup);
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->setObjectName(QString::fromUtf8("comboBox"));
        comboBox->setGeometry(QRect(140, 90, 341, 32));

        mainWindow_gridLayout->addWidget(gamepadGroup, 1, 0, 1, 1);

        controlGroup = new QGroupBox(centralwidget);
        controlGroup->setObjectName(QString::fromUtf8("controlGroup"));
        dial = new QDial(controlGroup);
        dial->setObjectName(QString::fromUtf8("dial"));
        dial->setGeometry(QRect(72, 173, 241, 241));
        dial->setMinimum(1);
        dial->setMaximum(360);
        dial->setValue(180);
        dial->setOrientation(Qt::Horizontal);
        dial->setInvertedAppearance(false);
        dial->setWrapping(true);
        dial->setNotchesVisible(true);
        preset_groupBox = new QGroupBox(controlGroup);
        preset_groupBox->setObjectName(QString::fromUtf8("preset_groupBox"));
        preset_groupBox->setGeometry(QRect(400, 30, 211, 281));
        default_radioButton = new QRadioButton(preset_groupBox);
        default_radioButton->setObjectName(QString::fromUtf8("default_radioButton"));
        default_radioButton->setGeometry(QRect(11, 24, 89, 17));
        default_radioButton->setChecked(true);
        walking_1_radioButton = new QRadioButton(preset_groupBox);
        walking_1_radioButton->setObjectName(QString::fromUtf8("walking_1_radioButton"));
        walking_1_radioButton->setGeometry(QRect(11, 47, 69, 17));
        walking_2_radioButton = new QRadioButton(preset_groupBox);
        walking_2_radioButton->setObjectName(QString::fromUtf8("walking_2_radioButton"));
        walking_2_radioButton->setGeometry(QRect(11, 70, 69, 17));
        walking_3_radioButton = new QRadioButton(preset_groupBox);
        walking_3_radioButton->setObjectName(QString::fromUtf8("walking_3_radioButton"));
        walking_3_radioButton->setGeometry(QRect(11, 93, 69, 17));
        kreis = new QLabel(controlGroup);
        kreis->setObjectName(QString::fromUtf8("kreis"));
        kreis->setGeometry(QRect(55, 157, 275, 275));
        kreis->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/kreisi-01-01.png);"));
        arrow_left_Button = new QPushButton(controlGroup);
        arrow_left_Button->setObjectName(QString::fromUtf8("arrow_left_Button"));
        arrow_left_Button->setGeometry(QRect(65, 274, 31, 33));
        arrow_left_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/arrow_left.png);"));
        arrow_left_up_Button = new QPushButton(controlGroup);
        arrow_left_up_Button->setObjectName(QString::fromUtf8("arrow_left_up_Button"));
        arrow_left_up_Button->setGeometry(QRect(99, 198, 31, 33));
        arrow_left_up_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/arrow_left-up-01.png);"));
        arrow_up_Button = new QPushButton(controlGroup);
        arrow_up_Button->setObjectName(QString::fromUtf8("arrow_up_Button"));
        arrow_up_Button->setGeometry(QRect(177, 165, 31, 33));
        arrow_up_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/arrow_up-01.png);"));
        arrow_right_up_Button = new QPushButton(controlGroup);
        arrow_right_up_Button->setObjectName(QString::fromUtf8("arrow_right_up_Button"));
        arrow_right_up_Button->setGeometry(QRect(260, 200, 31, 33));
        arrow_right_up_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/arrow_right-up-01.png);"));
        arrow_right_Button = new QPushButton(controlGroup);
        arrow_right_Button->setObjectName(QString::fromUtf8("arrow_right_Button"));
        arrow_right_Button->setGeometry(QRect(290, 274, 31, 33));
        arrow_right_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/arrow_right-01.png);"));
        arrow_down_Button = new QPushButton(controlGroup);
        arrow_down_Button->setObjectName(QString::fromUtf8("arrow_down_Button"));
        arrow_down_Button->setGeometry(QRect(177, 390, 31, 33));
        arrow_down_Button->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/arrow_down-01.png);"));
        leg_height_label = new QLabel(controlGroup);
        leg_height_label->setObjectName(QString::fromUtf8("leg_height_label"));
        leg_height_label->setGeometry(QRect(11, 80, 44, 16));
        speed_label = new QLabel(controlGroup);
        speed_label->setObjectName(QString::fromUtf8("speed_label"));
        speed_label->setGeometry(QRect(11, 41, 76, 16));
        speed_hSlider = new QSlider(controlGroup);
        speed_hSlider->setObjectName(QString::fromUtf8("speed_hSlider"));
        speed_hSlider->setGeometry(QRect(140, 41, 141, 22));
        speed_hSlider->setOrientation(Qt::Horizontal);
        leg_height_hSlider = new QSlider(controlGroup);
        leg_height_hSlider->setObjectName(QString::fromUtf8("leg_height_hSlider"));
        leg_height_hSlider->setGeometry(QRect(140, 80, 141, 22));
        leg_height_hSlider->setOrientation(Qt::Horizontal);
        leg_height_label->raise();
        speed_label->raise();
        speed_hSlider->raise();
        leg_height_hSlider->raise();
        kreis->raise();
        dial->raise();
        preset_groupBox->raise();
        arrow_left_Button->raise();
        arrow_left_up_Button->raise();
        arrow_up_Button->raise();
        arrow_right_up_Button->raise();
        arrow_right_Button->raise();
        arrow_down_Button->raise();

        mainWindow_gridLayout->addWidget(controlGroup, 0, 0, 1, 1);

        fooGroup = new QGroupBox(centralwidget);
        fooGroup->setObjectName(QString::fromUtf8("fooGroup"));

        mainWindow_gridLayout->addWidget(fooGroup, 0, 1, 1, 1);

        raspiGroup = new QGroupBox(centralwidget);
        raspiGroup->setObjectName(QString::fromUtf8("raspiGroup"));
        raspi_name_label = new QLabel(raspiGroup);
        raspi_name_label->setObjectName(QString::fromUtf8("raspi_name_label"));
        raspi_name_label->setGeometry(QRect(53, 61, 31, 16));
        password_label = new QLabel(raspiGroup);
        password_label->setObjectName(QString::fromUtf8("password_label"));
        password_label->setGeometry(QRect(53, 177, 48, 16));
        ip_address_label = new QLabel(raspiGroup);
        ip_address_label->setObjectName(QString::fromUtf8("ip_address_label"));
        ip_address_label->setGeometry(QRect(53, 100, 16, 16));
        username_label = new QLabel(raspiGroup);
        username_label->setObjectName(QString::fromUtf8("username_label"));
        username_label->setGeometry(QRect(53, 139, 73, 16));
        ip_address_line = new QLineEdit(raspiGroup);
        ip_address_line->setObjectName(QString::fromUtf8("ip_address_line"));
        ip_address_line->setGeometry(QRect(221, 107, 133, 20));
        raspi_name_line = new QLineEdit(raspiGroup);
        raspi_name_line->setObjectName(QString::fromUtf8("raspi_name_line"));
        raspi_name_line->setGeometry(QRect(221, 71, 133, 20));
        password_line = new QLineEdit(raspiGroup);
        password_line->setObjectName(QString::fromUtf8("password_line"));
        password_line->setGeometry(QRect(221, 179, 133, 20));
        password_line->setEchoMode(QLineEdit::Password);
        username_line = new QLineEdit(raspiGroup);
        username_line->setObjectName(QString::fromUtf8("username_line"));
        username_line->setGeometry(QRect(221, 143, 133, 20));
        connectButton = new QPushButton(raspiGroup);
        connectButton->setObjectName(QString::fromUtf8("connectButton"));
        connectButton->setGeometry(QRect(219, 266, 75, 23));
        disconnectButton = new QPushButton(raspiGroup);
        disconnectButton->setObjectName(QString::fromUtf8("disconnectButton"));
        disconnectButton->setGeometry(QRect(51, 266, 75, 23));
        connection_label = new QLabel(raspiGroup);
        connection_label->setObjectName(QString::fromUtf8("connection_label"));
        connection_label->setGeometry(QRect(422, 93, 105, 16));
        status_label = new QLabel(raspiGroup);
        status_label->setObjectName(QString::fromUtf8("status_label"));
        status_label->setGeometry(QRect(422, 62, 35, 16));
        led_Label = new QLabel(raspiGroup);
        led_Label->setObjectName(QString::fromUtf8("led_Label"));
        led_Label->setGeometry(QRect(440, 140, 41, 41));
        led_Label->setStyleSheet(QString::fromUtf8("border-image: url(:/data/files/ui-elements/led-red-on.png);"));

        mainWindow_gridLayout->addWidget(raspiGroup, 1, 1, 1, 1);

        MainWindow->setCentralWidget(centralwidget);
        menubar = new QMenuBar(MainWindow);
        menubar->setObjectName(QString::fromUtf8("menubar"));
        menubar->setGeometry(QRect(0, 0, 1280, 21));
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
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "Hexapod Steuerungssoftware", nullptr));
        actionEinstellungn_exportieren->setText(QApplication::translate("MainWindow", "Einstellungn exportieren", nullptr));
        actionEinstellungn_importieren->setText(QApplication::translate("MainWindow", "Einstellungn importieren", nullptr));
        actionBeenden->setText(QApplication::translate("MainWindow", "Beenden", nullptr));
#ifndef QT_NO_SHORTCUT
        actionBeenden->setShortcut(QApplication::translate("MainWindow", "Ctrl+Q", nullptr));
#endif // QT_NO_SHORTCUT
        actionStatusleiste_anzeigen->setText(QApplication::translate("MainWindow", "Statusleiste anzeigen", nullptr));
        actionVollbildmodus->setText(QApplication::translate("MainWindow", "Vollbildmodus", nullptr));
#ifndef QT_NO_SHORTCUT
        actionVollbildmodus->setShortcut(QApplication::translate("MainWindow", "F11", nullptr));
#endif // QT_NO_SHORTCUT
        actionTerminal_anzeigen->setText(QApplication::translate("MainWindow", "Terminal anzeigen", nullptr));
        actionAktuelles_Profil_Bearbeiten->setText(QApplication::translate("MainWindow", "Aktuelles Profil Bearbeiten", nullptr));
        actionProfile_Bearbeiten->setText(QApplication::translate("MainWindow", "Profile Bearbeiten", nullptr));
        actionSprache_Umschalten->setText(QApplication::translate("MainWindow", "Sprache Umschalten", nullptr));
        actionKurzbefehle_festlegen->setText(QApplication::translate("MainWindow", "Kurzbefehle festlegen", nullptr));
        actionHexapod_Einrichtung->setText(QApplication::translate("MainWindow", "Programm Einrichtung", nullptr));
        actionHilfe->setText(QApplication::translate("MainWindow", "Hilfe", nullptr));
#ifndef QT_NO_SHORTCUT
        actionHilfe->setShortcut(QApplication::translate("MainWindow", "F1", nullptr));
#endif // QT_NO_SHORTCUT
        actionInfo->setText(QApplication::translate("MainWindow", "Info", nullptr));
        actionStandardprofil->setText(QApplication::translate("MainWindow", "Standardprofil", nullptr));
        gamepadGroup->setTitle(QApplication::translate("MainWindow", "Game Controller", nullptr));
        lt_Button->setText(QString());
        startButton->setText(QString());
        rb_Button->setText(QString());
        xboxButton->setText(QString());
        lb_Button->setText(QString());
        x_Button->setText(QString());
        analog_r_Button->setText(QString());
        analog_l_Button->setText(QString());
        rt_Button->setText(QString());
        b_Button->setText(QString());
        a_Button->setText(QString());
        backButton->setText(QString());
        y_Button->setText(QString());
        d_pad_Button->setText(QString());
        devie_name_label->setText(QApplication::translate("MainWindow", "Ger\303\244t", nullptr));
        comboBox->setItemText(0, QApplication::translate("MainWindow", "XBOX 360 Gamepad (/dev/input/js0)", nullptr));
        comboBox->setItemText(1, QApplication::translate("MainWindow", "Playstation Gamepad (/dev/input/js1)", nullptr));

        controlGroup->setTitle(QApplication::translate("MainWindow", "Steuerung", nullptr));
        preset_groupBox->setTitle(QApplication::translate("MainWindow", "Presets", nullptr));
        default_radioButton->setText(QApplication::translate("MainWindow", "Grundposition", nullptr));
        walking_1_radioButton->setText(QApplication::translate("MainWindow", "Walking 1", nullptr));
        walking_2_radioButton->setText(QApplication::translate("MainWindow", "Walking 2", nullptr));
        walking_3_radioButton->setText(QApplication::translate("MainWindow", "Walking 3", nullptr));
        kreis->setText(QString());
        arrow_left_Button->setText(QString());
        arrow_left_up_Button->setText(QString());
        arrow_up_Button->setText(QString());
        arrow_right_up_Button->setText(QString());
        arrow_right_Button->setText(QString());
        arrow_down_Button->setText(QString());
        leg_height_label->setText(QApplication::translate("MainWindow", "Beinh\303\266he", nullptr));
        speed_label->setText(QApplication::translate("MainWindow", "Geschwindigkeit", nullptr));
        fooGroup->setTitle(QApplication::translate("MainWindow", "Foo", nullptr));
        raspiGroup->setTitle(QApplication::translate("MainWindow", "RaspberryPi Verbindung", nullptr));
        raspi_name_label->setText(QApplication::translate("MainWindow", "Name:", nullptr));
        password_label->setText(QApplication::translate("MainWindow", "Passwort:", nullptr));
        ip_address_label->setText(QApplication::translate("MainWindow", "IP:", nullptr));
        username_label->setText(QApplication::translate("MainWindow", "Benutzername:", nullptr));
        ip_address_line->setText(QApplication::translate("MainWindow", "192.168.0.1", nullptr));
        raspi_name_line->setText(QApplication::translate("MainWindow", "MyRobot", nullptr));
        password_line->setText(QApplication::translate("MainWindow", "MyRobot", nullptr));
        username_line->setText(QApplication::translate("MainWindow", "root", nullptr));
        connectButton->setText(QApplication::translate("MainWindow", "Verbinden", nullptr));
        disconnectButton->setText(QApplication::translate("MainWindow", "Trennen", nullptr));
        connection_label->setText(QApplication::translate("MainWindow", "<html><head/><body><p><span style=\" color:#00aa00;\">Verbunden</span> | <span style=\" color:#aa0000;\">Getrennt</span></p></body></html>", nullptr));
        status_label->setText(QApplication::translate("MainWindow", "Status:", nullptr));
        led_Label->setText(QString());
        menuDatei->setTitle(QApplication::translate("MainWindow", "Datei", nullptr));
        menuAnsicht->setTitle(QApplication::translate("MainWindow", "Ansicht", nullptr));
        menuEinstellungen->setTitle(QApplication::translate("MainWindow", "Einstellungen", nullptr));
        menuProfile_wechseln->setTitle(QApplication::translate("MainWindow", "Profile wechseln", nullptr));
        menuHilfe->setTitle(QApplication::translate("MainWindow", "Hilfe", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
